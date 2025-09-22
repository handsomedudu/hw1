# HW1: 簡單線性迴歸 Streamlit 應用

這是一個使用 Streamlit 建立的互動式簡單線性迴歸應用程式。使用者可以透過網頁介面調整參數，觀察線性迴歸模型的結果變化。

專案遵循 CRISP-DM 流程進行開發。

## 技術棧

- Python
- Streamlit
- Scikit-learn
- Pandas
- Numpy
- Matplotlib

---

## 開發與運行步驟

### 1. 環境準備

- 確認您的電腦已安裝 Python (建議透過 Anaconda 安裝)。
- 已安裝 Git 版本控制工具。

### 2. 複製專案

在您的終端機中，執行以下指令來複製此儲存庫：

```bash
git clone https://github.com/handsomedudu/hw1.git
cd hw1
```

### 3. 安裝相依套件

在 `hw1` 資料夾中，執行以下指令來安裝所有必要的 Python 套件：

```bash
pip install -r requirements.txt
```

### 4. 運行應用程式

執行以下指令來啟動 Streamlit 應用程式：

```bash
streamlit run app.py
```

執行後，您的瀏覽器會自動打開一個本地網址 (通常是 `http://localhost:8501`)，您就可以看到並操作這個應用程式了。

---

## 部署到 Streamlit Community Cloud

您可以將這個專案免費部署成一個公開的網站。

1.  **註冊/登入 Streamlit Community Cloud**
    - 前往 [https://share.streamlit.io/signup](https://share.streamlit.io/signup)
    - 建議直接使用您的 GitHub 帳號進行授權登入。

2.  **部署應用程式**
    - 登入後，點擊畫面右上角的「**New app**」按鈕。
    - 在部署頁面中，填寫以下資訊：
        - **Repository**: 選擇 `handsomedudu/hw1` 儲存庫。
        - **Branch**: 輸入 `master`。
        - **Main file path**: 輸入 `app.py`。
    - 點擊「**Deploy!**」按鈕。

3.  **等待部署完成**
    - Streamlit 會開始建置您的應用程式，幾分鐘後即可透過專屬網址瀏覽。
