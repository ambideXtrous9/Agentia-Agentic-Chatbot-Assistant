import time
from utils.response import extract_answer
from utils.cache import save_chat_sessions
import streamlit as st

def process_user_input(app):
    """Process the user input and generate response"""
    user_input = st.session_state.user_input.strip()
    if not user_input:
        return
    
    current_session = st.session_state.chat_sessions[st.session_state.current_session]
    current_session["messages"].append({
        "role": "user",
        "content": user_input,
        "timestamp": time.time()
    })
    
    if len(current_session["messages"]) == 1:
        current_session["title"] = user_input[:30] + ("..." if len(user_input) > 30 else "")
    
    save_chat_sessions()
    
    spinner = st.empty()
    spinner.markdown("<div style='text-align: center;'><div class='spinner'></div><p>Thinking...</p></div>", unsafe_allow_html=True)
    
    try:
        start_time = time.time()
        result = app.invoke({"question": user_input})
        processing_time = time.time() - start_time
        
        clean_response = extract_answer(result['response'])
        
        current_session["messages"].append({
            "role": "assistant",
            "content": clean_response,
            "original_response": result['response'],
            "classification": result['classification'],
            "processing_time": processing_time,
            "timestamp": time.time()
        })
        
    except Exception as e:
        current_session["messages"].append({
            "role": "assistant",
            "content": f"Sorry, I encountered an error: {str(e)}",
            "classification": "error",
            "processing_time": 0,
            "timestamp": time.time()
        })
    finally:
        spinner.empty()
    
    st.session_state.user_input = ""
    save_chat_sessions()