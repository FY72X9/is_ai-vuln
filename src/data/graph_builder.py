"""Graph Construction Engine for GraphIDS.
Converts tabular NetFlow records into topological bipartite/multigraph structures.
"""
import os
import sys
import numpy as np
import pandas as pd
import networkx as nx
from typing import Dict, Any, Tuple, Optional

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def build_networkx_flow_graph(
    df: pd.DataFrame,
    src_ip_col: str = "src_ip",
    dst_ip_col: str = "dst_ip",
    feature_cols: Optional[list] = None,
    label_col: str = "is_attack"
) -> nx.DiGraph:
    """Construct a directed network interaction graph from NetFlow DataFrame.

    Args:
        df: Input NetFlow tabular dataframe.
        src_ip_col: Name of source IP column.
        dst_ip_col: Name of destination IP column.
        feature_cols: Numerical columns to attach as edge attributes.
        label_col: Column indicating attack presence.

    Returns:
        nx.DiGraph: Attributed directed graph.
    """
    G = nx.DiGraph()

    # Identify existing columns
    cols = df.columns.tolist()
    src_col = src_ip_col if src_ip_col in cols else None
    dst_col = dst_ip_col if dst_ip_col in cols else None

    # Fallback to simulated IP addresses if not present in preprocessed statistical datasets
    if not src_col or not dst_col:
        # Generate pseudo topological endpoints for testing / datasets without raw IPs
        print("ℹ️ Source/Destination IP columns not found. Generating bipartite topology mapping...")
        df = df.copy()
        df["_src_node"] = [f"host_{(i % 50)}" for i in range(len(df))]
        df["_dst_node"] = [f"server_{(i % 10)}" for i in range(len(df))]
        src_col, dst_col = "_src_node", "_dst_node"

    if feature_cols is None:
        feature_cols = [c for c in df.select_dtypes(include=[np.number]).columns if c not in [label_col, "label"]]

    for _, row in df.iterrows():
        u = str(row[src_col])
        v = str(row[dst_col])
        edge_attrs = {col: float(row[col]) for col in feature_cols if col in row}
        if label_col in row:
            edge_attrs["label"] = int(row[label_col])
        G.add_edge(u, v, **edge_attrs)

    print(f"🕸️ Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G

def export_to_pyg_tensors(G: nx.DiGraph) -> Dict[str, Any]:
    """Convert NetworkX flow graph to edge index and feature arrays (PyG compatible)."""
    nodes = sorted(list(G.nodes()))
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    edge_list = []
    edge_features = []
    edge_labels = []

    for u, v, data in G.edges(data=True):
        edge_list.append([node_to_idx[u], node_to_idx[v]])
        feat = [v_ for k_, v_ in data.items() if k_ != "label"]
        edge_features.append(feat)
        edge_labels.append(data.get("label", 0))

    edge_index = np.array(edge_list, dtype=np.int64).T if edge_list else np.empty((2, 0), dtype=np.int64)
    edge_attr = np.array(edge_features, dtype=np.float32) if edge_features else np.empty((0, 0), dtype=np.float32)
    edge_y = np.array(edge_labels, dtype=np.int64) if edge_labels else np.empty((0,), dtype=np.int64)

    return {
        "num_nodes": len(nodes),
        "node_mapping": node_to_idx,
        "edge_index": edge_index,
        "edge_attr": edge_attr,
        "edge_y": edge_y
    }
