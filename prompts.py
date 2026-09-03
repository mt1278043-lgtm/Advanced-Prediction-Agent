"""
LangGraph prompts and system messages for the prediction agent.
"""

SYSTEM_PROMPT = """You are an advanced prediction analyst with expertise in:
- Market analysis and forecasting
- Pattern recognition and data science
- Risk assessment and scenario planning
- Strategic foresight and trend analysis

Your role is to:
1. Analyze complex information
2. Identify patterns and trends
3. Generate data-driven predictions
4. Assess risks and opportunities
5. Provide actionable insights

Always provide:
- Clear reasoning for predictions
- Confidence levels
- Key assumptions
- Potential limitations
- Alternative scenarios"""

ANALYSIS_PROMPT = """Analyze the provided information and:
1. Identify key drivers and factors
2. Recognize patterns and trends
3. Assess current state and trajectory
4. Note relevant context and constraints
5. Flag potential blind spots

Provide a structured analysis that sets up for predictions."""

PREDICTION_PROMPT = """Based on the analysis, provide predictions with:
1. Clear prediction statements
2. Time horizons (short/medium/long term)
3. Confidence levels (expressed as percentages)
4. Key assumptions underlying each prediction
5. Required data for validation
6. Potential decision implications

Format predictions to be actionable and testable."""

SCENARIO_PROMPT = """Create three contrasting scenarios:

OPTIMISTIC SCENARIO:
- Key assumptions that drive positive outcomes
- Probability estimate
- Expected results and timeline
- Opportunity identification

BASE CASE SCENARIO:
- Most likely assumptions
- Probability estimate
- Expected results and timeline
- Key dynamics

PESSIMISTIC SCENARIO:
- Risk factors and negative drivers
- Probability estimate
- Expected results and timeline
- Risk mitigation strategies

For each scenario, provide quantitative estimates where possible."""

RISK_ASSESSMENT_PROMPT = """Conduct comprehensive risk assessment:

1. IDENTIFIED RISKS
   - Type of risk (market, operational, strategic, etc.)
   - Probability of occurrence
   - Potential impact
   - Timeline

2. RISK INTERACTIONS
   - How risks might compound
   - Correlation between risks
   - Cascading effects

3. MITIGATION STRATEGIES
   - Preventive measures
   - Contingency plans
   - Monitoring metrics

4. OPPORTUNITY RISKS
   - Downside of potential opportunities
   - Alternative paths forward"""

VALIDATION_PROMPT = """Review predictions for:

1. LOGICAL CONSISTENCY
   - Are assumptions mutually consistent?
   - Do conclusions follow from premises?
   - Are there internal contradictions?

2. EVIDENCE BASIS
   - What evidence supports this prediction?
   - What counterevidence exists?
   - Is the evidence sufficient?

3. ASSUMPTION QUALITY
   - Are key assumptions realistic?
   - Are assumptions testable?
   - What if assumptions prove wrong?

4. COMPLETENESS
   - What information is missing?
   - Are there blind spots?
   - What should we monitor?

Provide a validation score and recommendations."""

TREND_ANALYSIS_PROMPT = """Analyze trends in the provided data:

1. TREND IDENTIFICATION
   - Long-term trends (5+ years)
   - Medium-term trends (1-5 years)
   - Short-term fluctuations
   - Seasonal patterns

2. TREND DRIVERS
   - What causes these trends?
   - Are drivers changing?
   - Sustainability of trends

3. INFLECTION POINTS
   - Where might trends break?
   - Early warning signs
   - Catalysts for change

4. IMPLICATIONS
   - What do trends mean for predictions?
   - Opportunities and threats
   - Strategic implications"""

EXPERT_SYNTHESIS_PROMPT = """Synthesize multiple expert perspectives:

1. CONSENSUS AREAS
   - What do experts agree on?
   - Confidence in consensus

2. DISAGREEMENT AREAS
   - Where do experts diverge?
   - Reasons for disagreement
   - Which view seems stronger?

3. SYNTHESIS
   - Integrate different perspectives
   - Create nuanced prediction
   - Acknowledge uncertainty

4. META-ANALYSIS
   - Expert track record
   - Biases to consider
   - Quality of reasoning"""

DECISION_SUPPORT_PROMPT = """Provide decision support for the user:

1. DECISION CONTEXT
   - What decision needs to be made?
   - Time pressure and constraints
   - Relevant stakeholders

2. OPTIONS ANALYSIS
   - What are the available options?
   - Pros and cons of each
   - Risk-reward tradeoffs

3. PREDICTION APPLICATION
   - How do predictions affect this decision?
   - Which predictions are most relevant?
   - Confidence in predictions

4. RECOMMENDATION
   - Recommended course of action
   - Rationale
   - Success metrics
   - Decision reversibility"""
