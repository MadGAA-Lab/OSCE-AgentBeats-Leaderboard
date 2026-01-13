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

# Create DuckDB connection and load data
conn = duckdb.connect()
conn.execute(f"CREATE TABLE results AS SELECT * FROM read_json('{results_pattern}')")

success = []
failed = []
warnings = []

for query_info in queries:
    try:
        result = conn.sql(query_info['query'])
        rows = result.fetchall()
        columns = [desc[0] for desc in result.description]
        
        # Check if 'id' is the first column (required for leaderboard)
        if columns and columns[0] != 'id':
            warning_msg = f"First column is '{columns[0]}', but 'id' must be the first column"
            warnings.append((query_info['name'], warning_msg))
            print(f"⚠ {query_info['name']}")
            print(f"  WARNING: {warning_msg}")
            print(f"  Current columns: {columns}")
        else:
            success.append(query_info['name'])
            print(f"✓ {query_info['name']}")
        
        print(f"  Results: {len(rows)} rows")
        print(f"  Columns: {columns}")
        if len(rows) > 0:
            print(f"  Sample: {rows[:2]}")
    except Exception as e:
        failed.append((query_info['name'], str(e)))
        print(f"✗ {query_info['name']}: {str(e)[:100]}")

conn.close()

print("\n" + "="*60)
print(f"Results: {len(success)} passed, {len(warnings)} warnings, {len(failed)} failed")

if warnings:
    print("\n⚠ Queries with warnings (will fail on leaderboard):")
    for name, warning in warnings:
        print(f"  - {name}: {warning}")

if failed:
    print("\nFailed queries:")
    for name, error in failed:
        print(f"  - {name}: {error[:100]}")

# Exit with error code if there are failures or warnings
exit(len(failed) + len(warnings))
