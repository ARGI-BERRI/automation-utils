from dataclasses import dataclass
from pathlib import Path


@dataclass
class SHUConfig:
    """Config for SayHelloUtils package."""

    pwd: Path = Path(__file__).parent
    logs_dir: Path = pwd / "logs"
