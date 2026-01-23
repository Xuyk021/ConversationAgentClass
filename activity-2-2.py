import streamlit as st
from openai import OpenAI

# ---------- Config ----------
st.set_page_config(page_title="Worry Chatbot", layout="centered")
st.title("Worry Chatbot")

OPENAI_API_KEY = ""  # e.g., "sk-..."
client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_STYLE = """
You are a warm and supportive chat partner.
The user may be sharing worries or negative emotions.

Your goals:
1) Briefly acknowledge and validate the user's feelings.
2) Ask exactly one gentle, open-ended follow-up question.
3) Offer one small, practical, and non-overwhelming coping suggestion.

Constraints:
- Do not provide medical, clinical, or diagnostic advice.
- Avoid judgmental or prescriptive language.
- Keep the response empathetic, calm, and natural.
- Limit the response to under 120 words.
"""

# ---------- session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi. What’s been bothering you today?"}
    ]

# ---------- render history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- user input ----------
user_text = st.chat_input("Type your message...")
if user_text:
    # 1. add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )
    with st.chat_message("user"):
        st.write(user_text)

    # 2. call OpenAI 
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=SYSTEM_STYLE,
        input=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
    )

    assistant_text = response.output_text

    # 3. add assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text}
    )
    with st.chat_message("assistant"):
        st.write(assistant_text)
