import google.generativeai as genai
import speech_recognition as sr
import streamlit as st
import playsound
import os
from translate import Translator
from gtts import gTTS

genai.configure(api_key="AIzaSyBPxmrE9bKVIqf8HZ-rHSbUYqMsA3zHVzY")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "answer me with a very simplestic answer the max amount of chars is 499\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I can do that!  What do you want me to answer? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "answer me without emojis\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. What question do you want me to answer? I will keep my response under 499 characters. \n",
      ],
    },
  ]
)


r = sr.Recognizer()


Translator(from_lang="ar", to_lang="en").translate("")

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


st.title("الذكاء الاصطناعي")

col1, col2 = st.columns(2)

col2.subheader("الاعدادات")
tos = col1.selectbox("طريقة استقبال الكلام", ("كتابة","صوت"),)

button = False
text_input = ""
response = ""


if tos == "صوت":
    button = st.button("اضغط للاستماع")
    if button:
        st.write("#### يتم الاستماع")
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio, language="ar")
                text = text.lower()
                tr = Translator(from_lang="ar", to_lang="en").translate(text)
                response = chat_session.send_message(tr)

                st.write(f"{Translator(from_lang='en', to_lang='ar').translate(response.text)}")
                tts = gTTS(f"{Translator(from_lang='en', to_lang='ar').translate(response.text)}", lang="ar")
                try:
                    tts.save("h.mp3")
                except:
                    print("already in project")

                playsound.playsound("h.mp3")
                os.remove("h.mp3")

        except sr.UnknownValueError:
            r = sr.Recognizer()
            print("Couldn't recognize")


else:
    text_input = st.text_input("اكتب هنا")
    st.write(text_input)
    try:
        tr = Translator(from_lang="ar", to_lang="en").translate(text_input)
        response = chat_session.send_message(tr)
        st.write(f"{Translator(from_lang='en', to_lang='ar').translate(response.text)}")
        tts = gTTS(f"{Translator(from_lang='en', to_lang='ar').translate(response.text)}", lang="ar")
        try:
            tts.save("h.mp3")
        except:
            print("already in project")

        playsound.playsound("h.mp3")
        os.remove("h.mp3")
    except:
        pass


