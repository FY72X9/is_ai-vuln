"""Automated LaTeX Table Generation for Q1 Journal Publication.
Generates professional IEEE / Elsevier formatted booktabs tables with bold maxima.
"""
import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Optional

def export_benchmark_to_latex(
    df: pd.DataFrame,
    output_filepath: str | Path,
    caption: str = "Benchmark Evaluation Across Multi-Paradigm IDS Architectures",
    label: str = "tab:benchmark_results",
    bold_cols: Optional[List[str]] = None
) -> str:
    """Format DataFrame into publication-grade LaTeX table with booktabs."""
    df_out = df.copy()
    
    if bold_cols:
        for col in bold_cols:
            if col in df_out.columns:
                try:
                    # Attempt to highlight maximum numerical value
                    vals = pd.to_numeric(df_out[col].astype(str).str.extract(r"([\d\.]+)")[0], errors='coerce')
                    max_idx = vals.idxmax()
                    df_out.loc[max_idx, col] = f"\\textbf{{{df_out.loc[max_idx, col]}}}"
                except Exception:
                    pass

    latex_code = df_out.to_latex(
        index=False,
        escape=False,
        column_format="l" + "c" * (len(df_out.columns) - 1)
    )

    # Wrap in table environment with caption and label
    full_latex = f"""\\begin{{table*}}[t]
\\centering
\\caption{{{caption}}}
\\label{{{label}}}
\\small
{latex_code}
\\end{{table*}}
"""
    out_path = Path(output_filepath)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_latex)

    print(f"📄 LaTeX table successfully written to: {out_path}")
    return full_latex
