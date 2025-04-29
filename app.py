import streamlit as st
from models.qwen_model import load_qwen_model, create_pipeline
from tools.search_tools import setup_search_tool
from workflow import create_workflow
from services.session_service import initialize_session_state, new_session, switch_session, clear_all_chats
from services.chat_service import process_user_input
from utils.display import setup_custom_css, display_chat
from PIL import Image
import io
import base64

def get_logo_base64():
    """Convert logo to base64 for favicon and title"""
    try:
        img = Image.open("agentia2.png")
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

def display_title_with_logo(logo_base64):
    """Display title with logo image instead of emoji"""
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            <img src="data:image/png;base64,{logo_base64}" width="40">
            <h1 style="margin: 0;">Agentia Assistant</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_logo():
    """Display the logo in sidebar"""
    st.image("agentia.jpg", use_container_width=True)
    st.markdown(
        """
        <style>
        [data-testid="stImage"] img {
            border-radius: 50%;
            object-fit: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    # Initialize app with logo as favicon
    logo_base64 = get_logo_base64()
    favicon = f"data:image/png;base64,{logo_base64}" if logo_base64 else "🤖"
    
    st.set_page_config(
        page_title="Agentia",
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    setup_custom_css()
    initialize_session_state()
    
    # Load AI resources
    model_path = "Qwen/Qwen2.5-0.5B-Instruct"
    qwen_model, qwen_tokenizer = load_qwen_model(model_path)
    qwen_pipe = create_pipeline(qwen_model, qwen_tokenizer)
    search_tool = setup_search_tool()
    app = create_workflow(qwen_pipe, qwen_tokenizer, search_tool)
    
    # UI Components with logo in title
    if logo_base64:
        display_title_with_logo(logo_base64)
    else:
        st.title("🤖 Agentia Assistant")
    
    # Sidebar with logo
    with st.sidebar:
        display_logo()
        
        st.header("Chat Sessions")
        if st.button("➕ New Chat"):
            new_session()
        if st.button("🗑️ Clear All Chats"):
            clear_all_chats()
        st.markdown("---")
        
        for session_id, session_data in st.session_state.chat_sessions.items():
            is_active = session_id == st.session_state.current_session
            emoji = "💬" if is_active else "🗨️"
            title = session_data["title"]
            
            if st.button(
                f"{emoji} {title}",
                key=f"btn_{session_id}",
                on_click=switch_session,
                args=(session_id,),
                use_container_width=True
            ):
                pass
    
    # Main Chat Area
    display_chat()
    
    # Input Area
    input_container = st.container()
    with input_container:
        st.text_input(
            "Type your message...",
            key="user_input",
            on_change=process_user_input,
            args=(app,),
            label_visibility="collapsed",
            placeholder="Ask me anything..."
        )

if __name__ == "__main__":
    main()