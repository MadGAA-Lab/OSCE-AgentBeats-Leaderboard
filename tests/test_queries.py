"""
Test queries from root queries.json file
"""
import json
import duckdb
from pathlib import Path

# Get root directory (parent of tests/)
ROOT_DIR = Path(__file__).parent.parent

print("Testing queries from root queries.json...")
print("="*60)

# Load queries from root
queries_path = ROOT_DIR / "tests" / "queries.json"
results_pattern = str(ROOT_DIR / "results" / "*.json")

with open(queries_path, 'r', encoding='utf-8') as f:
    queries = json.load(f)

success = []
failed = []

for query_info in queries:
    try:
        # Replace the results pattern in the query
        query = query_info['query'].replace("'results/*.json'", f"'{results_pattern}'")
        result = duckdb.sql(query)
        rows = result.fetchall()
        success.append(query_info['name'])
        print(f"✓ {query_info['name']}")
        print(f"  Results: {len(rows)} rows")
        if len(rows) > 0:
            print(f"  Sample: {rows[:2]}")
    except Exception as e:
        failed.append((query_info['name'], str(e)))
        print(f"✗ {query_info['name']}: {str(e)[:100]}")

print("\n" + "="*60)
print(f"Results: {len(success)} passed, {len(failed)} failed")

if failed:
    print("\nFailed queries:")
    for name, error in failed:
        print(f"  - {name}: {error[:100]}")
