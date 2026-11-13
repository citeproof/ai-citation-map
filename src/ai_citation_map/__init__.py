"""Turn a CSV of URLs cited in AI answers into a ranked list of domains."""
from .core import build_map, domain_of

__all__ = ["build_map", "domain_of"]
__version__ = "0.1.0"
