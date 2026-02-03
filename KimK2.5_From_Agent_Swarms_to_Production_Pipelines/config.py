import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # OpenRouter Settings
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    PREFERRED_PROVIDER = os.getenv("PREFERRED_PROVIDER", "")

    # Site info for OpenRouter rankings
    SITE_URL = os.getenv("SITE_URL", "https://localhost")
    SITE_NAME = os.getenv("SITE_NAME", "VideoDocsConverter")

    # OpenRouter Model IDs
    MODEL_INSTANT = "moonshotai/kimi-k2.5"
    MODEL_THINKING = "moonshotai/kimi-k2.5"

    # Video processing
    FRAME_INTERVAL_SECONDS = 10
    MAX_FRAMES = 15

    # Model parameters
    ANALYSIS_TEMPERATURE = 0.3
    CODE_GENERATION_TEMPERATURE = 0.2
    DOCUMENTATION_TEMPERATURE = 0.4
    MAX_TOKENS = 4096
    DOC_MAX_TOKENS = 8000
    SUMMARY_MAX_TOKENS = 2000
    QA_MAX_TOKENS = 1500

    # Cost estimation (USD per 1M tokens). Update if pricing changes.
    COST_PER_M_INPUT = float(os.getenv("COST_PER_M_INPUT", "0.60"))
    COST_PER_M_OUTPUT = float(os.getenv("COST_PER_M_OUTPUT", "0.60"))

    # Provider routing (optional)
    ENABLE_PROVIDER_ROUTING = bool(PREFERRED_PROVIDER)

    @classmethod
    def get_extra_headers(cls):
        return {
            "HTTP-Referer": cls.SITE_URL,
            "X-Title": cls.SITE_NAME,
        }

    @classmethod
    def get_provider_config(cls):
        if cls.ENABLE_PROVIDER_ROUTING and cls.PREFERRED_PROVIDER:
            return {
                "provider": {
                    "order": [cls.PREFERRED_PROVIDER],
                    "allow_fallbacks": True,
                }
            }
        return {}
