from __future__ import annotations

import importlib.util

if importlib.util.find_spec("networkx") is not None:
    import networkx as nx  # type: ignore
else:
    from temporal_engine.vendor import networkx_stub as nx

if importlib.util.find_spec("numpy") is not None:
    import numpy as np  # type: ignore
else:
    from temporal_engine.vendor import numpy_stub as np

__all__ = ["nx", "np"]
