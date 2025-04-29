import time
from utils.cache import save_chat_sessions
import streamlit as st
import os

def initialize_session_state():
    """Initialize all necessary session state variables"""
    from utils.cache import load_chat_sessions
    if not load_chat_sessions():
        if 'chat_sessions' not in st.session_state:
            st.session_state.chat_sessions = {}
            st.session_state.current_session = None
            st.session_state.session_counter = 0
    
    if not st.session_state.current_session or st.session_state.current_session not in st.session_state.chat_sessions:
        new_session()

def new_session():
    """Create a new chat session"""
    st.session_state.session_counter += 1
    session_id = f"session_{st.session_state.session_counter}"
    st.session_state.chat_sessions[session_id] = {
        "messages": [],
        "created_at": time.time(),
        "title": f"New Chat {st.session_state.session_counter}"
    }
    st.session_state.current_session = session_id
    save_chat_sessions()

def switch_session(session_id):
    """Switch to a different chat session"""
    st.session_state.current_session = session_id
    save_chat_sessions()

def clear_all_chats():
    """Clear all chat history"""
    st.session_state.chat_sessions = {}
    st.session_state.current_session = None
    st.session_state.session_counter = 0
    new_session()
    if os.path.exists('chat_sessions.json'):
        os.remove('chat_sessions.json')