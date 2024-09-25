import streamlit as st

st.markdown(
    """
    <style>
    body {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("فيديوهات عن اليوم الوطني")

col1, col2 = st.columns(2)
video_1 = "https://www.youtube.com/watch?v=D0D4Pa22iG0"
col1.video(video_1)
col1.video(video_1)
col2.video(video_1)
col2.video(video_1)