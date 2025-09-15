import streamlit as st
import pandas as pd
import plotly.express as px

# ========================
# Dummy Data
# ========================
data = {
    "Candidate": ["A", "B", "C", "D", "E", "F"],
    "Status": ["Hired", "Interview", "Rejected", "Hired", "Interview", "Rejected"],
    "Source": ["LinkedIn", "Naukri", "Referral", "LinkedIn", "Naukri", "Referral"],
    "Function": ["Tech", "HR", "Tech", "Finance", "HR", "Tech"],
    "DOJ": pd.date_range("2025-01-01", periods=6, freq="15D"),
}
df = pd.DataFrame(data)

st.set_page_config(page_title="Recruitment Dashboard", layout="wide")

# ========================
# Title
# ========================
st.markdown("### 📊 Recruitment Dashboard (Compact View)")

# ========================
# Filters
# ========================
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.multiselect("Filter by Status", df["Status"].unique(), default=df["Status"].unique())
    with col2:
        source_filter = st.multiselect("Filter by Source", df["Source"].unique(), default=df["Source"].unique())
    with col3:
        function_filter = st.multiselect("Filter by Function", df["Function"].unique(), default=df["Function"].unique())

df_filtered = df[
    (df["Status"].isin(status_filter)) &
    (df["Source"].isin(source_filter)) &
    (df["Function"].isin(function_filter))
]

# ========================
# Charts Compact Layout
# ========================
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        fig1 = px.bar(df_filtered, x="Source", color="Status", title="Source vs Status", barmode="group")
        st.plotly_chart(fig1, use_container_width=True, height=300)

    with col2:
        fig2 = px.pie(df_filtered, names="Status", title="Status Distribution")
        st.plotly_chart(fig2, use_container_width=True, height=300)

    with col3:
        fig3 = px.bar(df_filtered, x="Function", color="Status", title="Function vs Status", barmode="group")
        st.plotly_chart(fig3, use_container_width=True, height=300)

# ========================
# Table (Compact)
# ========================
with st.container():
    st.markdown("#### 📋 Candidate Data")
    st.dataframe(df_filtered, use_container_width=True, height=220)
