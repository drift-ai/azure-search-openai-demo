import os

from app import create_app
from load_azd_env import load_azd_env

# WEBSITE_HOSTNAME is always set by App Service, RUNNING_IN_PRODUCTION is set in main.bicep
RUNNING_ON_AZURE = os.getenv("WEBSITE_HOSTNAME") is not None or os.getenv("RUNNING_IN_PRODUCTION") is not None

if not RUNNING_ON_AZURE:
    try:
        load_azd_env()
    except Exception as e:
        print(f"Warning: Could not load Azure environment variables: {e}")
        print("Running in local development mode without Azure services...")
        
        # Set minimal environment variables for local development
        os.environ.setdefault("AUTH_TYPE", "None")
        os.environ.setdefault("USE_VECTORS", "false")
        os.environ.setdefault("OPENAI_HOST", "local")
        os.environ.setdefault("OPENAI_BASE_URL", "http://localhost:8080/v1")
        os.environ.setdefault("AZURE_OPENAI_CHATGPT_MODEL", "local-model")
        
        # Set required Azure environment variables to dummy values for local development
        os.environ.setdefault("AZURE_STORAGE_ACCOUNT", "dummy")
        os.environ.setdefault("AZURE_STORAGE_KEY", "dummy")
        os.environ.setdefault("AZURE_STORAGE_CONTAINER", "dummy")
        os.environ.setdefault("AZURE_OPENAI_ENDPOINT", "https://dummy.openai.azure.com/")
        os.environ.setdefault("AZURE_OPENAI_API_KEY", "dummy")
        os.environ.setdefault("AZURE_OPENAI_CHATGPT_DEPLOYMENT", "dummy")
        os.environ.setdefault("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "dummy")
        os.environ.setdefault("AZURE_SEARCH_SERVICE", "dummy")
        os.environ.setdefault("AZURE_SEARCH_INDEX", "dummy")
        os.environ.setdefault("AZURE_SEARCH_KEY", "dummy")
        os.environ.setdefault("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

app = create_app()
