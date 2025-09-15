import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Recruitment Dashboard", layout="wide")

# Sample Data
data = {
    "Stage": ["Screening", "Interview", "Offer", "Joining"],
    "Count": [120, 85, 40, 25]
}
df = pd.DataFrame(data)

# CSS for compact cards
st.markdown("""
    <style>
        .card {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
            text-align: center;
            height: 100px; /* reduced height */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .card h3 {
            margin: 0;
            font-size: 22px;
            color: #333333;
        }
        .card p {
            margin: 0;
            font-size: 18px;
            color: #666666;
        }
    </style>
""", unsafe_allow_html=True)

# Dashboard Title
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>📊 Recruitment Dashboard</h2>", unsafe_allow_html=True)

# Metric Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'><h3>Screening</h3><p>120</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><h3>Interview</h3><p>85</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'><h3>Offer</h3><p>40</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='card'><h3>Joining</h3><p>25</p></div>", unsafe_allow_html=True)

st.markdown("---")

# Charts Section
col5, col6 = st.columns(2)

with col5:
    fig1 = px.bar(df, x="Stage", y="Count", color="Stage", title="Candidates by Stage")
    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.pie(df, names="Stage", values="Count", title="Stage Distribution")
    st.plotly_chart(fig2, use_container_width=True)
