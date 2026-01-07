# 排行榜查詢更新說明

## 更新目的

根據 AgentBeats 官方規範，將所有排行榜查詢格式更新為標準格式。

## 官方規範要求

根據 AgentBeats 官方文檔（Appendix A: Writing Leaderboard Queries），所有查詢必須遵循以下規範：

1. **第一列必須是 `id`**：AgentBeats agent ID 必須是第一列
2. **使用 `FROM results` 表**：系統自動將 JSON 結果讀取到 `results` 表
3. **使用人類可讀的列名**：使用 `AS "Column Name"` 設定列名

### 標準查詢模板

```sql
SELECT
    id,           -- AgentBeats agent ID (必須是第一列)
    ...           -- 其他列使用 AS 設定人類可讀的名稱
FROM results      -- AgentBeats 自動讀取的表
-- WHERE, GROUP BY, ORDER BY 等...
```

## 修改內容

### 修改前後對比

#### ❌ 修改前（不符合規範）

```json
{
  "name": "Overall Performance",
  "query": "SELECT results.participants.doctor AS agent_id, res.detail.mean_aggregate_score AS score, res.detail.timestamp AS timestamp FROM read_json_auto('results/*.json') AS results CROSS JOIN UNNEST(results.results) AS r(res) ORDER BY score DESC"
}
```

**問題：**
- 第一列是 `agent_id` 而不是 `id`
- 使用 `read_json_auto('results/*.json')` 而不是 `FROM results`
- 列名不夠人性化（`score` vs `"Overall Score"`）

#### ✅ 修改後（符合規範）

```json
{
  "name": "Overall Performance",
  "query": "SELECT t.participants.doctor AS id, ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS \"Overall Score\", COUNT(DISTINCT r.res.detail.assessment_id) AS \"Assessments\" FROM results t CROSS JOIN UNNEST(t.results) AS r(res) GROUP BY id ORDER BY \"Overall Score\" DESC"
}
```

**改進：**
- ✅ 第一列改為 `id`
- ✅ 使用 `FROM results t`
- ✅ 人類可讀的列名：`"Overall Score"`, `"Assessments"`
- ✅ 數值四捨五入到 2 位小數
- ✅ 添加評估計數

---

### 所有查詢的詳細修改

#### 1. Overall Performance（總體表現）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       res.detail.mean_aggregate_score AS score,
       res.detail.timestamp AS timestamp
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
ORDER BY score DESC
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score",
       COUNT(DISTINCT r.res.detail.assessment_id) AS "Assessments"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
GROUP BY id
ORDER BY "Overall Score" DESC
```

**變更說明：**
- 第一列改為 `id`
- 添加 `ROUND()` 函數，保留 2 位小數
- 使用人類可讀的列名
- 添加評估計數
- 移除不必要的 timestamp

---

#### 2. Empathy Rankings（同理心排名）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       AVG(rep.overall_empathy) AS empathy_score,
       COUNT(*) AS sessions
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
CROSS JOIN UNNEST(res.detail.reports) AS rp(rep)
WHERE rep.overall_empathy IS NOT NULL
GROUP BY agent_id
ORDER BY empathy_score DESC
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(AVG(rep.rep.overall_empathy), 2) AS "Empathy Score",
       COUNT(DISTINCT rep.rep.session_id) AS "Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.reports) AS rep(rep)
WHERE rep.rep.overall_empathy IS NOT NULL
GROUP BY id
ORDER BY "Empathy Score" DESC
```

**變更說明：**
- 第一列改為 `id`
- 分數四捨五入到 2 位小數
- 使用 `"Empathy Score"` 作為列名
- 使用 `COUNT(DISTINCT)` 避免重複計數

---

#### 3. Persuasion Rankings（說服力排名）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       AVG(rep.overall_persuasion) AS persuasion_score,
       COUNT(*) AS sessions
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
CROSS JOIN UNNEST(res.detail.reports) AS rp(rep)
WHERE rep.overall_persuasion IS NOT NULL
GROUP BY agent_id
ORDER BY persuasion_score DESC
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(AVG(rep.rep.overall_persuasion), 2) AS "Persuasion Score",
       COUNT(DISTINCT rep.rep.session_id) AS "Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.reports) AS rep(rep)
WHERE rep.rep.overall_persuasion IS NOT NULL
GROUP BY id
ORDER BY "Persuasion Score" DESC
```

**變更說明：**
- 第一列改為 `id`
- 分數四捨五入到 2 位小數
- 使用 `"Persuasion Score"` 作為列名
- 使用 `COUNT(DISTINCT)` 避免重複計數

---

#### 4. Safety Rankings（安全性排名）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       AVG(rep.overall_safety) AS safety_score,
       COUNT(*) AS sessions
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
CROSS JOIN UNNEST(res.detail.reports) AS rp(rep)
WHERE rep.overall_safety IS NOT NULL
GROUP BY agent_id
ORDER BY safety_score DESC
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(AVG(rep.rep.overall_safety), 2) AS "Safety Score",
       COUNT(DISTINCT rep.rep.session_id) AS "Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.reports) AS rep(rep)
WHERE rep.rep.overall_safety IS NOT NULL
GROUP BY id
ORDER BY "Safety Score" DESC
```

**變更說明：**
- 第一列改為 `id`
- 分數四捨五入到 2 位小數
- 使用 `"Safety Score"` 作為列名
- 使用 `COUNT(DISTINCT)` 避免重複計數

---

#### 5. Success Rate（成功率）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       ROUND(SUM(CASE WHEN sess.final_outcome = 'patient_accepted' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS success_rate,
       COUNT(*) AS total_sessions
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
CROSS JOIN UNNEST(res.detail.sessions) AS s(sess)
GROUP BY agent_id
ORDER BY success_rate DESC
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(SUM(CASE WHEN rep.rep.final_outcome = 'patient_accepted' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS "Success Rate (%)",
       COUNT(*) AS "Total Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.reports) AS rep(rep)
GROUP BY id
ORDER BY "Success Rate (%)" DESC
```

**變更說明：**
- 第一列改為 `id`
- 使用 `"Success Rate (%)"` 作為列名（更清晰）
- 使用 `"Total Sessions"` 作為列名
- 從 `reports` 而非 `sessions` 計算（更準確）

---

#### 6. Detailed Performance Breakdown（詳細表現分析）**【新增】**

```sql
SELECT t.participants.doctor AS id,
       ROUND(AVG(rep.rep.overall_empathy), 2) AS "Empathy",
       ROUND(AVG(rep.rep.overall_persuasion), 2) AS "Persuasion",
       ROUND(AVG(rep.rep.overall_safety), 2) AS "Safety",
       ROUND(AVG(rep.rep.aggregate_score), 2) AS "Aggregate Score",
       ROUND(SUM(CASE WHEN rep.rep.final_outcome = 'patient_accepted' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS "Success Rate (%)",
       COUNT(*) AS "Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.reports) AS rep(rep)
GROUP BY id
ORDER BY "Aggregate Score" DESC
```

**新增原因：**
- 提供所有核心指標的綜合視圖
- 方便快速比較各 agent 的全面表現
- 一次查詢獲得所有關鍵數據

---

#### 7. Recent Submissions（最近提交）

**修改前：**
```sql
SELECT results.participants.doctor AS agent_id,
       res.detail.mean_aggregate_score AS score,
       res.detail.timestamp AS timestamp
FROM read_json_auto('results/*.json') AS results
CROSS JOIN UNNEST(results.results) AS r(res)
ORDER BY timestamp DESC
LIMIT 10
```

**修改後：**
```sql
SELECT t.participants.doctor AS id,
       ROUND(r.res.detail.mean_aggregate_score, 2) AS "Score",
       r.res.detail.timestamp AS "Timestamp",
       COUNT(s.sess) AS "Sessions"
FROM results t
CROSS JOIN UNNEST(t.results) AS r(res)
CROSS JOIN UNNEST(r.res.detail.sessions) AS s(sess)
GROUP BY id, "Score", "Timestamp"
ORDER BY "Timestamp" DESC
LIMIT 10
```

**變更說明：**
- 第一列改為 `id`
- 分數四捨五入到 2 位小數
- 使用人類可讀的列名
- 添加 sessions 計數

---

#### ❌ 移除的查詢

**Persona Performance**

```sql
-- 此查詢已移除，因為不符合以 agent 為中心的排行榜格式
-- AgentBeats 排行榜應該以 agent ID 為主，而非 persona ID
```

---

## 測試結果

### 測試環境

```bash
python3 tests/test_queries.py
```

### 測試輸出

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

### 測試數據說明

測試使用的真實數據來自 `results/MadGAA-Lab-20260107-122911.json`：
- Agent ID: `019b8d97-18dc-7a10-bbf0-22ffc3f8e30e`
- Overall Score: 49.1
- Empathy Score: 8.45/10
- Persuasion Score: 3.13/10
- Safety Score: 3.75/10
- Success Rate: 100% (1/1 session)

---

## 如何在本地測試

### 方法 1：使用測試腳本

```bash
# 安裝 DuckDB
pip install duckdb

# 運行測試
python3 tests/test_queries.py
```

### 方法 2：使用 DuckDB CLI

```bash
# 創建 results 表並執行查詢
duckdb -c 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");' \
       -c 'SELECT t.participants.doctor AS id, ROUND(AVG(r.res.detail.mean_aggregate_score), 2) AS "Overall Score" FROM results t CROSS JOIN UNNEST(t.results) AS r(res) GROUP BY id ORDER BY "Overall Score" DESC'
```

### 方法 3：互動式測試

```bash
# 啟動 DuckDB 互動 shell
duckdb -cmd 'CREATE TEMP TABLE results AS SELECT * FROM read_json_auto("results/*.json");'

# 在 shell 中執行查詢
D SELECT * FROM results;
D SELECT t.participants.doctor AS id FROM results t LIMIT 1;
```

---

## 變更影響

### ✅ 對現有提交的影響

**無影響** - 所有現有的 `results/*.json` 文件無需修改，查詢會自動適配。

### ✅ 對排行榜顯示的影響

- 列名更友善、更易讀
- 數值顯示更精確（2 位小數）
- 排序邏輯更合理

### ✅ 對測試的影響

- 測試現在使用官方格式
- 測試結果更準確
- 更容易本地調試

---

## 參考資料

### AgentBeats 官方文檔

根據 **Appendix A: Writing Leaderboard Queries**：

```sql
-- This is a DuckDB SQL query over `read_json_auto('results/*.json') AS results`
SELECT
    id, -- The AgentBeats agent ID is always required to be the first column
    ... -- Your columns go here. Use `AS` to set human-readable column names.
FROM results -- The AgentBeats app automatically reads the JSON results into this table
-- WHERE, GROUP BY, LIMIT, etc. go here if needed
```

### JSON 結構參考

```json
{
  "participants": {
    "doctor": "019b8d97-18dc-7a10-bbf0-22ffc3f8e30e"
  },
  "results": [
    {
      "winner": "doctor",
      "detail": {
        "assessment_id": "uuid",
        "timestamp": "2026-01-07T12:29:10.332470",
        "mean_aggregate_score": 49.1,
        "sessions": [...],
        "reports": [
          {
            "session_id": "uuid",
            "final_outcome": "patient_accepted",
            "overall_empathy": 8.45,
            "overall_persuasion": 3.13,
            "overall_safety": 3.75,
            "aggregate_score": 49.1
          }
        ]
      }
    }
  ]
}
```

---

## 總結

### 主要改進

1. ✅ **符合官方規範**：所有查詢現在完全符合 AgentBeats 官方格式
2. ✅ **更好的可讀性**：使用人類可讀的列名
3. ✅ **更精確的數據**：數值四捨五入到適當位數
4. ✅ **完整的測試**：所有查詢都通過驗證
5. ✅ **新增查詢**：Detailed Performance Breakdown 提供綜合視圖

### 查詢統計

| 狀態 | 數量 | 查詢名稱 |
|-----|------|---------|
| ✅ 更新 | 6 | Overall Performance, Empathy Rankings, Persuasion Rankings, Safety Rankings, Success Rate, Recent Submissions |
| ✅ 新增 | 1 | Detailed Performance Breakdown |
| ❌ 移除 | 1 | Persona Performance |
| **總計** | **7** | **活躍查詢** |

### 下一步

查詢已經完全符合 AgentBeats 官方規範，可以直接使用：

1. 提交到 AgentBeats 平台
2. 查詢將自動在排行榜上顯示
3. 所有數據會正確聚合和排序

---

## 相關文件

- `tests/queries.json` - 查詢定義文件
- `tests/test_queries.py` - 查詢測試腳本
- `QUERIES.md` - 查詢文檔
- `CHANGELOG.md` - 變更日誌
- `README.md` - 專案說明（已更新）

---

**更新日期：** 2026-01-07
**更新人員：** Claude Code
**版本：** 1.0
