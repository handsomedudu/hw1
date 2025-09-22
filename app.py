
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# --- CRISP-DM 流程 ---

# 1. Business Understanding
st.title("HW1: 互動式簡單線性迴歸")
st.markdown("""
這是一個基於 CRISP-DM 流程建立的簡單線性迴歸模型 `y = ax + b + noise`。
您可以在左側的側邊欄調整參數，觀察資料分佈和迴歸結果的變化。
""")

# --- 側邊欄：使用者輸入參數 ---
st.sidebar.header("參數設定")
a_param = st.sidebar.slider("斜率 (a)", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
b_param = st.sidebar.slider("截距 (b)", min_value=-20.0, max_value=20.0, value=5.0, step=0.5)
noise_param = st.sidebar.slider("隨機雜訊程度 (noise)", min_value=0.0, max_value=20.0, value=2.0, step=0.5)
n_points_param = st.sidebar.slider("資料點數 (n_points)", min_value=50, max_value=1000, value=200, step=10)

# 2. Data Understanding & 3. Data Preparation
st.header("資料生成與準備")
with st.expander("點擊查看說明"):
    st.markdown("""
    - **資料生成**: 我們根據您設定的參數 `a`, `b`, `noise` 來生成模擬資料。
        - `X` 是從 0 到 10 之間的均勻分佈隨機數。
        - `Y` 的計算公式為 `Y = a*X + b + noise`，其中 `noise` 來自常態分佈。
    - **資料準備**:
        - 生成的資料會被存入 Pandas DataFrame 中方便預覽。
        - 資料集會被分割為 80% 的訓練集和 20% 的測試集。
    """)

# 生成資料
X = np.random.rand(n_points_param, 1) * 10
noise = np.random.randn(n_points_param, 1) * noise_param
y = a_param * X + b_param + noise

# 存入 DataFrame
df = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})
st.write("生成資料的前五筆:")
st.dataframe(df.head())

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
st.write(f"資料集大小: {n_points_param} 筆，訓練集: {len(X_train)} 筆，測試集: {len(X_test)} 筆。")


# 4. Modeling
st.header("模型訓練")
with st.expander("點擊查看說明"):
    st.markdown("""
    - 我們使用 `scikit-learn` 的 `LinearRegression` 模型。
    - 模型會根據提供的 **訓練集** (`X_train`, `y_train`) 學習最佳的迴歸線。
    """)

# 建立並訓練模型
model = LinearRegression()
model.fit(X_train, y_train)
st.success("模型訓練完成！")

# 5. Evaluation
st.header("模型評估")
with st.expander("點擊查看說明"):
    st.markdown("""
    - **模型參數**: 顯示模型從訓練資料中學習到的斜率 (`â`) 和截距 (`b̂`)。您可以比較這些值與您在側邊欄設定的原始參數 `a` 和 `b`。
    - **R² 分數**: R-squared (R²) 分數用來衡量模型對 **測試集** 的解釋能力，分數越接近 1 代表模型表現越好。
    """)

# 取得模型學到的參數
a_learned = model.coef_[0][0]
b_learned = model.intercept_[0]
r2_score = model.score(X_test, y_test)

col1, col2 = st.columns(2)
col1.metric("學習到的斜率 (â)", f"{a_learned:.2f}", delta=f"{a_learned - a_param:.2f}")
col2.metric("學習到的截距 (b̂)", f"{b_learned:.2f}", delta=f"{b_learned - b_param:.2f}")
st.metric("R² 分數 (在測試集上)", f"{r2_score:.3f}")


# 6. Deployment (視覺化)
st.header("結果視覺化")
with st.expander("點擊查看說明"):
    st.markdown("""
    - **藍色點**: 代表完整的原始資料點 (`X`, `y`)。
    - **紅色線**: 代表我們訓練出的線性迴歸模型所繪製的預測線。
    """)

# 繪圖
fig, ax = plt.subplots()
# 繪製原始資料點
ax.scatter(X, y, alpha=0.6, label="原始資料 (Original Data)")
# 繪製迴歸線
y_pred = model.predict(X)
ax.plot(X, y_pred, color='red', linewidth=2, label="迴歸線 (Regression Line)")

ax.set_title("線性迴歸結果")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

st.pyplot(fig)
