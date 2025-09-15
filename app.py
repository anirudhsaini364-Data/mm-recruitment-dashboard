import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# Dummy Data
# ----------------------
data = {
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "IT", "Finance", "HR", "IT"],
    "Recruiter": ["A", "B", "C", "A", "B", "C", "D", "E", "F", "A"],
    "Status": [
        "Joined", "Offer", "In Process", "Cancelled", "Joined",
        "Selection", "Offer", "Reserve for IJP", "Joined", "Cancelled"
    ],
    "Month": ["Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Apr", "Apr", "Apr", "Apr"]
}
df = pd.DataFrame(data)

# ----------------------
# Page Config
# ----------------------
st.set_page_config(page_title="M&M Recruitment Dashboard", layout="wide")

# Custom CSS for Mahindra theme
st.markdown("""
    <style>
        body { background-color: #f5f5f5; }
        .big-font { font-size:30px !important; font-weight:bold; color:#E31837; }
        .card { padding:20px; border-radius:15px; background:white; text-align:center; box-shadow:2px 2px 10px #ccc; }
        .metric-label { font-size:18px; font-weight:bold; }
        .metric-value { font-size:26px; font-weight:bold; }
    </style>
""", unsafe_allow_html=True)

# ----------------------
# Title
# ----------------------
st.markdown("<h1 style='text-align: center; color:#E31837;'>🚀 Mahindra & Mahindra – Recruitment Dashboard</h1>", unsafe_allow_html=True)

# ----------------------
# Filters
# ----------------------
col1, col2, col3 = st.columns(3)
with col1:
    dept_filter = st.selectbox("Filter by Department", ["All"] + df["Department"].unique().tolist())
with col2:
    status_filter = st.selectbox("Filter by Status", ["All"] + df["Status"].unique().tolist())
with col3:
    recruiter_filter = st.selectbox("Filter by Recruiter", ["All"] + df["Recruiter"].unique().tolist())

filtered_df = df.copy()
if dept_filter != "All":
    filtered_df = filtered_df[filtered_df["Department"] == dept_filter]
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["Status"] == status_filter]
if recruiter_filter != "All":
    filtered_df = filtered_df[filtered_df["Recruiter"] == recruiter_filter]

# ----------------------
# KPI Cards
# ----------------------
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

kpis = {
    "Total Positions": len(filtered_df),
    "Total Offers": (filtered_df["Status"] == "Offer").sum(),
    "Joined": (filtered_df["Status"] == "Joined").sum(),
    "Selection": (filtered_df["Status"] == "Selection").sum(),
    "In Process": (filtered_df["Status"] == "In Process").sum(),
    "Reserve for IJP": (filtered_df["Status"] == "Reserve for IJP").sum(),
    "Cancelled": (filtered_df["Status"] == "Cancelled").sum(),
}

colors = ["#E31837", "orange", "green", "blue", "gold", "purple", "grey"]
for col, (label, value), color in zip([col1, col2, col3, col4, col5, col6, col7], kpis.items(), colors):
    with col:
        st.markdown(f"<div class='card'><div class='metric-label' style='color:{color}'>{label}</div>"
                    f"<div class='metric-value' style='color:{color}'>{value}</div></div>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------
# Row 1: Pie + Donut
# ----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Hires by Department")
    dept_chart = filtered_df["Department"].value_counts().reset_index()
    dept_chart.columns = ["Department", "Count"]
    fig1 = px.pie(dept_chart, names="Department", values="Count", hole=0)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🍩 Source Mix")
    source_chart = filtered_df["Status"].value_counts().reset_index()
    source_chart.columns = ["Status", "Count"]
    fig2 = px.pie(source_chart, names="Status", values="Count", hole=0.5)
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------
# Row 2: Column + Bar
# ----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Hires by Month")
    month_chart = filtered_df["Month"].value_counts().reset_index()
    month_chart.columns = ["Month", "Count"]
    fig3 = px.bar(month_chart, x="Month", y="Count", text="Count", color="Month")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("👤 Hires by Recruiter")
    rec_chart = filtered_df["Recruiter"].value_counts().reset_index()
    rec_chart.columns = ["Recruiter", "Count"]
    fig4 = px.bar(rec_chart, x="Recruiter", y="Count", text="Count", color="Recruiter", orientation="v")
    st.plotly_chart(fig4, use_container_width=True)

# ----------------------
# Funnel Chart
# ----------------------
st.subheader("🔻 Recruitment Funnel")
funnel_data = filtered_df["Status"].value_counts().reset_index()
funnel_data.columns = ["Stage", "Count"]
fig5 = px.funnel(funnel_data, x="Count", y="Stage")
st.plotly_chart(fig5, use_container_width=True)
