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
# Page Config
# ---------------------------
st.set_page_config(page_title="M&M Recruitment Dashboard", layout="wide")
st.title("🚀 Mahindra & Mahindra – Recruitment Dashboard")
st.markdown("---")

# ---------------------------
# Filters (1 row)
# ---------------------------
col_filter1, col_filter2, col_filter3 = st.columns(3)
with col_filter1:
    dept_filter = st.selectbox("Filter by Department", options=["All"] + list(df["Department"].unique()))
with col_filter2:
    status_filter = st.selectbox("Filter by Status", options=["All"] + list(df["Status"].unique()))
with col_filter3:
    rec_filter = st.selectbox("Filter by Recruiter", options=["All"] + list(df["Recruiter"].unique()))

# Apply Filters
dff = df.copy()
if dept_filter != "All":
    dff = dff[dff["Department"]==dept_filter]
if status_filter != "All":
    dff = dff[dff["Status"]==status_filter]
if rec_filter != "All":
    dff = dff[dff["Recruiter"]==rec_filter]

# ---------------------------
# KPI Cards (Big and colored)
# ---------------------------
kpi_cols = st.columns(7)

kpi_values = [
    ("Total Positions", dff['Job Req ID'].nunique(), "#FF0000"),
    ("Total Offers", dff[dff['Status']=="Offered"].shape[0], "#FF6600"),
    ("Joined", dff[dff['Status']=="Joined"].shape[0], "#009900"),
    ("Selection", dff[dff['Status']=="Selection"].shape[0], "#0066FF"),
    ("In Process", dff[dff['Status']=="In Process"].shape[0], "#FFCC00"),
    ("Reserve for IJP", dff[dff['Status']=="Reserve for IJP"].shape[0], "#9900CC"),
    ("Cancelled", dff[dff['Status']=="Cancelled"].shape[0], "#666666"),
]

for i, (title, value, color) in enumerate(kpi_values):
    kpi_cols[i].markdown(f"""
        <div style="background-color:#F5F5F5; padding:15px; border-radius:10px; text-align:center;">
            <h4 style="color:{color};">{title}</h4>
            <h2 style="color:{color};">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------
# Charts in 2x2 layout
# ---------------------------
col1, col2 = st.columns(2)

# Left Column
with col1:
    pie = px.pie(dff, names='Department', values='Job Req ID', title='Hires by Department', hole=0)
    pie.update_traces(textinfo='percent+label', marker=dict(colors=px.colors.qualitative.Pastel))
    st.plotly_chart(pie, use_container_width=True)

    bar = px.bar(dff.groupby('Status').size().reset_index(name='Count'),
                 x='Status', y='Count', title='Pipeline by Stage',
                 color='Count', color_continuous_scale='Reds')
    bar.update_layout(showlegend=False)
    st.plotly_chart(bar, use_container_width=True)

# Right Column
with col2:
    donut = px.pie(dff, names='Source', values='Job Req ID', hole=0.5, title='Source Mix')
    donut.update_traces(textinfo='percent+label', marker=dict(colors=px.colors.qualitative.Vivid))
    st.plotly_chart(donut, use_container_width=True)

    column = px.bar(dff.groupby(dff['Joining Date'].dt.strftime('%b'))['Job Req ID'].count()
                    .reset_index(name='Hires'),
                    x='Joining Date', y='Hires', title='Monthly Hiring Trend',
                    color='Hires', color_continuous_scale='Blues')
    column.update_layout(showlegend=False)
    st.plotly_chart(column, use_container_width=True)

st.markdown("---")
st.caption("Dashboard powered by Streamlit | Dummy data for demonstration")
