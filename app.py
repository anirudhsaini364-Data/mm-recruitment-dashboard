import streamlit as st
import plotly.express as px
import pandas as pd

# --- Page config ---
st.set_page_config(page_title="M&M Recruitment Dashboard", layout="wide")

# --- Fix header cut issue with CSS ONLY ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem !important; /* reduce top padding */
        }
    </style>
""", unsafe_allow_html=True)

# --- Dummy Data ---
data = {
    "Stage": ["Sourcing", "Screening", "Interview", "Offer", "Hired"],
    "Count": [120, 85, 50, 25, 15],
    "Source": ["Referral", "Job Portal", "LinkedIn", "Internal", "Others"],
    "SourceCount": [40, 60, 30, 20, 10]
}
df_stage = pd.DataFrame({"Stage": data["Stage"], "Count": data["Count"]})
df_source = pd.DataFrame({"Source": data["Source"], "Count": data["SourceCount"]})

# --- Header ---
st.markdown("<h1 style='color:#c8102e; text-align:center;'>🚀 Mahindra & Mahindra Recruitment Dashboard</h1>", unsafe_allow_html=True)

# --- Metrics Row ---
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.metric("Total Applications", 120)
with col2: st.metric("Screened", 85)
with col3: st.metric("Interviews", 50)
with col4: st.metric("Offers", 25)
with col5: st.metric("Hired", 15)

# --- Charts Row 1 ---
col1, col2, col3 = st.columns(3)
with col1:
    fig1 = px.pie(df_source, names="Source", values="Count", hole=0.3, title="Source Mix")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    fig2 = px.bar(df_stage, x="Stage", y="Count", text="Count", title="Stage-wise Count", color="Stage")
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    fig3 = px.funnel(df_stage, x="Count", y="Stage", title="Hiring Funnel")
    st.plotly_chart(fig3, use_container_width=True)

# --- Charts Row 2 ---
col1, col2, col3 = st.columns(3)
with col1:
    fig4 = px.pie(df_source, names="Source", values="Count", hole=0.6, title="Donut Chart View")
    st.plotly_chart(fig4, use_container_width=True)
with col2:
    fig5 = px.histogram(df_stage, x="Stage", y="Count", color="Stage", title="Stage Distribution")
    st.plotly_chart(fig5, use_container_width=True)
with col3:
    fig6 = px.line(df_stage, x="Stage", y="Count", markers=True, title="Trend Analysis")
    st.plotly_chart(fig6, use_container_width=True)
