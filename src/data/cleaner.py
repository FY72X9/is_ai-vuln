"""Data Cleaning & Decontamination Pipeline.
Addresses known anomalies in intrusion datasets (e.g., CICIDS2017 issues documented by Engelen et al. 2021 and Lanvin et al. 2022).
"""
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Tuple, Optional

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Strip extraneous whitespace and special characters from DataFrame column headers."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('/', '_per_').str.lower()
    return df

def decontaminate_cicids2017(df: pd.DataFrame, drop_duplicates: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Clean and decontaminate CICIDS2017 dataset according to SPW 2021 and TIFS 2022 findings.

    Removes:
      - Duplicate network flows (which inflate evaluation metrics)
      - Infinite and NaN float values in flow throughput metrics
      - Zero-variance / constant features
    Harmonizes:
      - Binary and multi-class label mappings
    """
    initial_rows = len(df)
    initial_cols = len(df.columns)
    
    df_clean = clean_column_names(df)
    
    # Identify label column
    label_col = None
    for candidate in ["label", "attack", "class"]:
        if candidate in df_clean.columns:
            label_col = candidate
            break

    # 1. Replace inf and -inf with NaN
    df_clean = df_clean.replace([np.inf, -np.inf], np.nan)
    
    # 2. Count & impute or drop NaN values
    nan_rows_before = df_clean.isna().any(axis=1).sum()
    # Drop rows with NaN if label is missing, otherwise median impute numerical columns
    if label_col and df_clean[label_col].isna().any():
        df_clean = df_clean.dropna(subset=[label_col])
    
    num_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if df_clean[col].isna().any():
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(0.0 if np.isnan(median_val) else median_val)
            
    # 3. Drop duplicate flows
    dup_rows = 0
    if drop_duplicates:
        dup_rows = df_clean.duplicated().sum()
        df_clean = df_clean.drop_duplicates()
        
    # 4. Remove zero-variance (constant) features
    constant_cols = []
    for col in num_cols:
        if col in df_clean.columns and df_clean[col].std() == 0:
            constant_cols.append(col)
    if constant_cols:
        df_clean = df_clean.drop(columns=constant_cols)

    # 5. Label Harmonization
    if label_col:
        # Standardize benign label
        df_clean["is_attack"] = (~df_clean[label_col].astype(str).str.strip().str.upper().isin(["BENIGN", "0", "NORMAL"])).astype(int)

    final_rows = len(df_clean)
    final_cols = len(df_clean.columns)

    stats = {
        "initial_rows": initial_rows,
        "final_rows": final_rows,
        "dropped_duplicates": int(dup_rows),
        "imputed_nan_rows": int(nan_rows_before),
        "removed_constant_cols": constant_cols,
        "initial_cols": initial_cols,
        "final_cols": final_cols,
    }

    print(f"🧹 Decontamination complete: {initial_rows} -> {final_rows} rows (-{dup_rows} dups, {nan_rows_before} NaNs handled).")
    return df_clean, stats

def clean_dataset(df: pd.DataFrame, dataset_name: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Universal cleaning dispatcher for benchmark datasets."""
    name = dataset_name.upper()
    if "CICIDS" in name or "CIC-IDS" in name:
        return decontaminate_cicids2017(df)
    else:
        # Standard generic decontamination
        initial_rows = len(df)
        df_clean = clean_column_names(df)
        df_clean = df_clean.replace([np.inf, -np.inf], np.nan)
        df_clean = df_clean.dropna()
        df_clean = df_clean.drop_duplicates()
        stats = {
            "initial_rows": initial_rows,
            "final_rows": len(df_clean),
            "removed_rows": initial_rows - len(df_clean)
        }
        return df_clean, stats
