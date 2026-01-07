# 快速開始測試指南

## 🚀 最快速的測試方法

### 1. 基本測試（推薦）

```bash
# 運行所有查詢測試
python3 tests/test_queries.py
```

**預期結果：**
```
✓ Overall Performance
✓ Empathy Rankings
✓ Persuasion Rankings
✓ Safety Rankings
✓ Success Rate
✓ Detailed Performance Breakdown
✓ Recent Submissions

Results: 7 passed, 0 failed
```

---

### 2. 測試單個查詢（詳細輸出）

```bash
python3 test_single_query.py
```

**預期結果：**
```
代理 ID: 019b8d97-18dc-7a10-bbf0-22ffc3f8e30e
  Empathy                          | 8.45
  Persuasion                       | 3.13
  Safety                           | 3.75
  Aggregate Score                  | 49.1
  Success Rate (%)                 | 100.0
  Sessions                         | 1
```

---

### 3. 性能測試

```bash
python3 benchmark_queries.py
```

**預期結果：**
```
查詢名稱                              | 結果數   | 執行時間
Overall Performance                  |      1  |   18.66 ms
Empathy Rankings                     |      1  |   25.50 ms
...
總執行時間                            |         |  151.87 ms
平均每個查詢: 21.70 ms
```

---

## 📋 前置需求檢查

### 檢查是否已安裝 DuckDB

```bash
python3 -c "import duckdb; print('✅ DuckDB 已安裝:', duckdb.__version__)"
```

### 如果沒有安裝

```bash
pip install duckdb --break-system-packages
```

### 檢查結果文件

```bash
# 確認有結果文件
ls -l results/*.json
```

---

## 🔍 測試場景

### 場景 A：快速驗證

**用途：** 確認查詢語法正確

```bash
python3 tests/test_queries.py
```

✅ 所有查詢通過 → 可以提交
❌ 有查詢失敗 → 需要修復

---

### 場景 B：查看具體數據

**用途：** 檢查查詢返回的實際數據

```bash
python3 test_single_query.py
```

可以編輯腳本中的查詢來測試不同的查詢。

---

### 場景 C：性能評估

**用途：** 確認查詢效率

```bash
python3 benchmark_queries.py
```

如果某個查詢超過 100ms，考慮優化。

---

## 🛠️ 常用調試命令

### 查看 JSON 結構

```bash
python3 -c "
import json
data = json.load(open('results/MadGAA-Lab-20260107-122911.json'))
print('Keys:', list(data.keys()))
print('Participants:', data['participants'])
print('Results count:', len(data['results']))
"
```

### 驗證查詢 JSON 格式

```bash
python3 -m json.tool tests/queries.json > /dev/null && echo "✅ JSON 有效"
```

### 測試特定查詢

```python
import json
import duckdb

# 讀取查詢
with open('tests/queries.json', 'r') as f:
    queries = json.load(f)

# 找到特定查詢
query = next(q for q in queries if q['name'] == 'Overall Performance')

# 執行
conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")
result = conn.execute(query['query'])
print(result.fetchall())
```

---

## ✅ 測試通過後的步驟

1. **提交變更**
```bash
git add tests/queries.json tests/test_queries.py
git commit -m "Update queries to AgentBeats official format"
git push
```

2. **創建 PR**
- 標題：`Update queries to AgentBeats official format`
- 描述：參考 `QUERY_UPDATES.md`

3. **等待 CI/CD**
- GitHub Actions 會自動運行測試
- 確認所有檢查通過 ✅

4. **合併**
- 查詢將自動部署到 AgentBeats 排行榜

---

## 🆘 遇到問題？

### 問題：找不到 duckdb

**解決方案：**
```bash
pip install duckdb --break-system-packages
```

### 問題：沒有結果文件

**解決方案：**
```bash
# 檢查目錄
ls results/

# 應該至少有一個 .json 文件
# 如果沒有，運行一次評估來生成結果
```

### 問題：查詢返回空結果

**解決方案：**
```bash
# 檢查 JSON 結構
python3 -c "
import json
data = json.load(open('results/MadGAA-Lab-20260107-122911.json'))
print('Has participants?', 'participants' in data)
print('Has doctor?', 'doctor' in data.get('participants', {}))
"
```

### 問題：查詢語法錯誤

**解決方案：**
1. 檢查 `tests/queries.json` 格式
2. 確認 SQL 語法正確
3. 運行單個查詢測試來調試

---

## 📚 更多資源

- 📖 詳細測試指南：[TESTING_GUIDE.md](TESTING_GUIDE.md)
- 📝 查詢修改說明：[QUERY_UPDATES.md](QUERY_UPDATES.md)
- 📊 查詢文檔：[QUERIES.md](QUERIES.md)
- 🔄 變更日誌：[CHANGELOG.md](CHANGELOG.md)

---

## 🎯 一鍵測試腳本

創建 `run_all_tests.sh`：

```bash
#!/bin/bash
set -e

echo "🧪 開始運行所有測試..."
echo ""

echo "1️⃣ 基本測試"
python3 tests/test_queries.py
echo ""

echo "2️⃣ 單個查詢測試"
python3 test_single_query.py
echo ""

echo "3️⃣ 性能測試"
python3 benchmark_queries.py
echo ""

echo "✅ 所有測試完成！"
```

使用方式：

```bash
chmod +x run_all_tests.sh
./run_all_tests.sh
```

---

**最後更新：** 2026-01-07
