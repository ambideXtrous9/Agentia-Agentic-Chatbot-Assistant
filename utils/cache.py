import json
import os
import streamlit as st

def save_chat_sessions():
    """Save chat sessions to a file"""
    if 'chat_sessions' in st.session_state:
        with open('chat_sessions.json', 'w') as f:
            json.dump({
                'sessions': st.session_state.chat_sessions,
                'current': st.session_state.current_session,
                'counter': st.session_state.session_counter
            }, f)

def load_chat_sessions():
    """Load chat sessions from file if exists"""
    if os.path.exists('chat_sessions.json'):
        try:
            with open('chat_sessions.json', 'r') as f:
                data = json.load(f)
                st.session_state.chat_sessions = data.get('sessions', {})
                st.session_state.current_session = data.get('current', None)
                st.session_state.session_counter = data.get('counter', 0)
                return True
        except:
            pass
    return False