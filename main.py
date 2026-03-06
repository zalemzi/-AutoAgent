"""
AutoAgent - Bot d'automatisation IA multifonctionnel
Point d'entrée principal du système
"""

import os
import sys
import asyncio
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from uvicorn import run

# Configuration
load_dotenv()
from config import settings
from api.routes import router
from utils.logger import setup_logger

# Setup logging
logger = setup_logger(__name__)

# Créer l'application FastAPI
app = FastAPI(
    title="AutoAgent API",
    description="Bot d'automatisation IA avec support multi-modèles",
    version="1.0.0"
)

# Inclure les routes
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 AutoAgent démarré avec succès")
    logger.info(f"OpenAI disponible: {bool(settings.OPENAI_API_KEY)}")
    logger.info(f"Claude disponible: {bool(settings.ANTHROPIC_API_KEY)}")
    logger.info(f"Gemini disponible: {bool(settings.GOOGLE_API_KEY)}")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 AutoAgent arrêté")

@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur AutoAgent",
        "version": "1.0.0",
        "description": "Bot d'automatisation IA multifonctionnel",
        "endpoints": {
            "docs": "/docs",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "ai_models": {
            "openai": bool(settings.OPENAI_API_KEY),
            "claude": bool(settings.ANTHROPIC_API_KEY),
            "gemini": bool(settings.GOOGLE_API_KEY)
        }
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=settings.DEBUG
    )
