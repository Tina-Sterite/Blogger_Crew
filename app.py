import os
import streamlit as st
from dotenv import load_dotenv    
from src.components.navigation import page_config, custom_style, footer 
from crew import BlogCrew
from langchain_core.callbacks import BaseCallbackHandler
from typing import Any, Dict

# Environment Variables
load_dotenv()

USER_AGENT = os.getenv("USER_AGENT")

class CustomHandler(BaseCallbackHandler):
    def __init__(self, agent_name: str) -> None:
        super().__init__()
        self.agent_name = agent_name

    def on_chain_start(self, serialized: Dict[str, Any], outputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": "assistant", "content": outputs['input']})
        st.chat_message("assistant").write(outputs['input'])

    def on_agent_action(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": "assistant", "content": inputs['input']})
        st.chat_message("assistant").write(inputs['input'])

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        st.session_state.messages.append({"role": self.agent_name, "content": outputs['output']})
        st.chat_message(self.agent_name).write(outputs['output'])


def main():
    # Streamlit Page Setup
    page_config("Crew Agents",":writing_hand:", "wide") 
    custom_style()
    st.sidebar.image('./src/logo.png')

    st.title("✍️Crew Agents✍️")
    st.markdown(
        '''
        <style>
            div.block-container{padding-top:0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        ### Write Structured blogs with AI Agents, powered by Llamma3 via Ollama & CrewAI  [Towards-GenAI](https://github.com/Towards-GenAI)
        """
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    col1, col2 = st.columns(2)
    
    # Input for blog topic
    with col1:
        blog_topic = st.text_input("Enter the blog topic:")

    # Dropdown for selecting the type of content  
    with col2:
        content_type = st.selectbox(
            "Select the type of content:", 
            ["Blog Post", "Research Paper", "Technical Report"]
        )

    if st.button("Start Blogging Crew"):
        if blog_topic:
            output_placeholder = st.empty()  # Create the placeholder here
            blog_crew = BlogCrew(blog_topic, content_type, output_placeholder)
            try:
                result_str, pdf_file, file_content = blog_crew.run()
                st.write(result_str)
            
            # Create download button
                st.download_button(
                    label=f"Download {pdf_file}",
                    data=file_content,
                    file_name=pdf_file,
                    mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a blog topic.")


if __name__ == "__main__":
    main()
    with st.sidebar:
        footer()