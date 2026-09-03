# Deployment Guide

## Streamlit Cloud Deployment

### Step 1: Prepare Your Repository

Ensure your repository is pushed to GitHub on the `claude/langgraph-streamlit-setup-oe5s43` branch:

```bash
git push -u origin claude/langgraph-streamlit-setup-oe5s43
```

### Step 2: Set Up Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **New app**
3. Select your GitHub repository: `mt1278043-lgtm/Advanced-Prediction-Agent`
4. Select the branch: `claude/langgraph-streamlit-setup-oe5s43`
5. Set the main file: `app.py`

### Step 3: Configure Secrets

After deployment, configure your API keys:

1. Go to your app's settings
2. Click **Secrets** in the left sidebar
3. Add your OpenAI API key:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

### Step 4: Access Your App

Your app will be available at:
- `https://<your-username>-advanced-prediction-agent.streamlit.app`

## Local Development

### Prerequisites
- Python 3.9+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/mt1278043-lgtm/Advanced-Prediction-Agent.git
cd Advanced-Prediction-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Docker Deployment

### Build Docker Image

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

### Build and Run

```bash
docker build -t prediction-agent .
docker run -p 8501:8501 -e OPENAI_API_KEY="your_key" prediction-agent
```

## Vercel/Railway/Heroku Deployment

For alternative hosting platforms, ensure:

1. Python 3.9+ is available
2. Environment variables are set
3. Port 8501 is exposed

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: API Key Not Found

**Solution:** 
- For local: Create `.env` file with `OPENAI_API_KEY`
- For Streamlit Cloud: Add secret in app settings
- For Docker: Pass as environment variable with `-e`

### Issue: Port Already in Use

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Connection Timeout

**Solution:** Check your internet connection and firewall settings. Ensure the OpenAI API is accessible.

## Monitoring and Logs

### Streamlit Cloud Logs
- Go to your app's settings
- Click **Logs** to view deployment and runtime logs

### Local Development Logs
- Streamlit outputs logs to the console
- Check for errors and warnings

## Performance Optimization

1. **Caching**: Use `@st.cache_data` for expensive operations
2. **Lazy Loading**: Load modules on demand
3. **Session State**: Minimize state size
4. **API Calls**: Implement request batching

## Security Best Practices

1. Never commit `.env` files
2. Use Streamlit Secrets for sensitive data
3. Validate user inputs
4. Keep dependencies updated
5. Use HTTPS for all connections

## Updating the App

1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub
4. Streamlit Cloud auto-deploys on push
5. Monitor logs for any issues

## Support

For issues with:
- **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io)
- **LangGraph**: [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- **OpenAI**: [OpenAI API Documentation](https://platform.openai.com/docs)
