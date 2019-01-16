"""Configurations Module for the Questioner REST API."""
import os

class Config():
    """Base Configurations Class."""
    DEBUG = False

class DevelopmentConfig(Config):
    """Development Phase Configurations Class."""
    DEBUG = True

class TestingConfig(Config):
    """Testing Phase Configurations Class."""
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """Production Phase Configurations Class."""
    DEBUG = False
    TESTING = False

APP_CONFIG = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
