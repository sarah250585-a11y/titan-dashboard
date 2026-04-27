import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="TITAN LOGIC SYSTEMS", layout="wide", page_icon="🤖")

# 2. TITAN BRANDING (ELECTRIC BLUE & DARK MODE)
st.markdown("""
    <style>
    .stApp { background-color: #00050a; }
    h1, h2, h3, p, label { color: #00f2ff !important; text-shadow: 0px 0px 10px #00f2ff; }
    .stTextInput>div>div>input { background-color: #001a33; color: white; border: 1px solid #00f2ff; }
    .stTextArea>div>div>textarea { background-color: #001a33; color: white; border: 1px solid #00f2ff; }
    [data-testid="stSidebar"] { background-color: #000a14 !important; border-right: 2px solid #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR STATUS
st.sidebar.title("SYSTEM STATUS")
st.sidebar.success("CORE: ACTIVE")
st.sidebar.info("MODE: STRATEGIC OUTREACH")
st.sidebar.write("---")
st.sidebar.write("User: Guest (Unauthorized)")

# 4. MAIN INTERFACE
st.title("TITAN LOGIC SYSTEMS")
st.subheader("STRATEGIC COMMAND INTERFACE")

# 5. PRECISION GEO-INTEL (NOTTINGHAM MAP)
st.write("### 🌐 PRECISION GEO-INTEL")
# Map centered on Nottingham
m = folium.Map(location=[52.9548, -1.1581], zoom_start=12, tiles="CartoDB dark_matter")
folium.Marker(
    [52.9548, -1.1581], 
    popup="TITAN HQ - NOTTINGHAM", 
    icon=folium.Icon(color='blue', icon='screenshot')
).add_to(m)
st_folium(m, width="100%", height=500)

# 6. TACTICAL AI COMMAND (CHATTING)
st.write("---")
st.subheader("🤖 TACTICAL AI COMMAND")
st.write("Enter commands to interface with Titan AI Intel.")
user_query = st.text_input("COMMAND INPUT:", placeholder="Type 'status', 'marketing', or a question...")

if user_query:
    query = user_query.lower()
    if "status" in query:
        st.info("TITAN AI: All systems nominal. Satellite links stable. Local grid online.")
    elif "marketing" in query:
        st.info("TITAN AI: Analyzing Nottingham sector... High engagement detected in city center. Recommend localized outreach.")
    elif "mission" in query:
        st.info("TITAN AI: Our mission is total market dominance through strategic data visualization.")
    else:
        st.info(f"TITAN AI: Processing '{user_query}'... Access restricted. Upgrade to Premium for full reasoning capabilities.")

# 7. FEEDBACK & REVIEWS (FOR YOUR MATE)
st.write("---")
st.subheader("📊 TACTICAL FEEDBACK & REVIEWS")
st.write("Leave your marketing intel or system feedback below.")

with st.form("review_form"):
    col1, col2 = st.columns(2)
    with col1:
        reviewer_name = st.text_input("Name / Callsign:")
    with col2:
        rating = st.selectbox("Rating:", ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"])
    
    review_text = st.text_area("Intel Message:")
    submit_button = st.form_submit_button("SUBMIT INTEL")
    
    if submit_button:
        st.success(f"Intel Logged! Thank you, {reviewer_name}. Your review of '{review_text}' has been saved.")

st.markdown("---")
st.caption("© 2024 TITAN LOGIC SYSTEMS | SECURE ENCRYPTED CONNECTION")
