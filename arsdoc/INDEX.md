# 📇 文檔快速索引

> 快速找到你需要的文檔或工具

## 🎯 按目的查找

### 我想要測試

| 需求 | 文檔/工具 | 時間 |
|-----|----------|------|
| 快速驗證所有查詢 | `run_all_tests.sh` | 2 分鐘 |
| 查看詳細測試結果 | `test_single_query.py` | 3 分鐘 |
| 測試查詢性能 | `benchmark_queries.py` | 2 分鐘 |
| 學習測試方法 | TESTING_GUIDE.md | 12 分鐘 |

---

### 我想要了解查詢

| 需求 | 文檔 | 時間 |
|-----|------|------|
| 快速了解有哪些查詢 | QUERIES.md | 5 分鐘 |
| 詳細了解查詢修改 | QUERY_UPDATES.md | 15 分鐘 |
| 查看變更歷史 | CHANGELOG.md | 3 分鐘 |
| 查看查詢定義 | `../tests/queries.json` | 2 分鐘 |

---

### 我想要快速上手

| 需求 | 文檔 | 時間 |
|-----|------|------|
| 5 分鐘快速開始 | QUICKSTART.md | 5 分鐘 |
| 了解文檔結構 | README.md | 10 分鐘 |
| 查看結構圖 | STRUCTURE.md | 5 分鐘 |
| 查看本索引 | INDEX.md（本文件） | 2 分鐘 |

---

## 📚 按文檔類型查找

### 📖 指南類

- **[QUICKSTART.md](QUICKSTART.md)** - 快速上手指南
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - 完整測試指南
- **[README.md](README.md)** - 文檔中心導覽

### 📝 參考類

- **[QUERIES.md](QUERIES.md)** - 查詢參考文檔
- **[QUERY_UPDATES.md](QUERY_UPDATES.md)** - 查詢修改說明
- **[STRUCTURE.md](STRUCTURE.md)** - 文檔結構圖

### 📅 記錄類

- **[CHANGELOG.md](CHANGELOG.md)** - 變更日誌
- **[INDEX.md](INDEX.md)** - 本索引文件

### 🧪 工具類

- **[run_all_tests.sh](run_all_tests.sh)** - 一鍵測試腳本
- **[test_single_query.py](test_single_query.py)** - 單查詢測試
- **[benchmark_queries.py](benchmark_queries.py)** - 性能測試

---

## 👤 按角色查找

### 🆕 新手

**推薦閱讀順序：**
1. README.md → 文檔導覽
2. QUICKSTART.md → 快速上手
3. 運行 `run_all_tests.sh` → 實際測試

**預計時間：** 15 分鐘

---

### 💻 開發者

**推薦閱讀順序：**
1. README.md → 文檔導覽
2. QUERY_UPDATES.md → 了解變更
3. QUERIES.md → 查詢參考
4. 運行 `run_all_tests.sh` → 驗證

**預計時間：** 30 分鐘

---

### 🧪 測試工程師

**推薦閱讀順序：**
1. README.md → 文檔導覽
2. TESTING_GUIDE.md → 測試方法
3. 嘗試所有測試工具 → 實踐
4. QUERY_UPDATES.md → 了解細節

**預計時間：** 60 分鐘

---

### 🔧 維護者

**推薦閱讀順序：**
1. CHANGELOG.md → 變更歷史
2. STRUCTURE.md → 文檔結構
3. QUERY_UPDATES.md → 詳細變更
4. 所有測試工具 → 驗證

**預計時間：** 50 分鐘

---

## 🔍 按關鍵字查找

### A-D

- **AgentBeats 規範** → QUERY_UPDATES.md
- **API** → QUERIES.md
- **Benchmark** → benchmark_queries.py
- **CHANGELOG** → CHANGELOG.md
- **CI/CD** → TESTING_GUIDE.md
- **Debug** → test_single_query.py
- **DuckDB** → TESTING_GUIDE.md

### E-P

- **Empathy** → QUERIES.md
- **Error** → TESTING_GUIDE.md（故障排除）
- **JSON** → QUERY_UPDATES.md
- **Performance** → benchmark_queries.py
- **Persuasion** → QUERIES.md

### Q-Z

- **Query** → QUERIES.md, QUERY_UPDATES.md
- **Quick Start** → QUICKSTART.md
- **Safety** → QUERIES.md
- **Structure** → STRUCTURE.md
- **Success Rate** → QUERIES.md
- **Test** → TESTING_GUIDE.md, run_all_tests.sh

---

## 📊 文檔統計

| 類別 | 數量 | 總字數 | 總時間 |
|-----|------|--------|--------|
| 📖 指南 | 3 | ~6,700 字 | 27 分鐘 |
| 📝 參考 | 3 | ~7,600 字 | 25 分鐘 |
| 📅 記錄 | 2 | ~1,000 字 | 5 分鐘 |
| 🧪 工具 | 3 | - | - |
| **總計** | **11** | **~15,300 字** | **57 分鐘** |

---

## ⚡ 常用命令速查

```bash
# 測試
./arsdoc/run_all_tests.sh              # 運行所有測試
python3 tests/test_queries.py          # 基本測試
python3 arsdoc/test_single_query.py    # 詳細測試
python3 arsdoc/benchmark_queries.py    # 性能測試

# 查看文檔
cat arsdoc/QUICKSTART.md | less        # 快速開始
cat arsdoc/QUERIES.md | less           # 查詢參考
cat arsdoc/QUERY_UPDATES.md | less     # 詳細變更

# 檢查
ls -la arsdoc/                         # 查看所有文檔
ls -la tests/                          # 查看測試文件
ls -la results/                        # 查看結果文件
```

---

## 🔗 快速連結

### 文檔

- [文檔中心](README.md)
- [快速開始](QUICKSTART.md)
- [查詢參考](QUERIES.md)
- [測試指南](TESTING_GUIDE.md)
- [結構圖](STRUCTURE.md)

### 工具

- [一鍵測試](run_all_tests.sh)
- [單查詢測試](test_single_query.py)
- [性能測試](benchmark_queries.py)

### 配置

- [查詢定義](../tests/queries.json)
- [主測試](../tests/test_queries.py)
- [專案 README](../README.md)

---

## 🆘 遇到問題？

### 找不到想要的信息？

1. 查看 [README.md](README.md) 文檔導覽
2. 查看 [STRUCTURE.md](STRUCTURE.md) 結構圖
3. 使用本索引搜索關鍵字

### 測試遇到問題？

1. 查看 [QUICKSTART.md](QUICKSTART.md) 常見問題
2. 查看 [TESTING_GUIDE.md](TESTING_GUIDE.md) 故障排除
3. 運行 `python3 arsdoc/test_single_query.py` 調試

### 查詢相關問題？

1. 查看 [QUERIES.md](QUERIES.md) 查詢說明
2. 查看 [QUERY_UPDATES.md](QUERY_UPDATES.md) 修改細節
3. 檢查 `../tests/queries.json` 定義

---

**索引版本：** 1.0
**最後更新：** 2026-01-07
**文檔數量：** 11 個文件
