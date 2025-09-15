import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# Dummy Data
# ----------------------
data = {
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Recruiter": ["A", "B", "C", "A", "B", "C", "D", "E", "F", "A"],
    "Status": [
        "Joined", "Offer", "In Process", "Cancelled", "Joined",
        "Selection", "Offer", "Reserve for IJP", "Joined", "Cancelled"
    ]
}
df = pd.DataFrame(data)

# ----------------------
# Page Config
# ----------------------
st.set_page_config(page_title="Recruitment Dashboard", layout="wide")

# ----------------------
# Title
# ----------------------
st.markdown("<h1 style='text-align: center;'>🚀 Mahindra & Mahindra – Recruitment Dashboard</h1>", unsafe_allow_html=True)

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

# Apply Filters
filtered_df = df.copy()
if dept_filter != "All":
    filtered_df = filtered_df[filtered_df["Department"] == dept_filter]
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["Status"] == status_filter]
if recruiter_filter != "All":
    filtered_df = filtered_df[filtered_df["Recruiter"] == recruiter_filter]

# ----------------------
# KPIs in One Row
# ----------------------
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

total_positions = len(filtered_df)
total_offers = (filtered_df["Status"] == "Offer").sum()
joined = (filtered_df["Status"] == "Joined").sum()
selection = (filtered_df["Status"] == "Selection").sum()
in_process = (filtered_df["Status"] == "In Process").sum()
reserve = (filtered_df["Status"] == "Reserve for IJP").sum()
cancelled = (filtered_df["Status"] == "Cancelled").sum()

with col1:
    st.markdown(f"<h4 style='color:red;'>Total Positions</h4><h2 style='color:red;'>{total_positions}</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h4 style='color:orange;'>Total Offers</h4><h2 style='color:orange;'>{total_offers}</h2>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<h4 style='color:green;'>Joined</h4><h2 style='color:green;'>{joined}</h2>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<h4 style='color:blue;'>Selection</h4><h2 style='color:blue;'>{selection}</h2>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<h4 style='color:gold;'>In Process</h4><h2 style='color:gold;'>{in_process}</h2>", unsafe_allow_html=True)
with col6:
    st.markdown(f"<h4 style='color:purple;'>Reserve for IJP</h4><h2 style='color:purple;'>{reserve}</h2>", unsafe_allow_html=True)
with col7:
    st.markdown(f"<h4 style='color:grey;'>Cancelled</h4><h2 style='color:grey;'>{cancelled}</h2>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------
# Charts in Two Columns
# ----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Hires by Department")
    dept_chart = filtered_df["Department"].value_counts().reset_index()
    dept_chart.columns = ["Department", "Count"]
    fig1 = px.pie(dept_chart, names="Department", values="Count")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Source Mix")
    source_chart = filtered_df["Status"].value_counts().reset_index()
    source_chart.columns = ["Status", "Count"]
    fig2 = px.pie(source_chart, names="Status", values="Count")
    st.plotly_chart(fig2, use_container_width=True)
