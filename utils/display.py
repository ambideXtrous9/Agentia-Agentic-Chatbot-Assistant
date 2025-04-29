import streamlit as st

def setup_custom_css():
    """Setup custom CSS for the chat interface"""
    st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
    }
    .chat-message.user {
        background-color: #f0f2f6;
        justify-content: flex-end;
    }
    .chat-message.assistant {
        background-color: #e6f7ff;
        justify-content: flex-start;
    }
    .full-response {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        border-left: 3px solid #6c757d;
    }
    </style>
    """, unsafe_allow_html=True)
    

def display_chat():
    """Display the current chat session messages"""
    current_session = st.session_state.chat_sessions.get(st.session_state.current_session)
    
    if current_session:
        chat_container = st.container()
        with chat_container:
            for msg in current_session["messages"]:
                role = msg["role"]
                content = msg["content"]
                classification = msg.get("classification", "")
                processing_time = msg.get("processing_time", 0)
                
                if role == "user":
                    st.markdown(
                        f"""<div class="chat-message user">
                            <div><strong>You:</strong> {content}</div>
                        </div>""",
                        unsafe_allow_html=True
                    )
                else:
                    with st.container():
                        col1, col2 = st.columns([10, 2])
                        with col1:
                            st.markdown(f"**Assistant** (Classification: {classification} | Time: {processing_time:.2f}s)")
                        with col2:
                            show_full = st.checkbox("Full", key=f"full_{msg['timestamp']}")
                        
                        if "code" in classification.lower():
                            st.code(content)
                        else:
                            st.markdown(content)
                        
                        if show_full and msg.get("original_response") and msg["original_response"] != content:
                            st.markdown("---")
                            st.markdown("**Full Response:**")
                            st.markdown(f'<div class="full-response">{msg["original_response"]}</div>', unsafe_allow_html=True)