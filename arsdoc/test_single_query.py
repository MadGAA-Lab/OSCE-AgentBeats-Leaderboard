#!/usr/bin/env python3
"""測試單個查詢並顯示格式化結果"""

import duckdb
import json
from pathlib import Path

# 連接 DuckDB
conn = duckdb.connect()

# 創建 results 表
results_pattern = 'results/*.json'
conn.execute(f"CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('{results_pattern}')")

print("=" * 80)
print("單個查詢測試 - Detailed Performance Breakdown")
print("=" * 80)

# 測試 Detailed Performance Breakdown 查詢
query = """
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
"""

# 執行查詢
result = conn.execute(query)
rows = result.fetchall()
columns = [desc[0] for desc in result.description]

# 顯示結果
print("\n查詢結果：")
print(f"{'列名':<50} | 值")
print("-" * 80)
if rows:
    for row in rows:
        print(f"\n代理 ID: {row[0]}")
        for i, col in enumerate(columns[1:], 1):
            print(f"  {col:<40} | {row[i]}")
else:
    print("無結果")

print("\n" + "=" * 80)
print("列名：", columns)
print("結果行數：", len(rows))
print("=" * 80)
