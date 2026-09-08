"""Classical Gradient Boosted Decision Tree (GBDT) Baselines.
Implements XGBoost and LightGBM with Optuna hyperparameter optimization.
"""
import os
import sys
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.models.base import BaseIDSModel

class XGBoostIDS(BaseIDSModel):
    """XGBoost Classifier Baseline with Optuna Tuning and Hist/GPU acceleration."""

    def __init__(self, random_state: int = 42, optuna_trials: int = 0, **kwargs):
        super().__init__(name="XGBoost", task_profile="T1", random_state=random_state, **kwargs)
        self.optuna_trials = optuna_trials
        self.best_params = {
            "n_estimators": 150,
            "max_depth": 6,
            "learning_rate": 0.08,
            "subsample": 0.85,
            "colsample_bytree": 0.85,
            "tree_method": "hist",
            "random_state": random_state,
            "n_jobs": -1,
            "eval_metric": "logloss"
        }

    def _tune_with_optuna(self, X_train: np.ndarray, y_train: np.ndarray) -> Dict[str, Any]:
        try:
            import optuna
            from xgboost import XGBClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import f1_score
            
            # Use small validation subset for fast tuning
            X_tr, X_val, y_tr, y_val = train_test_split(
                X_train, y_train, test_size=0.2, random_state=self.random_state, stratify=y_train
            )
            
            def objective(trial):
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 80, 250),
                    "max_depth": trial.suggest_int("max_depth", 3, 9),
                    "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2, log=True),
                    "subsample": trial.suggest_float("subsample", 0.6, 1.0),
                    "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
                    "tree_method": "hist",
                    "random_state": self.random_state,
                    "n_jobs": -1,
                    "eval_metric": "logloss"
                }
                clf = XGBClassifier(**params)
                clf.fit(X_tr, y_tr)
                preds = clf.predict(X_val)
                return f1_score(y_val, preds, average="macro")

            optuna.logging.set_verbosity(optuna.logging.WARNING)
            study = optuna.create_study(direction="maximize")
            study.optimize(objective, n_trials=self.optuna_trials, timeout=60)
            print(f"🎯 Optuna tuned XGBoost: Best Macro F1 = {study.best_value:.4f}")
            return study.best_params
        except ImportError:
            print("ℹ️ Optuna not installed; using standard tuned parameters.")
            return {}

    def fit(self, X: np.ndarray, y: np.ndarray, **kwargs) -> "XGBoostIDS":
        try:
            from xgboost import XGBClassifier
            
            params = dict(self.best_params)
            if self.optuna_trials > 0:
                tuned = self._tune_with_optuna(X, y)
                params.update(tuned)
            params.update(self.params)
            
            # Check for GPU
            try:
                import torch
                if torch.cuda.is_available():
                    params["device"] = "cuda"
            except ImportError:
                pass
                
            self.model = XGBClassifier(**params)
            self.model.fit(X, y)
            self.is_fitted = True
            return self
        except ImportError:
            # Fallback to sklearn GradientBoostingClassifier if xgboost not available
            from sklearn.ensemble import HistGradientBoostingClassifier
            print("ℹ️ xgboost not available; falling back to HistGradientBoostingClassifier.")
            self.model = HistGradientBoostingClassifier(random_state=self.random_state)
            self.model.fit(X, y)
            self.is_fitted = True
            return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError(f"Model {self.name} is not fitted.")
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError(f"Model {self.name} is not fitted.")
        return self.model.predict_proba(X)


class LightGBMIDS(BaseIDSModel):
    """LightGBM Classifier Baseline with Histogram Gradient Optimization."""

    def __init__(self, random_state: int = 42, optuna_trials: int = 0, **kwargs):
        super().__init__(name="LightGBM", task_profile="T1", random_state=random_state, **kwargs)
        self.optuna_trials = optuna_trials
        self.best_params = {
            "n_estimators": 150,
            "max_depth": -1,
            "num_leaves": 31,
            "learning_rate": 0.08,
            "subsample": 0.85,
            "random_state": random_state,
            "n_jobs": -1,
            "verbose": -1
        }

    def _tune_with_optuna(self, X_train: np.ndarray, y_train: np.ndarray) -> Dict[str, Any]:
        try:
            import optuna
            from lightgbm import LGBMClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import f1_score

            X_tr, X_val, y_tr, y_val = train_test_split(
                X_train, y_train, test_size=0.2, random_state=self.random_state, stratify=y_train
            )

            def objective(trial):
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 80, 250),
                    "num_leaves": trial.suggest_int("num_leaves", 15, 63),
                    "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2, log=True),
                    "subsample": trial.suggest_float("subsample", 0.6, 1.0),
                    "random_state": self.random_state,
                    "n_jobs": -1,
                    "verbose": -1
                }
                clf = LGBMClassifier(**params)
                clf.fit(X_tr, y_tr)
                preds = clf.predict(X_val)
                return f1_score(y_val, preds, average="macro")

            optuna.logging.set_verbosity(optuna.logging.WARNING)
            study = optuna.create_study(direction="maximize")
            study.optimize(objective, n_trials=self.optuna_trials, timeout=60)
            print(f"🎯 Optuna tuned LightGBM: Best Macro F1 = {study.best_value:.4f}")
            return study.best_params
        except ImportError:
            return {}

    def fit(self, X: np.ndarray, y: np.ndarray, **kwargs) -> "LightGBMIDS":
        try:
            from lightgbm import LGBMClassifier
            params = dict(self.best_params)
            if self.optuna_trials > 0:
                tuned = self._tune_with_optuna(X, y)
                params.update(tuned)
            params.update(self.params)
            
            self.model = LGBMClassifier(**params)
            self.model.fit(X, y)
            self.is_fitted = True
            return self
        except ImportError:
            from sklearn.ensemble import HistGradientBoostingClassifier
            print("ℹ️ lightgbm not available; falling back to HistGradientBoostingClassifier.")
            self.model = HistGradientBoostingClassifier(random_state=self.random_state)
            self.model.fit(X, y)
            self.is_fitted = True
            return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError(f"Model {self.name} is not fitted.")
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError(f"Model {self.name} is not fitted.")
        return self.model.predict_proba(X)
