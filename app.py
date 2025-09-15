import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Recruitment Dashboard", layout="wide")

# Dummy Data
data = {
    "Stage": ["Screening", "Interview", "Offer", "Joining"],
    "Count": [120, 85, 40, 25]
}
df = pd.DataFrame(data)

# Custom CSS (exact same style as screenshot, just reduced height)
st.markdown("""
    <style>
        .metric-card {
            border-radius: 12px;
            padding: 12px 10px;  /* reduced padding */
            height: 90px;        /* reduced height */
            color: white;
            text-align: center;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.2);
        }
        .metric-value {
            font-size: 22px;     /* reduced font size slightly */
            font-weight: bold;
            margin-bottom: -5px;
        }
        .metric-label {
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2 style='text-align: center; color:#2C3E50;'>📊 Recruitment Dashboard</h2>", unsafe_allow_html=True)

# Top Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='metric-card' style='background-color:#3498DB;'><div class='metric-value'>120</div><div class='metric-label'>Screening</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card' style='background-color:#E67E22;'><div class='metric-value'>85</div><div class='metric-label'>Interview</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card' style='background-color:#9B59B6;'><div class='metric-value'>40</div><div class='metric-label'>Offer</div></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='metric-card' style='background-color:#27AE60;'><div class='metric-value'>25</div><div class='metric-label'>Joining</div></div>", unsafe_allow_html=True)

st.markdown("---")

# Charts
col5, col6 = st.columns(2)

with col5:
    fig1 = px.bar(df, x="Stage", y="Count", color="Stage", title="Candidates by Stage")
    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.pie(df, names="Stage", values="Count", title="Stage Distribution")
    st.plotly_chart(fig2, use_container_width=True)
