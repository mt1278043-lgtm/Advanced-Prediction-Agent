"""
Advanced prediction agents built with LangGraph.
"""

from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """State for the prediction agent."""
    messages: Annotated[list[BaseMessage], add_messages]
    predictions: dict
    analysis: str


def create_analysis_agent():
    """Create an agent for analyzing input and making predictions."""

    graph = StateGraph(AgentState)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    def analyze_input(state: AgentState) -> AgentState:
        """Analyze user input."""
        messages = state.get("messages", [])

        analysis_prompt = """You are an advanced prediction analyst.
        Analyze the following input and identify key prediction opportunities:

        Focus on:
        1. Market trends
        2. Pattern recognition
        3. Risk factors
        4. Opportunity areas"""

        response = llm.invoke([
            HumanMessage(content=analysis_prompt),
            *messages
        ])

        return {
            **state,
            "messages": state["messages"] + [response],
            "analysis": response.content
        }

    def make_predictions(state: AgentState) -> AgentState:
        """Generate predictions based on analysis."""
        messages = state.get("messages", [])

        prediction_prompt = """Based on the analysis, provide specific predictions with:
        1. Prediction statement
        2. Confidence level (0-100%)
        3. Time horizon
        4. Key assumptions
        5. Potential risks"""

        response = llm.invoke([
            HumanMessage(content=prediction_prompt),
            *messages
        ])

        return {
            **state,
            "messages": state["messages"] + [response],
            "predictions": {"primary": response.content}
        }

    def validate_predictions(state: AgentState) -> AgentState:
        """Validate and cross-check predictions."""
        messages = state.get("messages", [])

        validation_prompt = """Review the predictions for:
        1. Logical consistency
        2. Data-driven reasoning
        3. Realistic assumptions
        4. Potential blind spots

        Provide validation feedback."""

        response = llm.invoke([
            HumanMessage(content=validation_prompt),
            *messages
        ])

        return {
            **state,
            "messages": state["messages"] + [response]
        }

    # Add nodes
    graph.add_node("analyze", analyze_input)
    graph.add_node("predict", make_predictions)
    graph.add_node("validate", validate_predictions)

    # Add edges
    graph.add_edge(START, "analyze")
    graph.add_edge("analyze", "predict")
    graph.add_edge("predict", "validate")
    graph.add_edge("validate", END)

    return graph.compile()


def create_multi_scenario_agent():
    """Create an agent for multi-scenario analysis."""

    graph = StateGraph(AgentState)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

    def scenario_planning(state: AgentState) -> AgentState:
        """Plan multiple scenarios."""
        messages = state.get("messages", [])

        scenario_prompt = """Generate 3 distinct scenarios:
        1. Optimistic scenario
        2. Base case scenario
        3. Pessimistic scenario

        For each, provide:
        - Key assumptions
        - Probability estimate
        - Likely outcomes"""

        response = llm.invoke([
            HumanMessage(content=scenario_prompt),
            *messages
        ])

        return {
            **state,
            "messages": state["messages"] + [response]
        }

    def risk_assessment(state: AgentState) -> AgentState:
        """Assess risks across scenarios."""
        messages = state.get("messages", [])

        risk_prompt = """Assess risks and opportunities:
        1. Identify tail risks
        2. Quantify potential impact
        3. Suggest mitigation strategies"""

        response = llm.invoke([
            HumanMessage(content=risk_prompt),
            *messages
        ])

        return {
            **state,
            "messages": state["messages"] + [response]
        }

    # Add nodes
    graph.add_node("scenario", scenario_planning)
    graph.add_node("risk", risk_assessment)

    # Add edges
    graph.add_edge(START, "scenario")
    graph.add_edge("scenario", "risk")
    graph.add_edge("risk", END)

    return graph.compile()
