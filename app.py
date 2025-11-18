import streamlit as st
st.title(" welcome hacker ")

import base64

# --- Load local video and convert to base64 ---
def get_base64_video(video_path):
    with open(video_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_base64 = get_base64_video("1032549521-preview.mp4")
import streamlit as st

st.set_page_config(layout="wide")

video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://www.shutterstock.com/video/clip-1032549521-green-hacker-text-code-on-screen-graphic?dd_referrer=https%3A%2F%2Fwww.google.com%2F">
		  Your browser does not support HTML5 video.
		</video>
        """

st.markdown(video_html, unsafe_allow_html=True)
st.title('Video page')

st.markdown("This text is written on top of the background video! 😁")
