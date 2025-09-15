import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------
# Dummy Data
# ---------------------------
data = {
    "Job Req ID": range(101, 121),
    "Department": ["Sales","Marketing","Operations","HR","IT"]*4,
    "Status": ["Joined","Offered","Selection","In Process","Reserve for IJP","Cancelled","Joined","Offered","In Process","Cancelled"]*2,
    "Source": ["Referral","Job Portal","Consultant","Direct","Referral"]*4,
    "Recruiter": ["John","Alice","Rahul","Priya","Ankit"]*4,
    "Offer Date": pd.date_range(start="2025-06-01", periods=20, freq="3D"),
    "Joining Date": pd.date_range(start="2025-06-05", periods=20, freq="3D")
}
df = pd.DataFrame(data)

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="M&M Recruitment Dashboard", layout="wide")

st.title("Mahindra & Mahindra – Recruitment Dashboard")

# ---------------------------
# Filters
# ---------------------------
dept_filter = st.selectbox("Filter by Department", options=["All"]+list(df["Department"].unique()))
status_filter = st.selectbox("Filter by Status", options=["All"]+list(df["Status"].unique()))
rec_filter = st.selectbox("Filter by Recruiter", options=["All"]+list(df["Recruiter"].unique()))

# Apply Filters
dff = df.copy()
if dept_filter != "All":
    dff = dff[dff["Department"]==dept_filter]
if status_filter != "All":
    dff = dff[dff["Status"]==status_filter]
if rec_filter != "All":
    dff = dff[dff["Recruiter"]==rec_filter]

# ---------------------------
# KPI Cards
# ---------------------------
kpi1 = dff['Job Req ID'].nunique()
kpi2 = dff[dff['Status']=="Offered"].shape[0]
kpi3 = dff[dff['Status']=="Joined"].shape[0]
kpi4 = dff[dff['Status']=="Selection"].shape[0]
kpi5 = dff[dff['Status']=="In Process"].shape[0]
kpi6 = dff[dff['Status']=="Reserve for IJP"].shape[0]
kpi7 = dff[dff['Status']=="Cancelled"].shape[0]

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
col1.metric("Total Positions", kpi1)
col2.metric("Total Offers", kpi2)
col3.metric("Joined", kpi3)
col4.metric("Selection", kpi4)
col5.metric("In Process", kpi5)
col6.metric("Reserve for IJP", kpi6)
col7.metric("Cancelled", kpi7)

# ---------------------------
# Charts
# ---------------------------
pie = px.pie(dff, names='Department', values='Job Req ID', title='Hires by Department')
donut = px.pie(dff, names='Source', values='Job Req ID', hole=0.5, title='Source Mix')
bar = px.bar(dff.groupby('Status').size().reset_index(name='Count'), x='Status', y='Count',
             title='Pipeline by Stage', color='Count', color_continuous_scale='Reds')
column = px.bar(dff.groupby(dff['Joining Date'].dt.strftime('%b'))['Job Req ID'].count().reset_index(name='Hires'),
                x='Joining Date', y='Hires', title='Monthly Hiring Trend', color='Hires', color_continuous_scale='Blues')

st.plotly_chart(pie, use_container_width=True)
st.plotly_chart(donut, use_container_width=True)
st.plotly_chart(bar, use_container_width=True)
st.plotly_chart(column, use_container_width=True)
