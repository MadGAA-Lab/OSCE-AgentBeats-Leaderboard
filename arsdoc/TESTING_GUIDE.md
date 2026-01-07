# 測試運行指南

本文檔說明如何測試排行榜查詢系統。

## 快速開始

### 前置需求

```bash
# 檢查 Python 版本（需要 3.8+）
python3 --version

# 確認專案目錄
cd /home/arsene/OSCE-AgentBeats-Leaderboard
```

## 方法 1：使用測試腳本（推薦）

### 步驟 1：安裝依賴

```bash
# 安裝 DuckDB
pip install duckdb --break-system-packages
```

### 步驟 2：運行測試

```bash
# 運行所有查詢測試
python3 tests/test_queries.py
```

### 預期輸出

```
Testing queries from queries.json...
============================================================
✓ Overall Performance
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 49.1, 1)]
✓ Empathy Rankings
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 8.45, 1)]
✓ Persuasion Rankings
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 3.13, 1)]
✓ Safety Rankings
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 3.75, 1)]
✓ Success Rate
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 100.0, 1)]
✓ Detailed Performance Breakdown
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 8.45, 3.13, 3.75, 49.1, 100.0, 1)]
✓ Recent Submissions
  Results: 1 rows
  Sample: [(UUID('019b8d97-18dc-7a10-bbf0-22ffc3f8e30e'), 49.1, '2026-01-07T12:29:10.332470', 1)]

============================================================
Results: 7 passed, 0 failed
```

---

## 方法 2：使用 DuckDB CLI

### 步驟 1：安裝 DuckDB CLI

```bash
# 方法 A：使用 pip
pip install duckdb --break-system-packages

# 方法 B：下載二進制文件（推薦）
wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip
unzip duckdb_cli-linux-amd64.zip
chmod +x duckdb
sudo mv duckdb /usr/local/bin/
```

### 步驟 2：測試單個查詢

```bash
# 測試 Overall Performance 查詢
duckdb -c 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");' \
       -c 'SELECT t.participants.doctor AS id,
                  ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score",
                  COUNT(DISTINCT r.res.detail.assessment_id) AS "Assessments"
           FROM results t
           CROSS JOIN UNNEST(t.results) AS r(res)
           GROUP BY id
           ORDER BY "Overall Score" DESC'
```

### 步驟 3：互動式測試

```bash
# 啟動互動式 shell
duckdb

# 在 DuckDB shell 中執行
D CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json');
D .tables
D SELECT * FROM results LIMIT 1;

# 測試查詢
D SELECT t.participants.doctor AS id,
         ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score"
  FROM results t
  CROSS JOIN UNNEST(t.results) AS r(res)
  GROUP BY id;

# 退出
D .quit
```

---

## 方法 3：使用 Python 腳本直接測試

### 創建測試腳本

創建 `test_single_query.py`：

```python
import duckdb
import json
from pathlib import Path

# 連接 DuckDB
conn = duckdb.connect()

# 創建 results 表
results_pattern = 'results/*.json'
conn.execute(f"CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('{results_pattern}')")

# 測試查詢
query = """
SELECT t.participants.doctor AS id,
       ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score",
       COUNT(DISTINCT r.res.detail.assessment_id) AS "Assessments"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
GROUP BY id
ORDER BY "Overall Score" DESC
"""

# 執行並顯示結果
result = conn.execute(query)
print("Query Results:")
print(result.fetchdf())
```

### 運行測試

```bash
python3 test_single_query.py
```

---

## 方法 4：測試特定查詢

### 創建自定義測試腳本

創建 `test_specific.py`：

```python
import json
import duckdb

# 讀取查詢定義
with open('tests/queries.json', 'r') as f:
    queries = json.load(f)

# 連接 DuckDB
conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")

# 選擇要測試的查詢
query_name = "Detailed Performance Breakdown"  # 修改這裡測試不同查詢

# 找到並執行查詢
for q in queries:
    if q['name'] == query_name:
        print(f"Testing: {query_name}")
        print("="*60)
        result = conn.execute(q['query'])
        df = result.fetchdf()
        print(df)
        print("\nColumn names:")
        print(df.columns.tolist())
        break
```

### 運行

```bash
python3 test_specific.py
```

---

## 方法 5：驗證 JSON 結構

### 檢查結果文件結構

```bash
# 查看 JSON 結構
python3 -c "
import json
data = json.load(open('results/MadGAA-Lab-20260107-122911.json'))
print('Top level keys:', list(data.keys()))
print('Participants:', data['participants'])
print('Number of results:', len(data['results']))
print('First result keys:', list(data['results'][0].keys()))
print('Detail keys:', list(data['results'][0]['detail'].keys()))
"
```

### 檢查報告數據

```bash
# 查看報告結構
python3 -c "
import json
data = json.load(open('results/MadGAA-Lab-20260107-122911.json'))
report = data['results'][0]['detail']['reports'][0]
print('Report keys:', list(report.keys()))
print('Empathy:', report.get('overall_empathy'))
print('Persuasion:', report.get('overall_persuasion'))
print('Safety:', report.get('overall_safety'))
print('Aggregate Score:', report.get('aggregate_score'))
print('Final Outcome:', report.get('final_outcome'))
"
```

---

## 測試場景

### 場景 1：測試新增的結果文件

```bash
# 1. 添加新的結果文件到 results/
cp path/to/new_result.json results/

# 2. 運行測試
python3 tests/test_queries.py

# 3. 檢查結果數量是否增加
duckdb -c 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");' \
       -c 'SELECT COUNT(*) AS total_results FROM results'
```

### 場景 2：測試多個提交

```bash
# 查看有多少個結果文件
ls -l results/*.json | wc -l

# 測試查詢是否正確聚合多個文件
python3 tests/test_queries.py
```

### 場景 3：測試錯誤處理

```bash
# 創建一個錯誤的查詢
cat > test_error.py << 'EOF'
import duckdb
conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")

# 測試錯誤的查詢（缺少 id 列）
try:
    result = conn.execute("SELECT 'test' AS name FROM results LIMIT 1")
    print("Query succeeded (should fail in production)")
except Exception as e:
    print(f"Query failed: {e}")
EOF

python3 test_error.py
```

---

## 使用 GitHub Actions 測試

### 本地模擬 GitHub Actions

創建 `.github/workflows/test-queries.yml`：

```yaml
name: Test Queries

on:
  pull_request:
    paths:
      - 'tests/queries.json'
      - 'tests/test_queries.py'
      - 'results/*.json'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install duckdb

      - name: Run query tests
        run: python3 tests/test_queries.py

      - name: Verify all queries passed
        run: |
          if python3 tests/test_queries.py | grep -q "0 failed"; then
            echo "✅ All queries passed"
          else
            echo "❌ Some queries failed"
            exit 1
          fi
```

### 觸發測試

```bash
# 提交變更
git add tests/queries.json
git commit -m "Update queries"
git push

# GitHub Actions 會自動運行測試
```

---

## 性能測試

### 測試查詢執行時間

創建 `benchmark_queries.py`：

```python
import time
import json
import duckdb

# 載入查詢
with open('tests/queries.json', 'r') as f:
    queries = json.load(f)

# 連接 DuckDB
conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")

print("Query Performance Benchmark")
print("="*70)

for query_info in queries:
    start_time = time.time()
    result = conn.execute(query_info['query'])
    rows = result.fetchall()
    elapsed = time.time() - start_time

    print(f"{query_info['name']:40} | {len(rows):5} rows | {elapsed*1000:7.2f} ms")

print("="*70)
```

### 運行性能測試

```bash
python3 benchmark_queries.py
```

---

## 調試技巧

### 1. 檢查查詢語法

```bash
# 驗證查詢 JSON 格式
python3 -m json.tool tests/queries.json > /dev/null && echo "✅ JSON valid" || echo "❌ JSON invalid"
```

### 2. 逐步執行查詢

```python
import duckdb

conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")

# 步驟 1：查看原始數據
print("Step 1: Raw data")
result = conn.execute("SELECT * FROM results LIMIT 1")
print(result.fetchdf())

# 步驟 2：展開 results
print("\nStep 2: Unnest results")
result = conn.execute("""
    SELECT r.res.detail.mean_aggregate_score
    FROM results t
    CROSS JOIN UNNEST(t.results) AS r(res)
""")
print(result.fetchdf())

# 步驟 3：完整查詢
print("\nStep 3: Full query")
result = conn.execute("""
    SELECT t.participants.doctor AS id,
           ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS score
    FROM results t
    CROSS JOIN UNNEST(t.results) AS r(res)
    GROUP BY id
""")
print(result.fetchdf())
```

### 3. 查看查詢計劃

```bash
duckdb -c 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");' \
       -c 'EXPLAIN SELECT t.participants.doctor AS id FROM results t CROSS JOIN UNNEST(t.results) AS r(res) GROUP BY id'
```

---

## 常見問題排查

### 問題 1：找不到 duckdb 模組

```bash
# 解決方案
pip install duckdb --break-system-packages

# 或使用虛擬環境
python3 -m venv venv
source venv/bin/activate
pip install duckdb
```

### 問題 2：沒有結果文件

```bash
# 檢查結果目錄
ls -la results/

# 如果沒有文件，使用示例數據
# results/ 目錄應該包含至少一個 .json 文件
```

### 問題 3：查詢返回空結果

```bash
# 檢查 JSON 結構
python3 -c "
import json
data = json.load(open('results/MadGAA-Lab-20260107-122911.json'))
print('Has participants?', 'participants' in data)
print('Has results?', 'results' in data)
print('Results length:', len(data.get('results', [])))
"
```

### 問題 4：UUID 類型錯誤

如果看到 UUID 相關錯誤：

```python
# 在查詢中將 UUID 轉換為字符串
SELECT CAST(t.participants.doctor AS VARCHAR) AS id
```

---

## 持續集成建議

### 在 CI/CD 中運行測試

```bash
# 在部署前自動測試
#!/bin/bash
set -e

echo "Running query tests..."
python3 tests/test_queries.py

if [ $? -eq 0 ]; then
    echo "✅ All tests passed"
else
    echo "❌ Tests failed"
    exit 1
fi
```

### Pre-commit Hook

創建 `.git/hooks/pre-commit`：

```bash
#!/bin/bash

# 如果修改了查詢文件，運行測試
if git diff --cached --name-only | grep -q "tests/queries.json"; then
    echo "Running query tests..."
    python3 tests/test_queries.py || exit 1
fi
```

---

## 下一步

測試通過後：

1. ✅ 提交變更到 Git
2. ✅ 創建 Pull Request
3. ✅ 等待 GitHub Actions 驗證
4. ✅ 合併到主分支
5. ✅ 查詢將自動部署到 AgentBeats 排行榜

---

## 相關資源

- `tests/test_queries.py` - 主要測試腳本
- `tests/queries.json` - 查詢定義文件
- `QUERY_UPDATES.md` - 詳細修改說明
- `QUERIES.md` - 查詢文檔

**最後更新：** 2026-01-07
