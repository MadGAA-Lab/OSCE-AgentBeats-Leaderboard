# 📚 OSCE-AgentBeats 查詢系統文檔中心

本目錄包含排行榜查詢系統的完整文檔和測試工具。

**更新日期：** 2026-01-07
**版本：** 1.0
**主要變更：** 更新查詢格式以符合 AgentBeats 官方規範

---

## 📖 文檔導覽

### 🚀 快速開始

**想要快速測試？從這裡開始：**

- **[QUICKSTART.md](QUICKSTART.md)** - 5 分鐘快速上手指南
  - 最快速的測試方法
  - 三種測試場景演示
  - 一鍵測試命令
  - 常見問題快速解答

### 📝 核心文檔

#### 1. [QUERY_UPDATES.md](QUERY_UPDATES.md) - 查詢修改詳細說明
**適合：** 想了解所有變更細節的開發者

**內容：**
- ✅ 更新目的與官方規範說明
- ✅ 所有 7 個查詢的修改前後對比
- ✅ 每個查詢的詳細變更說明
- ✅ JSON 結構參考
- ✅ 測試結果與統計

**何時閱讀：**
- 需要了解為什麼要修改
- 想知道每個查詢具體改了什麼
- 準備提交 Pull Request
- 需要向團隊解釋變更

---

#### 2. [QUERIES.md](QUERIES.md) - 查詢文檔
**適合：** 需要查詢參考的開發者和使用者

**內容：**
- ✅ 查詢格式說明
- ✅ 7 個查詢的詳細說明
- ✅ 每個查詢的列定義
- ✅ JSON 結構參考
- ✅ 關鍵字段說明

**何時閱讀：**
- 想知道有哪些查詢可用
- 需要理解查詢結果的含義
- 準備編寫新查詢
- 需要查詢參考文檔

---

#### 3. [TESTING_GUIDE.md](TESTING_GUIDE.md) - 完整測試指南
**適合：** 需要全面測試的開發者

**內容：**
- ✅ 5 種詳細測試方法
- ✅ 每種方法的步驟說明
- ✅ DuckDB 安裝與配置
- ✅ 互動式測試方法
- ✅ 性能測試指南
- ✅ 調試技巧
- ✅ 故障排除指南
- ✅ CI/CD 集成建議

**何時閱讀：**
- 需要全面的測試流程
- 遇到測試問題需要排查
- 想學習不同的測試方法
- 準備集成到 CI/CD

---

#### 4. [CHANGELOG.md](CHANGELOG.md) - 變更日誌
**適合：** 需要追蹤變更歷史的所有人

**內容：**
- ✅ 變更摘要
- ✅ 新增功能
- ✅ 查詢對比表
- ✅ 測試結果
- ✅ Breaking Changes
- ✅ 遷移指南

**何時閱讀：**
- 想快速了解有什麼變更
- 需要向團隊報告更新
- 檢查是否有 Breaking Changes
- 需要遷移現有代碼

---

## 🧪 測試工具

### 腳本說明

#### 1. [run_all_tests.sh](run_all_tests.sh) - 一鍵運行所有測試 ⭐️
**推薦指數：** ⭐⭐⭐⭐⭐

```bash
chmod +x arsdoc/run_all_tests.sh
./arsdoc/run_all_tests.sh
```

**功能：**
- 運行所有三種測試
- 清晰的輸出格式
- 自動生成測試報告

**適用場景：**
- ✅ 日常快速驗證
- ✅ 提交前完整測試
- ✅ CI/CD 集成

---

#### 2. [test_single_query.py](test_single_query.py) - 單個查詢詳細測試
**推薦指數：** ⭐⭐⭐⭐

```bash
python3 arsdoc/test_single_query.py
```

**功能：**
- 測試單個查詢並格式化輸出
- 顯示所有列和數值
- 便於調試和驗證

**適用場景：**
- ✅ 調試特定查詢
- ✅ 查看實際數據
- ✅ 驗證查詢邏輯

---

#### 3. [benchmark_queries.py](benchmark_queries.py) - 性能測試
**推薦指數：** ⭐⭐⭐

```bash
python3 arsdoc/benchmark_queries.py
```

**功能：**
- 測量所有查詢的執行時間
- 計算平均和總執行時間
- 性能分析

**適用場景：**
- ✅ 優化查詢性能
- ✅ 比較不同版本
- ✅ 性能回歸測試

---

## 🎯 使用場景指南

### 場景 1：我是新手，想快速測試

**推薦路徑：**
1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md)
2. 🧪 運行 `./arsdoc/run_all_tests.sh`
3. ✅ 看到 "7 passed, 0 failed" 就成功了！

---

### 場景 2：我要提交 Pull Request

**推薦路徑：**
1. 📖 閱讀 [QUERY_UPDATES.md](QUERY_UPDATES.md) - 了解所有變更
2. 🧪 運行 `./arsdoc/run_all_tests.sh` - 確保測試通過
3. 📝 使用 [QUERY_UPDATES.md](QUERY_UPDATES.md) 內容作為 PR 描述
4. 📊 附上測試結果截圖

---

### 場景 3：我要編寫新查詢

**推薦路徑：**
1. 📖 閱讀 [QUERIES.md](QUERIES.md) - 了解查詢格式和規範
2. 📖 參考 [QUERY_UPDATES.md](QUERY_UPDATES.md) - 查看示例
3. 🧪 使用 `test_single_query.py` 測試新查詢
4. 📖 閱讀 [TESTING_GUIDE.md](TESTING_GUIDE.md) - 學習完整測試流程

---

### 場景 4：遇到測試問題

**推薦路徑：**
1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md) - 檢查常見問題
2. 📖 閱讀 [TESTING_GUIDE.md](TESTING_GUIDE.md) - 查看故障排除章節
3. 🧪 逐步運行單個測試定位問題
4. 📝 檢查 [CHANGELOG.md](CHANGELOG.md) 是否有相關變更

---

### 場景 5：我要了解性能

**推薦路徑：**
1. 🧪 運行 `python3 arsdoc/benchmark_queries.py`
2. 📖 查看 [TESTING_GUIDE.md](TESTING_GUIDE.md) 的性能測試章節
3. 📊 分析執行時間報告
4. 🔧 如有需要，優化慢查詢

---

## 📊 文檔結構圖

```
arsdoc/
├── README.md                    # 📚 本文件 - 文檔導覽中心
│
├── 📖 快速開始
│   └── QUICKSTART.md           # ⚡ 5 分鐘快速上手
│
├── 📝 核心文檔
│   ├── QUERY_UPDATES.md        # 🔄 查詢修改詳細說明
│   ├── QUERIES.md              # 📊 查詢參考文檔
│   ├── TESTING_GUIDE.md        # 🧪 完整測試指南
│   └── CHANGELOG.md            # 📅 變更日誌
│
└── 🧪 測試工具
    ├── run_all_tests.sh        # 🚀 一鍵運行所有測試
    ├── test_single_query.py    # 🔍 單個查詢詳細測試
    └── benchmark_queries.py    # ⚡ 性能測試工具
```

---

## 📈 文檔統計

| 類型 | 數量 | 說明 |
|-----|------|------|
| 📖 文檔 | 5 | 核心文檔和指南 |
| 🧪 腳本 | 3 | 測試和工具腳本 |
| 📊 查詢 | 7 | 排行榜查詢定義 |
| ⏱️ 總字數 | ~15,000+ | 詳細完整的文檔 |

---

## 🎯 快速命令參考

### 最常用的命令

```bash
# 1. 運行所有測試（最推薦）
./arsdoc/run_all_tests.sh

# 2. 快速驗證
python3 tests/test_queries.py

# 3. 查看詳細結果
python3 arsdoc/test_single_query.py

# 4. 性能測試
python3 arsdoc/benchmark_queries.py
```

### 查看文檔

```bash
# 快速開始
cat arsdoc/QUICKSTART.md | less

# 完整測試指南
cat arsdoc/TESTING_GUIDE.md | less

# 查詢修改說明
cat arsdoc/QUERY_UPDATES.md | less
```

---

## 🔗 相關資源

### 專案文件

- `../tests/queries.json` - 查詢定義文件（7 個查詢）
- `../tests/test_queries.py` - 主測試腳本
- `../results/*.json` - 測試數據文件
- `../README.md` - 專案主文檔

### 外部連結

- [AgentBeats 官網](https://agentbeats.dev)
- [OSCE-Project GitHub](https://github.com/MadGAA-Lab/OSCE-Project)
- [DuckDB 文檔](https://duckdb.org/docs/)

---

## 📝 更新日誌摘要

### 2026-01-07 - v1.0

**主要變更：**
- ✅ 更新所有查詢以符合 AgentBeats 官方規範
- ✅ 第一列改為 `id`（AgentBeats 要求）
- ✅ 使用人類可讀的列名
- ✅ 新增 "Detailed Performance Breakdown" 查詢
- ✅ 創建完整的測試工具和文檔

**測試結果：**
- ✅ 7/7 查詢通過
- ✅ 平均查詢時間：~20ms
- ✅ 所有數據驗證正確

---

## 💡 提示與技巧

### 提示 1：文檔閱讀順序

**新手推薦順序：**
1. QUICKSTART.md → 快速上手
2. QUERIES.md → 了解查詢
3. TESTING_GUIDE.md → 深入學習

**開發者推薦順序：**
1. QUERY_UPDATES.md → 了解變更
2. TESTING_GUIDE.md → 測試方法
3. CHANGELOG.md → 追蹤歷史

---

### 提示 2：測試策略

**日常開發：**
```bash
python3 tests/test_queries.py  # 快速驗證
```

**提交前：**
```bash
./arsdoc/run_all_tests.sh  # 完整測試
```

**調試時：**
```bash
python3 arsdoc/test_single_query.py  # 詳細輸出
```

---

### 提示 3：文件命名規範

所有文檔遵循以下命名規範：
- 全大寫：核心文檔（`README.md`, `CHANGELOG.md`）
- 大寫+描述：指南文檔（`TESTING_GUIDE.md`）
- 小寫+下劃線：腳本文件（`test_single_query.py`）

---

## 🆘 需要幫助？

### 問題類別

1. **測試問題** → 查看 [TESTING_GUIDE.md](TESTING_GUIDE.md) 故障排除章節
2. **查詢問題** → 查看 [QUERIES.md](QUERIES.md) 和 [QUERY_UPDATES.md](QUERY_UPDATES.md)
3. **快速問題** → 查看 [QUICKSTART.md](QUICKSTART.md) 常見問題
4. **歷史問題** → 查看 [CHANGELOG.md](CHANGELOG.md)

### 聯繫方式

- 📧 GitHub Issues: [開啟 Issue](https://github.com/MadGAA-Lab/OSCE-AgentBeats-Leaderboard/issues)
- 💬 GitHub Discussions: [參與討論](https://github.com/MadGAA-Lab/OSCE-AgentBeats-Leaderboard/discussions)

---

## ✅ 文檔檢查清單

使用本文檔中心前，確保：

- [ ] 已安裝 Python 3.8+
- [ ] 已安裝 DuckDB (`pip install duckdb`)
- [ ] `results/` 目錄中有至少一個 .json 文件
- [ ] 所有測試腳本有執行權限

快速檢查：
```bash
python3 --version          # 檢查 Python 版本
python3 -c "import duckdb" # 檢查 DuckDB
ls results/*.json          # 檢查結果文件
```

---

## 🎓 學習路徑

### 初級（第 1 天）
1. ✅ 閱讀 QUICKSTART.md
2. ✅ 運行 run_all_tests.sh
3. ✅ 理解測試輸出

### 中級（第 2-3 天）
1. ✅ 閱讀 QUERIES.md
2. ✅ 理解每個查詢的作用
3. ✅ 嘗試修改 test_single_query.py

### 高級（第 4-7 天）
1. ✅ 深入閱讀 TESTING_GUIDE.md
2. ✅ 學習性能優化
3. ✅ 編寫自定義查詢
4. ✅ 集成到 CI/CD

---

**感謝使用本文檔中心！** 🎉

如有問題或建議，請隨時提出 Issue 或 PR。

---

**維護者：** Claude Code
**最後更新：** 2026-01-07
**文檔版本：** 1.0
**專案版本：** OSCE-AgentBeats-Leaderboard
