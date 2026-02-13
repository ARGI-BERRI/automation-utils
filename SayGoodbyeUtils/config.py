from dataclasses import dataclass
from pathlib import Path


@dataclass
class SGUConfig:
    """Config for SayGoodbyeUtils package."""

    pwd: Path = Path(__file__).parent
    logs_dir: Path = pwd / "logs"
