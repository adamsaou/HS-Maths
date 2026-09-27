import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["font.size"] = 14

Y_TOP = 1.2   # top border
Y_SEP = 0.3   # separator between x-row and f(x)-row
Y_BOT = -1.1  # bottom border
X_LEFT = 1.6
X_RIGHT = 9.4

def new_fig(title):
    fig, ax = plt.subplots(figsize=(9, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.6, 2.2)
    ax.axis("off")
    ax.set_title(title, fontsize=16, fontweight="bold", pad=20, loc="left")
    fig.subplots_adjust(top=0.80, bottom=0.06)
    return fig, ax

def frame(ax, x_positions):
    # borders
    ax.plot([X_LEFT, X_RIGHT], [Y_TOP, Y_TOP], color="black", lw=1.5)
    ax.plot([X_LEFT, X_RIGHT], [Y_BOT, Y_BOT], color="black", lw=1.5)
    ax.plot([X_LEFT, X_RIGHT], [Y_SEP, Y_SEP], color="black", lw=1.5)
    ax.plot([X_LEFT, X_LEFT], [Y_TOP, Y_BOT], color="black", lw=1.5)
    for xp in x_positions:
        ax.plot([xp, xp], [Y_TOP, Y_BOT], color="black", lw=1.0)
    ax.text(0.9, (Y_TOP + Y_SEP) / 2, "x", fontsize=15, ha="center", va="center", fontweight="bold")
    ax.text(0.9, (Y_SEP + Y_BOT) / 2, "f(x)", fontsize=15, ha="center", va="center", fontweight="bold")

def double_bar(ax, x):
    ax.plot([x - 0.06, x - 0.06], [Y_TOP, Y_BOT], color="black", lw=1.0)
    ax.plot([x + 0.06, x + 0.06], [Y_TOP, Y_BOT], color="black", lw=1.0)

def xval(ax, x, text):
    ax.text(x, (Y_TOP + Y_SEP) / 2, text, fontsize=14, ha="center", va="center")

def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", color="black", lw=2))

def fval(ax, x, y, text, dx=0, dy=0.18):
    ax.text(x + dx, y + dy, text, fontsize=13, ha="center", va="center")

# vertical band available for arrows inside f(x) row
F_HIGH = Y_SEP - 0.18
F_LOW = Y_BOT + 0.18

pdf_path = "Tableaux_de_variations.pdf"
with PdfPages(pdf_path) as pdf:

    # 1. Affine croissante
    fig, ax = new_fig("Fonction affine (x -> ax+b), a > 0 -- croissante")
    frame(ax, [])
    xval(ax, X_LEFT, "-inf"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_LOW, X_RIGHT - 0.3, F_HIGH)
    pdf.savefig(fig); plt.close(fig)

    # 1b. Fonction constante
    fig, ax = new_fig("Fonction constante (x -> c)")
    frame(ax, [])
    xval(ax, X_LEFT, "-inf"); xval(ax, X_RIGHT, "+inf")
    y_flat = (F_HIGH + F_LOW) / 2
    ax.plot([X_LEFT + 0.3, X_RIGHT - 0.3], [y_flat, y_flat], color="black", lw=2)
    fval(ax, (X_LEFT + X_RIGHT) / 2, y_flat, "c", dy=0.22)
    pdf.savefig(fig); plt.close(fig)

    # 2. Affine décroissante
    fig, ax = new_fig("Fonction affine (x -> ax+b), a < 0 -- décroissante")
    frame(ax, [])
    xval(ax, X_LEFT, "-inf"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_HIGH, X_RIGHT - 0.3, F_LOW)
    pdf.savefig(fig); plt.close(fig)

    # 3. Fonction carrée
    fig, ax = new_fig("Fonction carrée (x -> x^2)")
    mid = 5.5
    frame(ax, [mid])
    xval(ax, X_LEFT, "-inf"); xval(ax, mid, "0"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_HIGH, mid - 0.15, F_LOW)
    arrow(ax, mid + 0.15, F_LOW, X_RIGHT - 0.3, F_HIGH)
    fval(ax, X_LEFT, F_HIGH, "+inf", dx=0.25)
    fval(ax, X_RIGHT, F_HIGH, "+inf", dx=-0.25)
    fval(ax, mid, F_LOW, "0", dy=-0.22)
    pdf.savefig(fig); plt.close(fig)

    # 4. Fonction valeur absolue
    fig, ax = new_fig("Fonction valeur absolue (x -> |x|)")
    mid = 5.5
    frame(ax, [mid])
    xval(ax, X_LEFT, "-inf"); xval(ax, mid, "0"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_HIGH, mid - 0.15, F_LOW)
    arrow(ax, mid + 0.15, F_LOW, X_RIGHT - 0.3, F_HIGH)
    fval(ax, X_LEFT, F_HIGH, "+inf", dx=0.25)
    fval(ax, X_RIGHT, F_HIGH, "+inf", dx=-0.25)
    fval(ax, mid, F_LOW, "0", dy=-0.22)
    pdf.savefig(fig); plt.close(fig)

    # 5. Fonction racine carrée
    fig, ax = new_fig("Fonction racine carrée (x -> sqrt(x))")
    frame(ax, [])
    xval(ax, X_LEFT, "0"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_LOW, X_RIGHT - 0.3, F_HIGH)
    fval(ax, X_LEFT, F_LOW, "0", dy=-0.22)
    fval(ax, X_RIGHT, F_HIGH, "+inf", dx=-0.25)
    pdf.savefig(fig); plt.close(fig)

    # 6b. Fonction cube
    fig, ax = new_fig("Fonction cube (x -> x^3)")
    frame(ax, [])
    xval(ax, X_LEFT, "-inf"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_LOW, X_RIGHT - 0.3, F_HIGH)
    fval(ax, X_LEFT, F_LOW, "-inf", dy=-0.22)
    fval(ax, X_RIGHT, F_HIGH, "+inf", dx=-0.25)
    pdf.savefig(fig); plt.close(fig)

    # 6c. Trinôme du second degré, a > 0
    fig, ax = new_fig("Trinôme du second degré f(x)=ax²+bx+c, a > 0")
    mid = 5.5
    frame(ax, [mid])
    xval(ax, X_LEFT, "-inf"); xval(ax, mid, "-b/2a"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_HIGH, mid - 0.15, F_LOW)
    arrow(ax, mid + 0.15, F_LOW, X_RIGHT - 0.3, F_HIGH)
    fval(ax, X_LEFT, F_HIGH, "+inf", dx=0.25)
    fval(ax, X_RIGHT, F_HIGH, "+inf", dx=-0.25)
    fval(ax, mid, F_LOW, "f(-b/2a)", dy=-0.22)
    pdf.savefig(fig); plt.close(fig)

    # 6d. Trinôme du second degré, a < 0
    fig, ax = new_fig("Trinôme du second degré f(x)=ax²+bx+c, a < 0")
    mid = 5.5
    frame(ax, [mid])
    xval(ax, X_LEFT, "-inf"); xval(ax, mid, "-b/2a"); xval(ax, X_RIGHT, "+inf")
    arrow(ax, X_LEFT + 0.3, F_LOW, mid - 0.15, F_HIGH)
    arrow(ax, mid + 0.15, F_HIGH, X_RIGHT - 0.3, F_LOW)
    fval(ax, X_LEFT, F_LOW, "-inf", dy=-0.22)
    fval(ax, X_RIGHT, F_LOW, "-inf", dy=-0.22)
    fval(ax, mid, F_HIGH, "f(-b/2a)", dy=0.18)
    pdf.savefig(fig); plt.close(fig)

    # 6. Fonction inverse
    fig, ax = new_fig("Fonction inverse (x -> 1/x)")
    mid = 5.5
    frame(ax, [mid])
    xval(ax, X_LEFT, "-inf"); xval(ax, mid, "0"); xval(ax, X_RIGHT, "+inf")
    double_bar(ax, mid)
    arrow(ax, X_LEFT + 0.3, F_HIGH - 0.35, mid - 0.2, F_LOW)
    arrow(ax, mid + 0.2, F_HIGH, X_RIGHT - 0.3, F_LOW + 0.35)
    fval(ax, X_LEFT, F_HIGH - 0.35, "0", dx=0.25)
    fval(ax, mid, F_LOW, "-inf", dx=-0.35, dy=-0.05)
    fval(ax, mid, F_HIGH, "+inf", dx=0.35, dy=0.05)
    fval(ax, X_RIGHT, F_LOW + 0.35, "0", dx=-0.25)
    pdf.savefig(fig); plt.close(fig)

print("done:", pdf_path)
