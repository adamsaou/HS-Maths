import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from fractions import Fraction

plt.rcParams["font.size"] = 11

pdf_path = "Trigonometrie_dessins.pdf"

# ---------- Page 1: full cercle trigonometrique ----------
points = [
    (0, "0", "(1, 0)"),
    (np.pi/6, "π/6", "(√3/2, 1/2)"),
    (np.pi/4, "π/4", "(√2/2, √2/2)"),
    (np.pi/3, "π/3", "(1/2, √3/2)"),
    (np.pi/2, "π/2", "(0, 1)"),
    (2*np.pi/3, "2π/3", "(-1/2, √3/2)"),
    (3*np.pi/4, "3π/4", "(-√2/2, √2/2)"),
    (5*np.pi/6, "5π/6", "(-√3/2, 1/2)"),
    (np.pi, "π", "(-1, 0)"),
    (7*np.pi/6, "7π/6", "(-√3/2, -1/2)"),
    (5*np.pi/4, "5π/4", "(-√2/2, -√2/2)"),
    (4*np.pi/3, "4π/3", "(-1/2, -√3/2)"),
    (3*np.pi/2, "3π/2", "(0, -1)"),
    (5*np.pi/3, "5π/3", "(1/2, -√3/2)"),
    (7*np.pi/4, "7π/4", "(√2/2, -√2/2)"),
    (11*np.pi/6, "11π/6", "(√3/2, -1/2)"),
]

with PdfPages(pdf_path) as pdf:

    fig, ax = plt.subplots(figsize=(9, 9))
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color="black", lw=1.5)
    ax.axhline(0, color="black", lw=1)
    ax.axvline(0, color="black", lw=1)
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Cercle trigonométrique — angles remarquables", fontsize=15, fontweight="bold")

    for ang, label, coord in points:
        x, y = np.cos(ang), np.sin(ang)
        ax.plot([0, x], [0, y], color="gray", lw=0.6, ls="--")
        ax.plot([x], [y], "o", color="black", ms=5)
        # push label outward
        lx, ly = 1.28*np.cos(ang), 1.28*np.sin(ang)
        ax.text(lx, ly, label, ha="center", va="center", fontsize=12, fontweight="bold", color="darkred")
        # coordinate near the point, pushed slightly further out than the dot
        cx, cy = 1.12*np.cos(ang), 1.12*np.sin(ang)
        ax.text(cx, cy, coord, ha="center", va="center", fontsize=8)

    pdf.savefig(fig); plt.close(fig)

    # ---------- Page 2: angles associes, 5 panels (2x3 grid, 1 empty) ----------
    fig, axes = plt.subplots(2, 3, figsize=(13, 9))
    x_demo = np.pi/5  # a generic angle to illustrate, not a remarkable one on purpose

    configs = [
        ("Opposé : -x", x_demo, -x_demo, "cos(-x)=cos(x)\nsin(-x)=-sin(x)"),
        ("Supplémentaire : π-x", x_demo, np.pi - x_demo, "cos(π-x)=-cos(x)\nsin(π-x)=sin(x)"),
        ("Anti-suppl. : π+x", x_demo, np.pi + x_demo, "cos(π+x)=-cos(x)\nsin(π+x)=-sin(x)"),
        ("Complémentaire : π/2-x", x_demo, np.pi/2 - x_demo, "cos(π/2-x)=sin(x)\nsin(π/2-x)=cos(x)"),
        ("π/2+x", x_demo, np.pi/2 + x_demo, "cos(π/2+x)=-sin(x)\nsin(π/2+x)=cos(x)"),
    ]

    axes.flat[-1].axis("off")  # 6th cell unused, hide it

    for ax, (title, a1, a2, formula) in zip(axes.flat, configs):
        theta = np.linspace(0, 2*np.pi, 300)
        ax.plot(np.cos(theta), np.sin(theta), color="black", lw=1.2)
        ax.axhline(0, color="black", lw=0.8)
        ax.axvline(0, color="black", lw=0.8)
        ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=12, fontweight="bold")

        x1, y1 = np.cos(a1), np.sin(a1)
        x2, y2 = np.cos(a2), np.sin(a2)
        ax.plot([0, x1], [0, y1], color="tab:blue", lw=2)
        ax.plot([0, x2], [0, y2], color="tab:red", lw=2)
        ax.plot([x1], [y1], "o", color="tab:blue", ms=6)
        ax.plot([x2], [y2], "o", color="tab:red", ms=6)
        ax.text(x1*1.2, y1*1.2, "x", color="tab:blue", fontsize=12, fontweight="bold", ha="center")
        ax.text(x2*1.2, y2*1.2, "x'", color="tab:red", fontsize=12, fontweight="bold", ha="center")
        ax.text(0, -1.3, formula, ha="center", va="center", fontsize=9)

    fig.suptitle("Angles associés — visualisation par symétrie", fontsize=14, fontweight="bold", y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    pdf.savefig(fig); plt.close(fig)

    # ---------- Page 3: table of valeurs remarquables ----------
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.axis("off")
    ax.set_title("Valeurs remarquables — à connaître par cœur", fontsize=15, fontweight="bold", pad=20)

    col_labels = ["x", "0", "π/6", "π/4", "π/3", "π/2"]
    rows = [
        ["cos(x)", "1", "√3/2", "√2/2", "1/2", "0"],
        ["sin(x)", "0", "1/2", "√2/2", "√3/2", "1"],
        ["tan(x)", "0", "√3/3", "1", "√3", "indéfinie"],
    ]

    n_cols = len(col_labels)
    n_rows = len(rows) + 1  # +1 for header
    x_left, x_right = 0.5, 9.5
    y_top, y_bot = 3.6, 0.4
    col_w = (x_right - x_left) / n_cols
    row_h = (y_top - y_bot) / n_rows

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.4)

    # outer border + header separator
    ax.plot([x_left, x_right], [y_top, y_top], color="black", lw=1.8)
    ax.plot([x_left, x_right], [y_bot, y_bot], color="black", lw=1.8)
    ax.plot([x_left, x_left], [y_top, y_bot], color="black", lw=1.8)
    ax.plot([x_right, x_right], [y_top, y_bot], color="black", lw=1.8)
    header_y = y_top - row_h
    ax.plot([x_left, x_right], [header_y, header_y], color="black", lw=1.4)

    # vertical lines
    for c in range(1, n_cols):
        xc = x_left + c * col_w
        ax.plot([xc, xc], [y_top, y_bot], color="black", lw=1.0 if c > 1 else 1.6)

    # horizontal lines between data rows
    for r in range(1, len(rows)):
        yr = header_y - r * row_h
        ax.plot([x_left, x_right], [yr, yr], color="black", lw=0.8)

    # header text
    for c, label in enumerate(col_labels):
        xc = x_left + (c + 0.5) * col_w
        ax.text(xc, (y_top + header_y) / 2, label, ha="center", va="center", fontsize=13, fontweight="bold")

    # data text
    for r, row in enumerate(rows):
        yr_center = header_y - r * row_h - row_h / 2
        for c, val in enumerate(row):
            xc = x_left + (c + 0.5) * col_w
            weight = "bold" if c == 0 else "normal"
            ax.text(xc, yr_center, val, ha="center", va="center", fontsize=12, fontweight=weight)

    pdf.savefig(fig); plt.close(fig)

print("done:", pdf_path)
