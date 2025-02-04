import configparser
from typing import Any, Dict, Optional

config: Optional[Dict[str, Any]] = None


def getenv(key: str) -> Any:
    global config
    if config is None:
        config = configparser.ConfigParser()
        config.read(".env")
    return config["DEFAULT"].get(key)
