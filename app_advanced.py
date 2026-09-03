"""
Advanced Streamlit app with LangGraph integration.
"""

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from agents import create_analysis_agent, create_multi_scenario_agent
from prompts import SYSTEM_PROMPT, ANALYSIS_PROMPT, PREDICTION_PROMPT
from utils import load_api_key, format_for_display, extract_predictions

st.set_page_config(
    page_title="Advanced Prediction Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 Advanced Prediction Agent")
st.markdown("*Powered by LangGraph + OpenAI + Streamlit*")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key Setup
    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        value=load_api_key() or "",
        help="Your OpenAI API key for predictions"
    )

    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input

    # Agent Selection
    agent_type = st.selectbox(
        "Select Analysis Type",
        ["Analysis Agent", "Multi-Scenario Agent"],
        help="Choose the type of prediction analysis"
    )

    st.divider()

    # Advanced Settings
    with st.expander("Advanced Settings"):
        temperature = st.slider(
            "Temperature (Creativity)",
            0.0, 1.0, 0.7,
            help="Higher = more creative, Lower = more deterministic"
        )
        max_tokens = st.slider(
            "Max Response Tokens",
            100, 2000, 1000,
            step=100
        )

    st.divider()

    # Information
    st.markdown("### 📚 About")
    st.markdown("""
    This agent uses LangGraph to:
    - Analyze complex information
    - Generate multi-scenario predictions
    - Assess risks and opportunities
    - Provide actionable insights
    """)

# Main Chat Interface
st.header("💬 Prediction Chat")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "predictions" not in st.session_state:
    st.session_state.predictions = []

if "analysis" not in st.session_state:
    st.session_state.analysis = ""

# Display chat history
for message in st.session_state.messages:
    role = message.get("role", "user")
    content = message.get("content", "")
    with st.chat_message(role):
        st.markdown(content)

# User input
if prompt := st.chat_input("Ask me about predictions, trends, or scenarios..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Analyzing..."):
            try:
                api_key = os.environ.get("OPENAI_API_KEY")
                if not api_key:
                    st.error("❌ Please provide an OpenAI API key in the sidebar")
                else:
                    # Select and run agent
                    if agent_type == "Analysis Agent":
                        agent = create_analysis_agent()
                        input_state = {
                            "messages": [HumanMessage(content=prompt)],
                            "predictions": {},
                            "analysis": ""
                        }
                    else:
                        agent = create_multi_scenario_agent()
                        input_state = {
                            "messages": [HumanMessage(content=prompt)],
                            "predictions": {},
                            "analysis": ""
                        }

                    # Run agent
                    result = agent.invoke(input_state)

                    # Extract response
                    messages = result.get("messages", [])
                    if messages:
                        response = messages[-1]
                        response_text = str(response.content)

                        # Display response
                        st.markdown(response_text)

                        # Store in session
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response_text
                        })

                        # Extract and display predictions
                        predictions = extract_predictions(response_text)
                        st.session_state.predictions.append(predictions)

                        if predictions.get("confidence"):
                            st.info(
                                f"📊 Confidence Level: {predictions['confidence']*100:.1f}%"
                            )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.warning(
                    "Please ensure your API key is valid and has sufficient credits."
                )

# Sidebar - Prediction History
st.sidebar.divider()
st.sidebar.header("📊 Prediction History")

if st.session_state.predictions:
    for i, pred in enumerate(st.session_state.predictions, 1):
        with st.sidebar.expander(f"Prediction #{i}"):
            if pred.get("confidence"):
                st.metric(
                    "Confidence",
                    f"{pred['confidence']*100:.1f}%"
                )
            st.text_area(
                "Raw Response",
                value=pred.get("raw", "")[:300],
                height=100,
                disabled=True
            )
else:
    st.sidebar.info("No predictions yet. Start asking questions!")

# Footer
st.divider()
st.markdown("""
---
Built with ❤️ using [LangGraph](https://langchain-ai.github.io/langgraph/)
and [Streamlit](https://streamlit.io/)
""")
