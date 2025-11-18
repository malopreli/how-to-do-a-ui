import streamlit as st
st.title(" welcome hacker ")

import base64

# --- Load local video and convert to base64 ---
def get_base64_video(video_path):
    with open(video_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_base64 = get_base64_video("....mp4")
