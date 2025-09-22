# HW1: 使用 CRISP-DM 開發簡單線性迴歸應用

---

### **[LIVE DEMO 網址](https://kurr3bugddpgugxzo2xtyn.streamlit.app/)**

---

本文檔詳細記錄了從專案啟動到最終部署的完整開發流程與思考過程，旨在完整呈現一個小型數據科學專案的生命週期。

## 1. 初始需求 (Initial Prompt)

專案的核心需求如下：

1.  **問題定義**：建立一個 Python 程式來解決簡單線性迴歸問題。
2.  **方法論**：整個開發過程需遵循 CRISP-DM 框架。
3.  **互動性**：需提供一個使用者介面，允許使用者動態調整以下參數：
    *   線性方程式 `y = ax + b` 中的斜率 `a`。
    *   隨機雜訊 `noise` 的程度。
    *   生成資料點的數量 `number of points`。
4.  **呈現方式**：需透過網頁框架（如 Streamlit 或 Flask）來呈現結果。
5.  **部署**：需提供將此應用程式部署上線的開發步驟說明。
6.  **過程記錄**：專案產出不可只有程式碼與結果，必須包含完整的開發過程描述。

---

## 2. CRISP-DM 流程詳解

以下為我們如何應用 CRISP-DM 框架的六個步驟來完成此專案。

### (1) Business Understanding (商業理解)

- **目標**：本次專案的主要目標並非解決一個真實的商業問題，而是建立一個**教育與展示工具**。
- **價值**：這個工具的價值在於讓非技術背景的使用者或初學者，能夠透過親手操作與即時反饋，直觀地理解線性迴歸的基本原理，以及參數（如斜率、雜訊）如何影響數據分佈和模型擬合的結果。

### (2) Data Understanding (資料理解)

- **資料來源**：由於專案的核心是讓使用者觀察參數變化的影響，因此我們不採用固定的真實數據集，而是選擇生成**模擬資料 (Synthetic Data)**。
- **資料特性**：我們定義了資料生成的規則，使其符合簡單線性迴歸 `y = ax + b + noise` 的形式。
    - **X (特徵)**：使用 `numpy.random.rand()` 生成一組在 [0, 10] 區間內均勻分佈的隨機數，作為自變數。
    - **Y (目標)**：根據使用者輸入的斜率 `a` 和截距 `b`，以及 `X` 值，計算出基礎的 `y`。接著，使用 `numpy.random.randn()` 生成符合常態分佈的雜訊，其標準差由使用者輸入的 `noise` 參數控制。最終的 `Y` 即為 `a*X + b + noise`。
- **結論**：這種方式讓我們可以完全控制數據的生成過程，完美符合專案的教育目的。

### (3) Data Preparation (資料準備)

- **數據生成與整理**：在使用者調整參數後，我們使用 NumPy 根據上述規則即時生成 `X` 和 `Y` 數據。為了方便後續處理與展示，我們使用 Pandas 將這些數據轉換為一個 DataFrame，並給予明確的欄位名稱 (`'X'`, `'y'`)。
- **數據分割**：為了模擬真實的機器學習流程並客觀地評估模型，我們需要將數據分為訓練集和測試集。這裡我們使用 `scikit-learn` 的 `train_test_split` 函式，按照 80/20 的比例進行分割。這確保了模型在訓練時看不到測試數據，從而使我們在測試集上的評估結果（如 R² 分數）更具參考價值。

### (4) Modeling (模型建立)

- **模型選擇**：根據問題定義（簡單線性迴歸），我們選用了 `scikit-learn` 函式庫中最直接對應的模型：`sklearn.linear_model.LinearRegression`。
- **模型訓練**：我們實例化 `LinearRegression` 模型後，調用其 `.fit()` 方法，並將前一步準備好的**訓練集** (`X_train`, `y_train`) 作為參數傳入。模型會自動學習數據中的線性關係，找到最佳的擬合直線。

### (5) Evaluation (模型評估)

為了評估模型的好壞，我們採用了量化與質化兩種方式：

- **量化評估**：
    1.  **模型參數**：我們從訓練好的模型中提取學習到的斜率 (`model.coef_`) 和截距 (`model.intercept_`)，並將其與使用者最初設定的 `a` 和 `b` 進行比較，讓使用者了解模型「還原」原始參數的能力。
    2.  **R² 分數 (決定係數)**：我們使用模型的 `.score()` 方法，在**測試集** (`X_test`, `y_test`) 上計算 R² 分數。此分數衡量了模型對數據變異性的解釋能力，越接近 1 代表擬合效果越好。
- **質化評估 (視覺化)**：
    - 我們使用 Matplotlib 繪製了一張圖表，其中包含：
        - 原始數據點的散佈圖 (Scatter Plot)。
        - 模型學習到的迴歸線 (Line Plot)。
    - 這種視覺化的方式讓使用者可以直觀地看到模型的擬合程度。

### (6) Deployment (部署)

- **框架選擇**：
    - **Streamlit vs. Flask**：雖然兩者都可以完成任務，但考量到本專案的重點是快速開發和互動式數據展示，**Streamlit** 是更優的選擇。它允許我們用純 Python 腳本快速生成帶有滑桿、按鈕等元件的網頁介面，無需編寫任何前端程式碼 (HTML/CSS/JS)，極大地簡化了開發流程。

- **部署步驟**：
    1.  **程式碼準備**：將所有應用程式邏輯寫入 `app.py` 檔案。將所有專案依賴的套件名稱寫入 `requirements.txt` 檔案，這是部署時告知雲端平台需要安裝哪些套件的依據。
    2.  **版本控制 (Git & GitHub)**：
        - 初始化 Git 儲存庫，並將 `app.py` 和 `requirements.txt` 加入版本控制。
        - 在 GitHub 上建立一個新的儲存庫 (`hw1`)。
        - 將本地儲存庫與遠端的 GitHub 儲存庫連結，並使用 `git push` 將程式碼上傳。此過程需要使用 Personal Access Token (PAT) 進行身份驗證。
    3.  **雲端部署 (Streamlit Community Cloud)**：
        - 登入 Streamlit Community Cloud 帳戶 (使用 GitHub 帳號授權)。
        - 點擊 "New app"，並選擇剛剛上傳程式碼的 GitHub 儲存庫 (`handsomedudu/hw1`)。
        - 指定分支為 `master`，主檔案為 `app.py`。
        - 點擊 "Deploy!"，平台會自動根據 `requirements.txt` 安裝環境並啟動應用程式，幾分鐘後即可獲得公開的網站連結。

---

## 3. 最終產出 (Final Deliverables)

- **Live Demo**：[https://kurr3bugddpgugxzo2xtyn.streamlit.app/](https://kurr3bugddpgugxzo2xtyn.streamlit.app/)
- **核心檔案**：
    - `app.py`: Streamlit 應用程式的完整原始碼。
    - `requirements.txt`: 專案依賴套件列表。
    - `README.md`: 本文件，包含開發流程與使用指南。
- **GitHub 儲存庫**：[https://github.com/handsomedudu/hw1](https://github.com/handsomedudu/hw1)