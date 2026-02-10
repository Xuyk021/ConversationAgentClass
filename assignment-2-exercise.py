from __future__ import annotations


from datetime import date
import random
import re
import streamlit as st

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

# TODO: Paste your OpenAI API key here if you want LLM advice to work.
# Start of the code block ===========================
OPENAI_API_KEY = ""
# End of the code block =============================


APP_TITLE = "🧘 Daily Anxiety Tracker Bot"


def today_str() -> str:
    return date.today().isoformat()


def append_history(role: str, content: str) -> None:
    st.session_state.history.append({"role": role, "content": content})


def render_history() -> None:
    # TODO (1): Render chat history from st.session_state.history
    # Hint:
    # for m in st.session_state.history:
    #   with st.chat_message(m["role"]):
    #       st.markdown(m["content"])
    # Start of the code block ===========================
    

    # End of the code block =============================
    pass


def parse_level(user_text: str) -> int | None:
    """
    Accept:
      - "7"
      - "7/10"
      - "log 7"
      - "anxiety 7"
      - "level 7"
    """
    t = user_text.strip().lower()
    m = re.match(r"^(?:(?:log|anxiety|level)\s*)?(\d{1,2})(?:\s*/\s*10)?\s*$", t)
    if not m:
        return None
    return int(m.group(1))


def valid_level(level: int) -> bool:
    return 1 <= level <= 10


def rule_smalltalk(user_text: str) -> str | None:
    """
    If user greets / says small talk / mentions deadlines,
    respond politely and guide them back to entering 1–10.
    """
    # TODO: Implement:
    # - greetings set (hi/hello/hey...)
    # - small talk pattern like "how are you"
    # - workload signals like "deadline/exam/assignment"
    # Hint: use random.choice([...]) for 2–3 variations.
    # Start of the code block ===========================
    

    # End of the code block =============================
    return None


def rule_feedback(level: int) -> str:
    """
    Rule-based feedback after logging.
    Must cover ranges: 1–3, 4–6, 7–8, 9–10.
    """
    # TODO: Write short, supportive messages for each range.
    # Safety hint: For 9–10 include a brief safety note (emergency/crisis support).
    # Start of the code block ===========================
    
    return ""
    # End of the code block =============================


def llm_advice(level: int, note: str | None) -> str:
    """
    OPTIONAL: Called after saving.
    If key missing, return a helpful message instead of crashing.
    """
    if not OPENAI_API_KEY:
        return "LLM advice is unavailable because no API key was provided in the code."
    if OpenAI is None:
        return "LLM advice is unavailable because the `openai` package is not installed."
    
    # TODO: Create OpenAI client and call chat.completions.create(...)
    # Keep prompts concise and non-clinical.
    # End with: "This is not medical advice."
    # Start of the code block ===========================
    
    return ""
    # End of the code block =============================


def format_history(log: list[dict], limit: int = 3) -> str:
    if not log:
        return "No history yet. Start by typing a number **1–10**."
    recent = log[-limit:]
    lines = ["Your most recent check-ins:"]
    for item in recent:
        lines.append(f"- {item['date']}: {item['level']}/10")
    return "\n".join(lines)


# -------------------- App UI --------------------

st.set_page_config(page_title="Daily Anxiety Tracker", page_icon="🧘")
st.title(APP_TITLE)

if st.button("Clear chat"):
    # TODO: This button should reset the chat state.
    # Use st.session_state.pop(key, default) to safely remove stored values.
    # The keys to clear are chat-related variables such as messages, stage,
    # today_level, today_note, and anxiety_log.
    # After clearing the state, use st.rerun() so the interface updates immediately.
    # Start of the code block ===========================
    

    # End of the code block =============================
    st.rerun()

# State init
if "history" not in st.session_state:
    st.session_state.history = [
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
    st.session_state.stage = "ASK_LEVEL"

if "today_level" not in st.session_state:
    st.session_state.today_level = None

if "today_note" not in st.session_state:
    st.session_state.today_note = None

if "anxiety_log" not in st.session_state:
    st.session_state.anxiety_log = []


render_history()



#-------------------- User input handling --------------------

user_text = st.chat_input("Type here (try: 6, log 6, help, today, history, advice)")

if user_text:
    append_history("user", user_text)
    with st.chat_message("user"):
        st.markdown(user_text)

    cmd = user_text.strip().lower()

    # Implement simple commands (help/today/history/advice) in a beginner-friendly way.
    # - help: show command list
    # - today: show today's saved log if exists
    # - advice: regenerate llm advice (if a level exists)
    # - history: show past 3 entries from anxiety_log with dates and levels.
    # Hint: You can handle commands before the stage machine and use st.stop() after responding.
    if cmd == "help":
        # TODO: Implement simple command 'help'
        # Start of the code block ===========================

        # End of the code block =============================

        st.stop()

    if cmd == "today":
        today = today_str()
        todays = [x for x in st.session_state.anxiety_log if x["date"] == today]
        if not todays:
            reply = "No check-in saved for today yet. Type a number **1–10** to start."
        else:
            last = todays[-1]
            reply = f"Today ({today}) you logged **{last['level']}/10**. Note: {last['note'] or '(none)'}"
        append_history("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)
        st.stop()
    
    if cmd == "history":
        # TODO: Implement simple command 'history'
        # Start of the code block ===========================

        # End of the code block ===========================

        st.stop()


    # Stage machine
    if st.session_state.stage == "ASK_LEVEL":
        # TODO: First handle smalltalk:
        # reply = rule_smalltalk(user_text)
        # If reply is None, parse level and validate:
        # - level = parse_level(user_text)
        # - if level is None -> prompt "enter 1..10"
        # - elif not valid_level(level) -> out of range message
        # - else -> save today_level, set stage to "ASK_NOTE", ask optional note or "skip"
        # Start of the code block ===========================
        
        reply = 

        # End of the code block ===========================

        append_history("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)

    elif st.session_state.stage == "ASK_NOTE":
        note = user_text.strip()
        # TODO: Save note:
        # - if user typed "skip": today_note = None
        # - else: keep it short (e.g., first 200 chars)
        # Then:
        # - save entry into anxiety_log: {"date": today_str(), "level": today_level, "note": today_note}
        # - build reply with:
        #   "Rule-based feedback" (rule_feedback)
        #   "LLM-based advice" (llm_advice)
        # - set stage to "DONE"
        # Start of the code block ===========================
        
        reply = 

        # End of the code block ===========================
        st.session_state.stage = "DONE"

        append_history("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)

    else:
        # DONE stage: allow advice regeneration or restart
        if cmd == "advice":
            if st.session_state.today_level is None:
                reply = "No level found. Type a number **1–10** to start."
                st.session_state.stage = "ASK_LEVEL"
            else:
                reply = "### LLM-based advice\n\n" + llm_advice(st.session_state.today_level, st.session_state.today_note)
        else:
            # If they type a number, restart new check-in
            maybe_level = parse_level(user_text)
            if maybe_level is not None:
                st.session_state.stage = "ASK_LEVEL"
                st.session_state.today_level = None
                st.session_state.today_note = None
                reply = "Starting a new check-in. Please enter today’s anxiety level **1–10**."
            else:
                reply = "Type `help` for commands, or type a number **1–10** to start a new check-in."

        append_history("assistant", reply)
        with st.chat_message("assistant"):
            st.markdown(reply)

