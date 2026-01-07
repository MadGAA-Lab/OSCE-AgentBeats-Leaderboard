#!/bin/bash
set -e

echo "🧪 開始運行所有測試..."
echo ""

echo "1️⃣ 基本測試"
echo "=================================================="
python3 tests/test_queries.py
echo ""

echo "2️⃣ 單個查詢測試"
echo "=================================================="
python3 test_single_query.py
echo ""

echo "3️⃣ 性能測試"
echo "=================================================="
python3 benchmark_queries.py
echo ""

echo "✅ 所有測試完成！"
