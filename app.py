import streamlit as st
st.title(" welcome hacker ")

import base64

# --- Load local video and convert to base64 ---
def get_base64_video(video_path):
    with open(video_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_base64 = get_base64_video("1032549521-preview.mp4")

background_video_html = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: transparent;
}}
video.bg-video {{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    object-fit: cover;
}}
</style>

<video autoplay loop muted playsinline class="bg-video">
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
"""

st.markdown(background_video_html, unsafe_allow_html=True)

# --- Your Streamlit UI ---
st.title("My App with Video Background")
st.write("Your content goes on top of the video 🌟")
