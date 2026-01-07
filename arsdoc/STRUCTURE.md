# 📂 文檔結構圖

## 完整目錄結構

```
OSCE-AgentBeats-Leaderboard/
│
├── 📚 arsdoc/                           # 文檔中心（你在這裡）
│   ├── README.md                       # 📖 文檔導覽中心（從這裡開始）
│   ├── STRUCTURE.md                    # 📂 本文件 - 結構圖
│   │
│   ├── 🚀 快速開始
│   │   └── QUICKSTART.md              # ⚡ 5 分鐘快速上手
│   │
│   ├── 📝 核心文檔
│   │   ├── QUERY_UPDATES.md           # 🔄 查詢修改詳細說明
│   │   ├── QUERIES.md                 # 📊 查詢參考文檔
│   │   ├── TESTING_GUIDE.md           # 🧪 完整測試指南
│   │   └── CHANGELOG.md               # 📅 變更日誌
│   │
│   └── 🧪 測試工具
│       ├── run_all_tests.sh           # 🚀 一鍵測試（最推薦）
│       ├── test_single_query.py       # 🔍 單查詢測試
│       └── benchmark_queries.py       # ⚡ 性能測試
│
├── 📊 tests/                           # 測試目錄
│   ├── queries.json                   # 查詢定義（7 個查詢）
│   └── test_queries.py                # 主測試腳本
│
├── 📈 results/                         # 評估結果
│   └── *.json                         # 結果文件
│
├── 📋 submissions/                     # 提交記錄
│   ├── *.toml                         # 提交配置
│   └── *.provenance.json              # 來源資訊
│
├── 🔧 工具腳本
│   ├── generate_compose.py           # Docker Compose 生成器
│   └── record_provenance.py          # 來源記錄器
│
├── ⚙️ 配置文件
│   ├── scenario.toml                  # 場景配置
│   └── .github/workflows/             # CI/CD 配置
│       └── run-scenario.yml
│
└── 📖 專案文檔
    ├── README.md                      # 專案主文檔
    ├── LICENSE                        # 授權文件
    └── .gitignore                     # Git 忽略規則
```

---

## 文檔層級關係

### Level 1: 入口文檔（必讀）

```
📖 /README.md
   └── 專案概述、快速開始、使用說明
       │
       └── 指向 → 📚 arsdoc/README.md
```

### Level 2: 文檔中心（導覽）

```
📚 arsdoc/README.md
   ├── 📖 文檔導覽和索引
   ├── 🎯 使用場景指南
   ├── 🗺️ 學習路徑
   └── 🔗 快速命令參考
       │
       ├─→ QUICKSTART.md        (快速開始)
       ├─→ QUERY_UPDATES.md     (詳細變更)
       ├─→ QUERIES.md           (查詢參考)
       ├─→ TESTING_GUIDE.md     (測試指南)
       └─→ CHANGELOG.md         (變更日誌)
```

### Level 3: 專題文檔（深入）

```
📝 核心文檔
│
├── QUICKSTART.md
│   ├── 3 種測試方法
│   ├── 常用場景
│   ├── 一鍵命令
│   └── 快速故障排除
│
├── QUERY_UPDATES.md
│   ├── 修改目的
│   ├── 7 個查詢對比
│   ├── 變更說明
│   ├── JSON 結構
│   └── 測試結果
│
├── QUERIES.md
│   ├── 查詢格式
│   ├── 7 個查詢說明
│   ├── 列定義
│   ├── 使用示例
│   └── 關鍵字段
│
├── TESTING_GUIDE.md
│   ├── 5 種測試方法
│   ├── 詳細步驟
│   ├── DuckDB 使用
│   ├── 調試技巧
│   ├── 性能測試
│   └── CI/CD 集成
│
└── CHANGELOG.md
    ├── 變更摘要
    ├── 新增功能
    ├── Breaking Changes
    └── 遷移指南
```

### Level 4: 測試工具（實踐）

```
🧪 測試工具
│
├── run_all_tests.sh          ⭐⭐⭐⭐⭐
│   └── 運行全部 3 種測試
│
├── test_single_query.py      ⭐⭐⭐⭐
│   └── 詳細測試單個查詢
│
└── benchmark_queries.py      ⭐⭐⭐
    └── 性能分析
```

---

## 文件大小與字數統計

| 文件 | 大小 | 行數 | 字數（約） | 閱讀時間 |
|-----|------|------|-----------|---------|
| README.md | 9.8 KB | 268 行 | ~2,500 字 | 10 分鐘 |
| QUICKSTART.md | 4.9 KB | 141 行 | ~1,200 字 | 5 分鐘 |
| QUERY_UPDATES.md | 13.7 KB | 434 行 | ~3,500 字 | 15 分鐘 |
| QUERIES.md | 4.1 KB | 118 行 | ~1,000 字 | 5 分鐘 |
| TESTING_GUIDE.md | 11.6 KB | 318 行 | ~3,000 字 | 12 分鐘 |
| CHANGELOG.md | 2.3 KB | 71 行 | ~600 字 | 3 分鐘 |
| **總計** | **46.4 KB** | **1,350 行** | **~12,000 字** | **50 分鐘** |

---

## 閱讀路徑推薦

### 🎯 路徑 1：新手快速上手（15 分鐘）

```
1. arsdoc/README.md (導覽)          → 5 分鐘
2. arsdoc/QUICKSTART.md             → 5 分鐘
3. 運行 ./arsdoc/run_all_tests.sh    → 2 分鐘
4. 查看結果                          → 3 分鐘
```

**適合：** 第一次使用的用戶

---

### 🎯 路徑 2：開發者深入了解（30 分鐘）

```
1. arsdoc/README.md (導覽)          → 5 分鐘
2. arsdoc/QUERY_UPDATES.md          → 15 分鐘
3. arsdoc/QUERIES.md                → 5 分鐘
4. 運行測試並閱讀代碼                  → 5 分鐘
```

**適合：** 需要提交 PR 的開發者

---

### 🎯 路徑 3：測試專家全面掌握（60 分鐘）

```
1. arsdoc/README.md (導覽)          → 5 分鐘
2. arsdoc/TESTING_GUIDE.md          → 20 分鐘
3. 嘗試 5 種測試方法                  → 20 分鐘
4. arsdoc/QUERY_UPDATES.md          → 10 分鐘
5. 性能測試和優化                     → 5 分鐘
```

**適合：** 負責測試和 CI/CD 的工程師

---

### 🎯 路徑 4：查詢開發者（45 分鐘）

```
1. arsdoc/README.md (導覽)          → 5 分鐘
2. arsdoc/QUERIES.md                → 10 分鐘
3. arsdoc/QUERY_UPDATES.md          → 15 分鐘
4. 研究 queries.json                → 10 分鐘
5. 編寫測試查詢                      → 5 分鐘
```

**適合：** 需要編寫或修改查詢的開發者

---

## 文檔依賴關係

```mermaid
graph TD
    A[/README.md<br/>專案主文檔] --> B[arsdoc/README.md<br/>文檔中心]

    B --> C[QUICKSTART.md<br/>快速開始]
    B --> D[QUERY_UPDATES.md<br/>查詢修改]
    B --> E[QUERIES.md<br/>查詢參考]
    B --> F[TESTING_GUIDE.md<br/>測試指南]
    B --> G[CHANGELOG.md<br/>變更日誌]

    C --> H[run_all_tests.sh]
    F --> H
    F --> I[test_single_query.py]
    F --> J[benchmark_queries.py]

    D --> K[../tests/queries.json]
    E --> K

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#e1ffe1
    style D fill:#ffe1ff
    style E fill:#fff5e1
    style F fill:#e1ffff
    style G fill:#ffe1e1
```

---

## 交叉引用索引

### QUICKSTART.md 引用

- → README.md（返回導覽）
- → TESTING_GUIDE.md（詳細測試）
- → run_all_tests.sh（執行測試）

### QUERY_UPDATES.md 引用

- → QUERIES.md（查詢參考）
- → CHANGELOG.md（變更歷史）
- → tests/queries.json（查詢定義）
- → results/*.json（示例數據）

### QUERIES.md 引用

- → QUERY_UPDATES.md（修改說明）
- → tests/queries.json（查詢定義）
- → TESTING_GUIDE.md（測試方法）

### TESTING_GUIDE.md 引用

- → QUICKSTART.md（快速方法）
- → run_all_tests.sh（測試腳本）
- → test_single_query.py（單查詢測試）
- → benchmark_queries.py（性能測試）
- → tests/test_queries.py（主測試）

### CHANGELOG.md 引用

- → QUERY_UPDATES.md（詳細變更）
- → tests/queries.json（查詢定義）

---

## 文檔使用場景對照表

| 場景 | 推薦文檔 | 推薦工具 | 預計時間 |
|-----|---------|---------|---------|
| 快速測試 | QUICKSTART.md | run_all_tests.sh | 5 分鐘 |
| 提交 PR | QUERY_UPDATES.md | run_all_tests.sh | 20 分鐘 |
| 編寫查詢 | QUERIES.md + QUERY_UPDATES.md | test_single_query.py | 30 分鐘 |
| 故障排查 | TESTING_GUIDE.md | test_single_query.py | 15 分鐘 |
| 性能優化 | TESTING_GUIDE.md | benchmark_queries.py | 20 分鐘 |
| 了解變更 | CHANGELOG.md + QUERY_UPDATES.md | - | 10 分鐘 |
| CI/CD 集成 | TESTING_GUIDE.md | run_all_tests.sh | 30 分鐘 |

---

## 文檔更新頻率

| 文檔 | 更新頻率 | 最後更新 |
|-----|---------|---------|
| README.md | 每次新增文檔 | 2026-01-07 |
| QUICKSTART.md | 每次新增測試方法 | 2026-01-07 |
| QUERY_UPDATES.md | 每次查詢修改 | 2026-01-07 |
| QUERIES.md | 每次查詢修改 | 2026-01-07 |
| TESTING_GUIDE.md | 每次新增測試方法 | 2026-01-07 |
| CHANGELOG.md | 每次重要變更 | 2026-01-07 |
| STRUCTURE.md | 每次文檔結構變更 | 2026-01-07 |

---

## 維護檢查清單

### 新增查詢時

- [ ] 更新 tests/queries.json
- [ ] 更新 QUERIES.md
- [ ] 更新 QUERY_UPDATES.md
- [ ] 更新 CHANGELOG.md
- [ ] 運行 run_all_tests.sh 驗證

### 修改查詢時

- [ ] 更新 tests/queries.json
- [ ] 記錄修改原因在 QUERY_UPDATES.md
- [ ] 更新 CHANGELOG.md
- [ ] 運行測試驗證

### 新增測試方法時

- [ ] 更新 TESTING_GUIDE.md
- [ ] 更新 QUICKSTART.md（如果是常用方法）
- [ ] 更新 README.md（如果是重要方法）
- [ ] 更新本文件的結構圖

### 重大變更時

- [ ] 更新 CHANGELOG.md
- [ ] 更新 QUERY_UPDATES.md
- [ ] 檢查所有交叉引用
- [ ] 更新版本號

---

## 快速檢索

### 想要...

- **快速測試** → QUICKSTART.md + run_all_tests.sh
- **了解變更** → CHANGELOG.md → QUERY_UPDATES.md
- **查詢參考** → QUERIES.md
- **測試方法** → TESTING_GUIDE.md
- **性能分析** → benchmark_queries.py
- **調試問題** → test_single_query.py
- **完整導覽** → README.md

### 我是...

- **新手** → 從 QUICKSTART.md 開始
- **開發者** → 從 QUERY_UPDATES.md 開始
- **測試工程師** → 從 TESTING_GUIDE.md 開始
- **項目維護者** → 從 CHANGELOG.md 開始

---

## 文檔品質指標

| 指標 | 目標 | 當前狀態 |
|-----|------|---------|
| 完整性 | 100% | ✅ 100% |
| 交叉引用 | 所有文檔互聯 | ✅ 已完成 |
| 示例代碼 | 每個方法都有示例 | ✅ 已完成 |
| 測試覆蓋 | 所有查詢可測試 | ✅ 7/7 |
| 更新日期 | 所有文檔有日期 | ✅ 已標記 |
| 版本號 | 有版本追蹤 | ✅ v1.0 |

---

**文檔結構版本：** 1.0
**最後更新：** 2026-01-07
**維護者：** Claude Code
