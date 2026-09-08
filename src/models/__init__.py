"""Models package for benchmark architectures (Foundation, SSM, GNN, Transformer, GBDT)."""
from typing import Dict, Any, Type

from src.models.base import BaseIDSModel
from src.models.classical import XGBoostIDS, LightGBMIDS
from src.models.foundation import TabPFNIDS, TabICLIDS
from src.models.deep_tabular import MambularSSMIDS, FTTransformerIDS, SAINTIDS
from src.models.graph_ids import GraphIDSModel

MODEL_REGISTRY: Dict[str, Type[BaseIDSModel]] = {
    "xgboost": XGBoostIDS,
    "lightgbm": LightGBMIDS,
    "tabpfn_v3": TabPFNIDS,
    "tabpfn": TabPFNIDS,
    "tabicl_v2": TabICLIDS,
    "tabicl": TabICLIDS,
    "mambular_ssm": MambularSSMIDS,
    "mambular": MambularSSMIDS,
    "ft_transformer": FTTransformerIDS,
    "fttransformer": FTTransformerIDS,
    "saint": SAINTIDS,
    "graphids": GraphIDSModel,
}

def get_model(model_name: str, **kwargs) -> BaseIDSModel:
    """Instantiate a benchmark IDS model by name."""
    key = model_name.strip().lower()
    if key not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model '{model_name}'. Available architectures: {list(MODEL_REGISTRY.keys())}"
        )
    return MODEL_REGISTRY[key](**kwargs)

__all__ = [
    "BaseIDSModel",
    "XGBoostIDS",
    "LightGBMIDS",
    "TabPFNIDS",
    "TabICLIDS",
    "MambularSSMIDS",
    "FTTransformerIDS",
    "SAINTIDS",
    "GraphIDSModel",
    "get_model",
    "MODEL_REGISTRY"
]
