import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="TITAN LOGIC SYSTEMS", layout="wide")

# TITAN LOGIC BRANDING (ELECTRIC BLUE & DARK MODE)
st.markdown("""
    <style>
    .stApp { background-color: #00050a; }
    h1, h2, h3, p, label { color: #00f2ff !important; text-shadow: 0px 0px 10px #00f2ff; }
    [data-testid="stSidebar"] { background-color: #000a14 !important; border-right: 2px solid #00f2ff; }
    .stTextInput>div>div>input { background-color: #001a33; color: white; border: 1px solid #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("TITAN LOGIC SYSTEMS")
st.subheader("STRATEGIC COMMAND INTERFACE")

# MAP SECTION
st.write("### 🌍 PRECISION GEO-INTEL")
m = folium.Map(location=[52.9548, -1.1581], zoom_start=12)
st_folium(m, width="100%", height=400)

# CHAT SECTION
st.write("### 🛰️ NEURAL COMMAND")
user_input = st.text_input("Enter Command...")
if user_input:
    st.write(f"Titan Logic processing: {user_input}")

# FOOTER JOIN
st.markdown("---")
st.write("© 2026 TITAN LOGIC SYSTEMS | SECURE OPERATIONS")
