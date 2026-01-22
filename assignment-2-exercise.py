from __future__ import annotations

from datetime import date
import random
import re
import streamlit as st

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

# TODO (0): Paste your OpenAI API key here if you want LLM advice to work.
OPENAI_API_KEY = ""


APP_TITLE = "🧘 Daily Anxiety Tracker Bot"


def today_str() -> str:
    # TODO (1): Return today's date string like "2026-01-20"
    # Hint: date.today().isoformat()
    return "TODO_TODAY"


def append_message(role: str, content: str) -> None:
    st.session_state.messages.append({"role": role, "content": content})


def render_history() -> None:
    # TODO (2): Render chat history from st.session_state.messages
    # Hint:
    # for m in st.session_state.messages:
    #   with st.chat_message(m["role"]):
    #       st.markdown(m["content"])
    pass


def parse_level(user_text: str) -> int | None:
    """
    Accept:
      - "7", "7/10"
      - "log 7", "anxiety 7", "level 7"
    """
    # TODO (3): Implement parsing with regex and return int or None
    # Hint regex idea:
    # re.match(r"^(?:(?:log|anxiety|level)\s*)?(\d{1,2})(?:\s*/\s*10)?\s*$", ...)
    return None


def valid_level(level: int) -> bool:
    # TODO (4): Return True if level is 1..10
    return False


def rule_smalltalk(user_text: str) -> str | None:
    """
    If user greets / says small talk / mentions deadlines,
    respond politely and guide them back to entering 1–10.
    """
    # TODO (5): Implement:
    # - greetings set (hi/hello/hey...)
    # - small talk pattern like "how are you"
    # - workload signals like "deadline/exam/assignment"
    # Hint: use random.choice([...]) for 2–3 variations.
    return None


def rule_feedback(level: int) -> str:
    """
    Rule-based feedback after logging.
    Must cover ranges: 1–3, 4–6, 7–8, 9–10.
    """
    # TODO (6): Write short, supportive messages for each range.
    # Safety hint: For 9–10 include a brief safety note (emergency/crisis support).
    return "TODO_RULE_FEEDBACK"


def llm_advice(level: int, note: str | None) -> str:
    """
    OPTIONAL: Called after saving.
    If key missing, return a helpful message instead of crashing.
    """
    # TODO (7): If OPENAI_API_KEY is empty, return a message like:
    # "LLM advice unavailable because no API key was provided."
    #
    # TODO (8): If OpenAI is None, return a message telling user to install openai.
    #
    # TODO (9): Create OpenAI client and call chat.completions.create(...)
    # Keep prompts concise and non-clinical.
    # End with: "This is not medical advice."
    return "TODO_LLM_ADVICE"


def format_history(log: list[dict], limit: int = 3) -> str:
    # TODO (10): Show the last `limit` items as "- date: level/10"
    # If empty: return a friendly message.
    return "TODO_HISTORY"


# -------------------- App UI --------------------

st.set_page_config(page_title="Daily Anxiety Tracker", page_icon="🧘")
st.title(APP_TITLE)

if st.button("Clear chat"):
    # TODO (11): Clear these keys and rerun:
    # messages, stage, today_level, today_note, anxiety_log
    # Hint: st.session_state.pop("messages", None); st.rerun()
    pass

# State init
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! Let’s do a quick daily check-in.\n\n"
                "**Step 1:** Rate your anxiety today from **1 to 10**.\n"
                "Type a number like `6`."
            ),
        }
    ]

if "stage" not in st.session_state:
    # TODO (12): Set initial stage to "ASK_LEVEL"
    st.session_state.stage = "TODO_STAGE"

if "today_level" not in st.session_state:
    st.session_state.today_level = None

if "today_note" not in st.session_state:
    st.session_state.today_note = None

if "anxiety_log" not in st.session_state:
    st.session_state.anxiety_log = []

render_history()

user_text = st.chat_input("Type here (try: 6, log 6, help, today, history, advice)")

if user_text:
    append_message("user", user_text)
    with st.chat_message("user"):
        st.markdown(user_text)

    cmd = user_text.strip().lower()

    # TODO (13): Implement simple commands (help/today/history/advice) in a beginner-friendly way.
    # - help: show command list
    # - today: show today's saved log if exists
    # - advice: regenerate llm advice (if a level exists)
    #
    # Hint: You can handle commands before the stage machine and use st.stop() after responding.

    # Stage machine
    if st.session_state.stage == "ASK_LEVEL":
        # TODO (14): First handle smalltalk:
        # reply = rule_smalltalk(user_text)
        # If reply is None, parse level and validate:
        # - level = parse_level(user_text)
        # - if level is None -> prompt "enter 1..10"
        # - elif not valid_level(level) -> out of range message
        # - else -> save today_level, set stage to "ASK_NOTE", ask optional note or "skip"
        reply = "TODO_LEVEL_STAGE_REPLY"

        append_message("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)

    elif st.session_state.stage == "ASK_NOTE":
        # TODO (15): Save note:
        # - if user typed "skip": today_note = None
        # - else: keep it short (e.g., first 200 chars)
        # Then:
        # - save entry into anxiety_log: {"date": today_str(), "level": today_level, "note": today_note}
        # - build reply with:
        #   "Rule-based feedback" (rule_feedback)
        #   "LLM-based advice" (llm_advice)
        # - set stage to "DONE"
        reply = "TODO_NOTE_STAGE_REPLY"

        append_message("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)

    else:
        # DONE stage
        # TODO (16): If user types a number again, restart to "ASK_LEVEL"
        # Otherwise: prompt help / restart
        reply = "TODO_DONE_STAGE_REPLY"

        append_message("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)
