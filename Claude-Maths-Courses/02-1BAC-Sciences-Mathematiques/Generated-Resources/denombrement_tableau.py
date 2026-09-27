import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["font.size"] = 12

pdf_path = "Denombrement_tableau_decision.pdf"

with PdfPages(pdf_path) as pdf:
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.axis("off")
    ax.set_title("Dénombrement — tableau de décision", fontsize=16, fontweight="bold", pad=20)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    x_left, x_mid, x_right = 2.4, 6.2, 9.6
    y_top, y_h1, y_h2, y_bot = 5.2, 3.7, 2.2, 0.7

    # outer border
    ax.plot([x_left, x_right], [y_top, y_top], color="black", lw=1.8)
    ax.plot([x_left, x_right], [y_bot, y_bot], color="black", lw=1.8)
    ax.plot([x_left, x_left], [y_top, y_bot], color="black", lw=1.8)
    ax.plot([x_right, x_right], [y_top, y_bot], color="black", lw=1.8)
    # header separator (below top row of column headers)
    ax.plot([x_left, x_right], [y_h1, y_h1], color="black", lw=1.6)
    # row separator between the two data rows
    ax.plot([x_left, x_right], [y_h2, y_h2], color="black", lw=1.0)
    # vertical separators
    ax.plot([x_mid, x_mid], [y_top, y_bot], color="black", lw=1.6)

    # column headers
    ax.text((x_left + x_mid) / 2, (y_top + y_h1) / 2, "Sans répétition", fontsize=13, fontweight="bold", ha="center", va="center")
    ax.text((x_mid + x_right) / 2, (y_top + y_h1) / 2, "Avec répétition", fontsize=13, fontweight="bold", ha="center", va="center")

    # row label column (draw a thin left strip by adding text to the left of x_left, outside the box)
    ax.text(x_left - 0.15, (y_h1 + y_h2) / 2, "Ordre\ncompte", fontsize=12, fontweight="bold", ha="right", va="center")
    ax.text(x_left - 0.15, (y_h2 + y_bot) / 2, "Ordre ne\ncompte pas", fontsize=12, fontweight="bold", ha="right", va="center")

    # cell contents
    ax.text((x_left + x_mid) / 2, (y_h1 + y_h2) / 2,
            "ARRANGEMENT\nA(n,p) = n!/(n-p)!\n\n(cas particulier p=n :\nPERMUTATION, n!)",
            fontsize=11, ha="center", va="center")

    ax.text((x_mid + x_right) / 2, (y_h1 + y_h2) / 2,
            "p-LISTE\nnᵖ",
            fontsize=13, fontweight="bold", ha="center", va="center")

    ax.text((x_left + x_mid) / 2, (y_h2 + y_bot) / 2,
            "COMBINAISON\nC(n,p) = n!/(p!(n-p)!)",
            fontsize=13, fontweight="bold", ha="center", va="center")

    ax.text((x_mid + x_right) / 2, (y_h2 + y_bot) / 2,
            "COMBINAISON AVEC RÉP.\nC'(n,p) = C(n+p-1,p)\n\n(bonus, hors 1BAC —\ntechnique étoiles et barres)",
            fontsize=10, ha="center", va="center")

    ax.text(5.0, 0.15, "Vocabulaire : tirage successif = ordre compte. Tirage simultané = ordre ne compte pas. \"Avec remise\" = avec répétition.",
            fontsize=9, ha="center", va="center", color="dimgray")

    pdf.savefig(fig); plt.close(fig)

print("done:", pdf_path)
