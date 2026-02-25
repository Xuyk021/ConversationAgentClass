import os
import streamlit as st
from openai import OpenAI




MODEL = "gpt-4o-mini"
st.set_page_config(page_title="Daily Check-in Chatbot")
st.title("🧠 Daily Depression Check-in")

# ===== Session state =====
if "stage" not in st.session_state:
    st.session_state.stage = "level"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "level" not in st.session_state:
    st.session_state.level = None

if "note" not in st.session_state:
    st.session_state.note = None

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

if "api_key_confirmed" not in st.session_state:
    st.session_state.api_key_confirmed = False

    
# ===== Sidebar =====
st.sidebar.markdown("## :material/settings: Settings")

# ===== API Key input ===== DO NOT Change THIS SECTION =====
disabled_input = st.session_state.api_key_confirmed

api_key_input = st.sidebar.text_input(
    ":material/key: OpenAI API Key",
    value=st.session_state.api_key,
    type="password",
    disabled=disabled_input
)

# ----- Confirm button -----
if not st.session_state.api_key_confirmed:
    if st.sidebar.button(
        ":material/check: Confirm API Key",
        use_container_width=True
    ):
        if api_key_input.strip():
            st.session_state.api_key = api_key_input.strip()
            st.session_state.api_key_confirmed = True
            st.rerun()
        else:
            st.sidebar.error("Please enter a key.")

# ----- Change button -----
else:
    if st.sidebar.button(
        ":material/edit: Change API Key",
        use_container_width=True
    ):
        st.session_state.api_key_confirmed = False
        st.rerun()

# ----- Block app if not confirmed -----
if not st.session_state.api_key_confirmed:
    st.sidebar.warning("Confirm API key to start.")
    st.stop()

# TODO: Create client after confirmation to avoid unnecessary initialization 


# ===========================================================================

# ----- Export history -----
import json

st.sidebar.markdown("## :material/build: Tools")

# TODO: Export history as a file with proper formatting and metadata (json, txt, csv, etc.)

# ===========================================================================


# ----- Clear history -----
if st.sidebar.button(":material/delete: Clear chat history", use_container_width=True):
    st.session_state.messages = []
    st.session_state.stage = "level"
    st.session_state.level = None
    st.session_state.note = None
    st.rerun()

# TODO: Render history =====

# ===========================================================================


# ===== Streaming helper =====
def stream_llm(system, user):
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.3,
        stream=True,
    )

    full_text = ""

    def generator():
        nonlocal full_text
        for chunk in stream:
            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_text += token
                yield token

    return generator, lambda: full_text


# ===== Stage logic =====
if st.session_state.stage == "level":
    if not st.session_state.messages:
        msg = "Please enter your depression level from 1 to 10 (e.g., 6, log 6, 7/10)."
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.rerun()

    user_input = st.chat_input("Enter level...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        # TODO: Analyze level input 
   








        # ===========================================================================
        st.rerun()

elif st.session_state.stage == "feedback":
    level = st.session_state.level

    # TODO: Give feedback based on level using LLM 









    # ===========================================================================
    st.session_state.stage = "note"
    st.rerun()

elif st.session_state.stage == "note":
    note_input = st.chat_input("Write your note...")

    if note_input:
        st.session_state.note = note_input
        st.session_state.messages.append({"role": "user", "content": note_input})
        with st.chat_message("user"):
            st.write(note_input)

        # TODO: Respond to note with LLM








        # ===========================================================================
        st.session_state.stage = "chat"
        st.rerun()

elif st.session_state.stage == "chat":
    user_input = st.chat_input("Chat...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # TODO: Respond to chat with LLM









        # ===========================================================================

        st.rerun()