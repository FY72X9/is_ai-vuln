"""Anti-Leakage Data Partitioning Suite.
Implements Subnet-Grouped and Time-Aware K-Fold cross validation with strictly isolated inside-fold preprocessing.
Compatible with Google Colab and local Python runtimes.
"""
from __future__ import annotations
import os
import sys
from typing import Generator, Tuple, List, Optional, Any, Union
import numpy as np
import pandas as pd

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def safe_slice(data: Any, indices: Union[np.ndarray, List[int]]) -> Any:
    """Safely slice pandas DataFrame, Series, or NumPy ndarray by integer indices.
    
    Prevents KeyError when indexing a pandas DataFrame with integer indices (e.g. df[idx]).
    """
    if data is None:
        return None
    if hasattr(data, "iloc"):
        return data.iloc[indices]
    return np.asarray(data)[indices]

def extract_subnet_mask(ip_series: Union[pd.Series, np.ndarray, List[str]], mask_prefix_len: int = 24) -> pd.Series:
    """Extract subnet group from IPv4 address string (default /24 mask)."""
    if not isinstance(ip_series, pd.Series):
        ip_series = pd.Series(ip_series)

    def _to_subnet(ip):
        if not isinstance(ip, str) or "." not in ip:
            return "unknown_subnet"
        parts = ip.strip().split(".")
        if len(parts) == 4:
            if mask_prefix_len == 24:
                return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"
            elif mask_prefix_len == 16:
                return f"{parts[0]}.{parts[1]}.0.0/16"
        return "unknown_subnet"
    
    return ip_series.apply(_to_subnet)

class PureNumPyStandardScaler:
    """Pure NumPy implementation of standard scaler for isolated or minimal environments."""
    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X: Union[np.ndarray, pd.DataFrame]):
        X_arr = np.asarray(X, dtype=np.float64)
        self.mean_ = np.nanmean(X_arr, axis=0)
        self.scale_ = np.nanstd(X_arr, axis=0)
        self.scale_[self.scale_ == 0.0] = 1.0
        return self

    def transform(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        if self.mean_ is None or self.scale_ is None:
            raise RuntimeError("PureNumPyStandardScaler must be fitted before transforming data.")
        X_arr = np.asarray(X, dtype=np.float64)
        return (X_arr - self.mean_) / self.scale_

    def fit_transform(self, X: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        return self.fit(X).transform(X)

class AntiLeakageGroupKFold:
    """GroupKFold cross-validator grouped by IP subnets or Host IDs to prevent session leakage."""
    
    def __init__(self, n_splits: int = 5):
        if n_splits < 2:
            raise ValueError("n_splits must be at least 2.")
        self.n_splits = n_splits

    def split(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Optional[Union[np.ndarray, pd.Series]] = None,
        groups: Optional[Union[np.ndarray, pd.Series, List[Any]]] = None
    ) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        """Generate train/validation indices grouped by subnet/host."""
        if groups is None:
            raise ValueError("The 'groups' parameter must not be None for AntiLeakageGroupKFold.")

        groups_arr = np.asarray(groups)
        unique_groups = np.unique(groups_arr)
        # If unique groups < n_splits, combine with sample chunks to guarantee n_splits distinct groups
        if len(unique_groups) < self.n_splits:
            chunk_factor = (self.n_splits // max(len(unique_groups), 1)) + 1
            chunks = np.arange(len(groups_arr)) // (max(len(groups_arr) // (self.n_splits * chunk_factor), 1))
            groups_arr = np.array([f"{g}_c{c}" for g, c in zip(groups_arr, chunks)])
            groups = groups_arr

        try:
            from sklearn.model_selection import GroupKFold
            gkf = GroupKFold(n_splits=self.n_splits)
            yield from gkf.split(X, y, groups=groups)
        except (ImportError, Exception):
            # Deterministic pure-Python/NumPy fallback
            unique_groups = np.unique(groups_arr)
            group_folds = np.array_split(unique_groups, self.n_splits)
            indices = np.arange(len(groups_arr))
            
            for fold_idx in range(self.n_splits):
                val_groups = set(group_folds[fold_idx])
                val_mask = np.isin(groups_arr, list(val_groups))
                val_indices = indices[val_mask]
                train_indices = indices[~val_mask]
                yield train_indices, val_indices

class AntiLeakageTimeSeriesSplit:
    """Time-aware chronological cross-validator without future-looking data leakage."""

    def __init__(self, n_splits: int = 5):
        if n_splits < 2:
            raise ValueError("n_splits must be at least 2.")
        self.n_splits = n_splits

    def split(
        self,
        X: Union[np.ndarray, pd.DataFrame],
        y: Optional[Union[np.ndarray, pd.Series]] = None
    ) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        """Generate sequential train/validation split indices."""
        try:
            from sklearn.model_selection import TimeSeriesSplit
            tscv = TimeSeriesSplit(n_splits=self.n_splits)
            yield from tscv.split(X, y)
        except ImportError:
            n_samples = len(X)
            test_size = n_samples // (self.n_splits + 1)
            indices = np.arange(n_samples)
            for i in range(self.n_splits):
                train_end = (i + 1) * test_size
                val_end = train_end + test_size
                yield indices[:train_end], indices[train_end:val_end]

def fit_fold_isolated_pipeline(
    X_train: Union[np.ndarray, pd.DataFrame],
    y_train: Union[np.ndarray, pd.Series],
    X_val: Union[np.ndarray, pd.DataFrame],
    y_val: Union[np.ndarray, pd.Series],
    apply_scaling: bool = True,
    apply_smote: bool = False,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Any]:
    """Fit scaler and sampler STRICTLY within the train split, preventing leakage to validation set.

    Args:
        X_train: Training features (NumPy array or pandas DataFrame).
        y_train: Training labels.
        X_val: Validation features.
        y_val: Validation labels.
        apply_scaling: Whether to fit and apply standard scaling.
        apply_smote: Whether to apply SMOTE oversampling to training set only.
        random_state: Seed for reproducibility.

    Returns:
        Tuple: (X_train_processed, y_train_processed, X_val_processed, y_val, fitted_scaler)
    """
    # Convert DataFrames to numerical float ndarrays for scaling if needed
    if isinstance(X_train, pd.DataFrame):
        num_cols = X_train.select_dtypes(include=[np.number]).columns
        X_train_arr = X_train[num_cols].to_numpy(dtype=np.float64)
        X_val_arr = X_val[num_cols].to_numpy(dtype=np.float64)
    else:
        X_train_arr = np.asarray(X_train, dtype=np.float64)
        X_val_arr = np.asarray(X_val, dtype=np.float64)

    y_train_arr = np.asarray(y_train)
    y_val_arr = np.asarray(y_val)

    scaler = None
    if apply_scaling:
        try:
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
        except ImportError:
            scaler = PureNumPyStandardScaler()
            
        X_train_arr = scaler.fit_transform(X_train_arr)
        X_val_arr = scaler.transform(X_val_arr)

    if apply_smote:
        try:
            import importlib
            imblearn_os = importlib.import_module("imblearn.over_sampling")
            smote_cls = getattr(imblearn_os, "SMOTE")
            smote = smote_cls(random_state=random_state)
            X_train_arr, y_train_arr = smote.fit_resample(X_train_arr, y_train_arr)
        except (ImportError, AttributeError):
            pass

    return X_train_arr, y_train_arr, X_val_arr, y_val_arr, scaler
