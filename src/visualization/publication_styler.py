"""Journal-grade publication figure styling for IEEE / ACM / Elsevier Q1 venues."""
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

def set_publication_style(is_double_column: bool = False, font_family: str = "serif"):
    """Apply IEEE/Nature publication styling to matplotlib rcParams.
    
    Args:
        is_double_column (bool): True for 7.0-inch width (full page), False for 3.5-inch width (single column).
        font_family (str): Default font family, 'serif' or 'sans-serif'.
    """
    width = 7.0 if is_double_column else 3.5
    height = width * 0.72

    plt.rcParams.update({
        "figure.figsize": (width, height),
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "font.family": font_family,
        "font.serif": ["Times New Roman", "DejaVu Serif", "Liberation Serif", "serif"],
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "lines.linewidth": 1.2,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
        "figure.autolayout": True,
        "pdf.fonttype": 42,
        "ps.fonttype": 42
    })
    sns.set_palette("colorblind")

def save_publication_figure(fig, output_path_without_ext: str | Path, dpi: int = 300):
    """Save figure simultaneously in vector PDF format and high-res PNG preview.
    
    Args:
        fig: Matplotlib figure object.
        output_path_without_ext: Base path (without extension) for output files.
        dpi: Dots per inch resolution.
    """
    base = Path(output_path_without_ext)
    base.parent.mkdir(parents=True, exist_ok=True)
    
    pdf_path = base.with_suffix(".pdf")
    png_path = base.with_suffix(".png")

    fig.savefig(pdf_path, dpi=dpi, bbox_inches="tight")
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight")
    print(f"📊 Publication figures saved: {pdf_path.name} & {png_path.name}")
