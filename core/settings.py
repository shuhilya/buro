from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings

__all__ = ["Settings", "settings"]

_env_settings_file = ".env.example"


class LogSettings(BaseSettings):
    path: Path

    class Config:
        env_file = _env_settings_file
        env_prefix = "LOG_"


class Settings(BaseSettings):
    logs: LogSettings

    class Config:
        env_file = _env_settings_file


@lru_cache()
def settings() -> Settings:
    res = Settings(logs=LogSettings())
    res.logs.path.mkdir(parents=True, exist_ok=True)

    return res
