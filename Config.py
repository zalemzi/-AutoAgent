"""
Configuration centralisée d'AutoAgent
Gère les variables d'environnement et les paramètres globaux
"""

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AutoAgent"
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    VERSION: str = "1.0.0"
    
    # Clés API IA
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    
    # Modèles IA
    OPENAI_MODEL: str = "gpt-4-turbo"
    CLAUDE_MODEL: str = "claude-3-opus-20240229"
    GEMINI_MODEL: str = "gemini-pro"
    
    # Configuration agents
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.7
    
    # URLs et endpoints
    API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8000")
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Timeouts
    API_TIMEOUT: int = 30
    
    class Config:
        env_file = ".env"

# Instance globale
settings = Settings()
