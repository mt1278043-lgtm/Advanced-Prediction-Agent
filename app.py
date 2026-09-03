import streamlit as st
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

st.set_page_config(page_title="Advanced Prediction Agent", layout="wide")

st.title("🤖 Advanced Prediction Agent")
st.write("Powered by LangGraph and Streamlit")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def create_prediction_agent():
    """Create a LangGraph-based prediction agent."""
    graph = StateGraph(State)

    llm = ChatOpenAI(model="gpt-4o-mini")

    def process_input(state):
        """Process user input through the LLM."""
        messages = state.get("messages", [])
        response = llm.invoke(messages)
        return {"messages": [response]}

    graph.add_node("predictor", process_input)
    graph.add_edge(START, "predictor")
    graph.add_edge("predictor", END)

    return graph.compile()

if __name__ == "__main__":
    agent = create_prediction_agent()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("OpenAI API Key", type="password")
        if api_key:
            st.session_state.api_key = api_key

    st.header("Chat Interface")

    for msg in st.session_state.messages:
        with st.chat_message(msg.get("role", "user")):
            st.write(msg.get("content", ""))

    if prompt := st.chat_input("Ask me anything about predictions..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                input_state = {
                    "messages": [{"role": "user", "content": prompt}]
                }
                result = agent.invoke(input_state)

                assistant_response = result["messages"][-1]
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": str(assistant_response)
                })
                st.write(str(assistant_response))
