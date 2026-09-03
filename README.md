# Advanced Prediction Agent

A powerful prediction agent built with LangGraph and Streamlit for intelligent forecasting and analysis.

## Features

- 🚀 Built with LangGraph for advanced AI workflows
- 💬 Interactive Streamlit chat interface
- 🔄 Real-time predictions
- 🎯 Extensible agent architecture

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mt1278043-lgtm/Advanced-Prediction-Agent.git
cd Advanced-Prediction-Agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Deployment on Streamlit Cloud

1. Push this repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select this repository
5. Set the main file to `app.py`
6. Add your OpenAI API key as a secret in the Streamlit Cloud dashboard

## Project Structure

```
Advanced-Prediction-Agent/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── README.md             # This file
```

## Configuration

Edit `.streamlit/config.toml` to customize the Streamlit app appearance and behavior.

## License

MIT License - see LICENSE file for details
