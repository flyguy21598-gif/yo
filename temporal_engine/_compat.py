from __future__ import annotations

try:  # pragma: no cover - exercised when real dependencies exist
    import networkx as nx  # type: ignore
except ImportError:  # pragma: no cover - exercised in constrained environments
    from temporal_engine.vendor import networkx_stub as nx

try:  # pragma: no cover - exercised when real dependencies exist
    import numpy as np  # type: ignore
except ImportError:  # pragma: no cover - exercised in constrained environments
    from temporal_engine.vendor import numpy_stub as np

__all__ = ["nx", "np"]
