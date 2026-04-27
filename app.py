import streamlit as st
import folium
from streamlit_folium import st_folium
from gtts import gTTS
import os

# 1. PAGE CONFIG
st.set_page_config(page_title="TITAN LOGIC SYSTEMS", layout="wide", page_icon="🤖")

# 2. BRANDING (BRIGHTER & SHARP)
st.markdown("""
    <style>
    .stApp { background-color: #050a14; }
    h1, h2, h3, p, label { color: #00f2ff !important; text-shadow: 0px 0px 5px #00f2ff; }
    .stTextInput>div>div>input { background-color: #001a33; color: white; border: 1px solid #00f2ff; }
    [data-testid="stSidebar"] { background-color: #0a1428 !important; border-right: 2px solid #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
st.sidebar.title("SYSTEM STATUS")
st.sidebar.success("CORE: ACTIVE")
st.sidebar.info("MODE: STRATEGIC OUTREACH")
st.sidebar.write("User: Guest (Unauthorized)")

# 4. MAIN INTERFACE
st.title("TITAN LOGIC SYSTEMS")
st.subheader("STRATEGIC COMMAND INTERFACE")

# 5. BRIGHTER PRECISION MAP (Changed to 'OpenStreetMap' for visibility)
st.write("### 🌐 PRECISION GEO-INTEL (NOTTINGHAM)")
m = folium.Map(location=[52.9548, -1.1581], zoom_start=12) # Brighter map
folium.Marker([52.9548, -1.1581], popup="TITAN HQ", icon=folium.Icon(color='blue')).add_to(m)
st_folium(m, width="100%", height=500)

# 6. TACTICAL AI COMMAND WITH VOICE
st.write("---")
st.subheader("🤖 TACTICAL AI COMMAND (VOICE ENABLED)")
user_query = st.text_input("COMMAND INPUT:", placeholder="Type 'status' or ask a question...")

if user_query:
    query = user_query.lower()
    # Simple Logic
    if "status" in query:
        response = "All systems nominal. Satellite links stable. Local Nottingham grid is currently online."
    elif "marketing" in query:
        response = "Analyzing Nottingham sector. High engagement detected. Recommend immediate tactical outreach."
    else:
        response = f"Titan AI has processed your request regarding {user_query}. Data analysis is complete."

    st.info(f"TITAN AI: {response}")

    # VOICE GENERATION
    tts = gTTS(text=response, lang='en', tld='co.uk') # British accent
    tts.save("response.mp3")
    st.audio("response.mp3", format="audio/mp3", autoplay=True) # Plays automatically

# 7. FEEDBACK SECTION
st.write("---")
st.subheader("📊 TACTICAL FEEDBACK")
with st.form("review_form"):
    name = st.text_input("Name:")
    msg = st.text_area("Intel Message:")
    if st.form_submit_button("SUBMIT"):
        st.success(f"Intel Logged, {name}!")
