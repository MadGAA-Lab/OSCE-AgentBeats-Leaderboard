#!/usr/bin/env python3
"""性能測試 - 測量所有查詢的執行時間"""

import time
import json
import duckdb

# 載入查詢
with open('tests/queries.json', 'r') as f:
    queries = json.load(f)

# 連接 DuckDB
conn = duckdb.connect()
conn.execute("CREATE TEMP TABLE results AS SELECT * FROM read_json_auto('results/*.json')")

print("=" * 80)
print("查詢性能測試")
print("=" * 80)
print(f"{'查詢名稱':<45} | {'結果數':<8} | {'執行時間':<12}")
print("-" * 80)

total_time = 0
for query_info in queries:
    start_time = time.time()
    result = conn.execute(query_info['query'])
    rows = result.fetchall()
    elapsed = time.time() - start_time
    total_time += elapsed

    print(f"{query_info['name']:<45} | {len(rows):>8} | {elapsed*1000:>9.2f} ms")

print("-" * 80)
print(f"{'總執行時間':<45} | {'':<8} | {total_time*1000:>9.2f} ms")
print("=" * 80)
print(f"\n平均每個查詢: {(total_time/len(queries))*1000:.2f} ms")
print(f"查詢總數: {len(queries)}")
