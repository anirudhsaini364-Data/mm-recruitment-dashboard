import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# Dummy Recruitment Data
# --------------------------
data = {
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Status": ["Joined", "Offer", "Cancelled", "In Process", "Selection", "Reserve for IJP", "Joined", "Offer", "Cancelled", "Joined"],
    "Recruiter": ["R1", "R2", "R1", "R3", "R2", "R1", "R3", "R2", "R1", "R3"],
    "Month": ["Jan", "Feb", "Mar", "Mar", "Apr", "Apr", "Apr", "Feb", "Jan", "Apr"]
}
df = pd.DataFrame(data)

# --------------------------
# Dashboard Header
# --------------------------
st.markdown("""
    <div style="
        background-color:#d32f2f;
        padding:15px;
        border-radius:8px;
        text-align:center;
        width:100%;
        box-shadow:0 4px 8px rgba(0,0,0,0.2);
    ">
        <h2 style="color:white; font-size:28px; margin:0;">
            🚀 Mahindra & Mahindra – Recruitment Dashboard
        </h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------
# Filters
# --------------------------
col1, col2, col3 = st.columns(3)
with col1:
    dept_filter = st.selectbox("Filter by Department", options=["All"] + df["Department"].unique().tolist())
with col2:
    status_filter = st.selectbox("Filter by Status", options=["All"] + df["Status"].unique().tolist())
with col3:
    recruiter_filter = st.selectbox("Filter by Recruiter", options=["All"] + df["Recruiter"].unique().tolist())

# Apply Filters
filtered_df = df.copy()
if dept_filter != "All":
    filtered_df = filtered_df[filtered_df["Department"] == dept_filter]
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["Status"] == status_filter]
if recruiter_filter != "All":
    filtered_df = filtered_df[filtered_df["Recruiter"] == recruiter_filter]

# --------------------------
# KPI Cards with Stylish Boxes
# --------------------------
def kpi_card(title, value, color):
    return f"""
    <div style="
        background-color:white;
        padding:15px;
        border-radius:12px;
        text-align:center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin:5px;
    ">
        <h4 style="margin:0; font-size:16px; color:#333;">{title}</h4>
        <h2 style="margin:0; color:{color}; font-size:26px;">{value}</h2>
    </div>
    """

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6, kpi7 = st.columns(7)

with kpi1:
    st.markdown(kpi_card("Total Positions", len(filtered_df), "#e53935"), unsafe_allow_html=True)
with kpi2:
    st.markdown(kpi_card("Total Offers", (filtered_df["Status"]=="Offer").sum(), "#ff9800"), unsafe_allow_html=True)
with kpi3:
    st.markdown(kpi_card("Joined", (filtered_df["Status"]=="Joined").sum(), "#4caf50"), unsafe_allow_html=True)
with kpi4:
    st.markdown(kpi_card("Selection", (filtered_df["Status"]=="Selection").sum(), "#1e88e5"), unsafe_allow_html=True)
with kpi5:
    st.markdown(kpi_card("In Process", (filtered_df["Status"]=="In Process").sum(), "#fbc02d"), unsafe_allow_html=True)
with kpi6:
    st.markdown(kpi_card("Reserve for IJP", (filtered_df["Status"]=="Reserve for IJP").sum(), "#8e24aa"), unsafe_allow_html=True)
with kpi7:
    st.markdown(kpi_card("Cancelled", (filtered_df["Status"]=="Cancelled").sum(), "#6d4c41"), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------
# Charts Row 1
# --------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("📊 **Hires by Department**")
    dept_counts = filtered_df["Department"].value_counts().reset_index()
    dept_counts.columns = ["Department", "Count"]
    fig = px.pie(dept_counts, names="Department", values="Count", color="Department")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("🍩 **Source Mix**")
    status_counts = filtered_df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig = px.pie(status_counts, names="Status", values="Count", hole=0.4, color="Status")
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.markdown("🔻 **Recruitment Funnel**")
    funnel = filtered_df["Status"].value_counts().reset_index()
    funnel.columns = ["Stage", "Count"]
    fig = px.funnel(funnel, x="Count", y="Stage", color="Stage")
    st.plotly_chart(fig, use_container_width=True)

# --------------------------
# Charts Row 2
# --------------------------
c4, c5 = st.columns(2)

with c4:
    st.markdown("📈 **Hires by Month**")
    month_counts = filtered_df["Month"].value_counts().reset_index()
    month_counts.columns = ["Month", "Count"]
    fig = px.bar(month_counts, x="Month", y="Count", color="Month", text="Count")
    st.plotly_chart(fig, use_container_width=True)

with c5:
    st.markdown("🧑‍💼 **Hires by Recruiter**")
    recruiter_counts = filtered_df["Recruiter"].value_counts().reset_index()
    recruiter_counts.columns = ["Recruiter", "Count"]
    fig = px.bar(recruiter_counts, x="Recruiter", y="Count", color="Recruiter", text="Count")
    st.plotly_chart(fig, use_container_width=True)
