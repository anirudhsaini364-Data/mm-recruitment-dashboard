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

# ----------------------
# Custom CSS for Mahindra Theme
# ----------------------
st.markdown("""
    <style>
        body { background-color: #fafafa; }
        .header {
            background-color: #E31837;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            color: white;
            font-size: 28px;
            font-weight: bold;
        }
        .card {
            padding: 12px;
            border-radius: 10px;
            background: white;
            text-align: center;
            box-shadow: 0px 2px 6px #ddd;
            margin: 4px;
        }
        .metric-label { font-size:14px; font-weight:600; color:#444; }
        .metric-value { font-size:20px; font-weight:bold; }
        .block-container { padding-top:1rem; padding-bottom:0rem; }
    </style>
""", unsafe_allow_html=True)

# ----------------------
# Header
# ----------------------
st.markdown("<div class='header'>🚀 Mahindra & Mahindra – Recruitment Dashboard</div>", unsafe_allow_html=True)

# ----------------------
# Filters
# ----------------------
col1, col2, col3 = st.columns([1,1,1])
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
        st.markdown(f"<div class='card'><div class='metric-label'>{label}</div>"
                    f"<div class='metric-value' style='color:{color}'>{value}</div></div>", unsafe_allow_html=True)

# ----------------------
# Charts Row 1 (Pie + Donut + Funnel)
# ----------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Hires by Department")
    dept_chart = filtered_df["Department"].value_counts().reset_index()
    dept_chart.columns = ["Department", "Count"]
    fig1 = px.pie(dept_chart, names="Department", values="Count", hole=0, height=250, color_discrete_sequence=px.colors.sequential.Reds)
    fig1.update_traces(textinfo="percent+label")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🍩 Source Mix")
    source_chart = filtered_df["Status"].value_counts().reset_index()
    source_chart.columns = ["Status", "Count"]
    fig2 = px.pie(source_chart, names="Status", values="Count", hole=0.5, height=250, color_discrete_sequence=px.colors.qualitative.Set2)
    fig2.update_traces(textinfo="percent+label")
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    st.subheader("🔻 Recruitment Funnel")
    funnel_data = filtered_df["Status"].value_counts().reset_index()
    funnel_data.columns = ["Stage", "Count"]
    fig5 = px.funnel(funnel_data, x="Count", y="Stage", height=250, color="Stage", color_discrete_sequence=px.colors.sequential.Reds)
    st.plotly_chart(fig5, use_container_width=True)

# ----------------------
# Charts Row 2 (Bar + Column)
# ----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Hires by Month")
    month_chart = filtered_df["Month"].value_counts().reset_index()
    month_chart.columns = ["Month", "Count"]
    fig3 = px.bar(month_chart, x="Month", y="Count", text="Count", color="Month", height=250, color_discrete_sequence=px.colors.sequential.Reds)
    fig3.update_traces(textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("👤 Hires by Recruiter")
    rec_chart = filtered_df["Recruiter"].value_counts().reset_index()
    rec_chart.columns = ["Recruiter", "Count"]
    fig4 = px.bar(rec_chart, x="Recruiter", y="Count", text="Count", color="Recruiter", height=250, color_discrete_sequence=px.colors.qualitative.Set2)
    fig4.update_traces(textposition="outside")
    st.plotly_chart(fig4, use_container_width=True)
