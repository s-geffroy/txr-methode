# SPDX-License-Identifier: EUPL-1.2
"""Construit les figures et les fiches PDF du dépôt de méthode TxR.

    python3 outils/construire.py [racine du dépôt]

Entrées : fiches/sources/*.md (Markdown réduit, voir _histoire).
Sorties : figures/*.png, fiches/*.pdf. Aucune donnée de station n'est lue :
les figures sont des schémas et des calculs sur des profils types.
Dépendances : numpy, matplotlib, reportlab.
"""
import io
import re
import sys
from pathlib import Path

import numpy as np

RACINE = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
VERSION = "0.5.1"
AUTEUR = "Sylvain Geffroy"
ENCRE, ACCENT, NEIGE, SOL = "#1d2733", "#b4470b", "#7fb3e6", "#e9e2d6"

# --- La méthode, en chiffres (les mêmes que dans METHODE.md) -----------------
SEUILS_T30 = [10, 20, 25, 35, 45, 60]          # pente maximale sur 30 m, % -> T1..T6
SEUILS_MUR = {3: 40, 4: 50, 5: 60, 6: 75}       # pente maximale sur 10 m, % -> T >= classe
SEUILS_R = [80, 200, 400, 700, 1100]            # dénivelé, m -> R1..R5
L0, K = 5.0, 5.0                                # lissage : L = L0 + K * h (h en m)

GRILLE_T = [("T0", "< 10 %", "presque plat"), ("T1", "10 à 20 %", "pente douce"),
            ("T2", "20 à 25 %", "pente modérée"), ("T3", "25 à 35 %", "pente marquée"),
            ("T4", "35 à 45 %", "raide"), ("T5", "45 à 60 %", "très raide"), ("T6", "≥ 60 %", "extrême")]
GRILLE_R = [("R0", "< 80 m"), ("R1", "80 à 200 m"), ("R2", "200 à 400 m"), ("R3", "400 à 700 m"),
            ("R4", "700 à 1 100 m"), ("R5", "≥ 1 100 m")]
# couleurs des classes T (même palette que la carte : sans rouge ni vert, lisible en daltonisme)
PALETTE_T = ["#fff3b0", "#ffd166", "#f4a259", "#d4789a", "#9b5de5", "#6a2c91", "#2e0f4f"]
# Descriptifs génériques, provisoires. Le préfixe « ~ » marque une combinaison rare.
GRILLE = [
    ["Front de neige, jardin d'enfants", "Petite pente pour débuter", "Raidillon court sur une liaison",
     "Court passage soutenu", "Ressaut raide très court", "~Mur isolé, quelques virages", "~Ressaut extrême isolé"],
    ["Chemin de liaison, on pousse sur les bâtons", "Verte courte, premiers virages", "Bleue courte",
     "Rouge courte", "Piste courte avec un passage raide", "Noire courte, un mur", "~Rare"],
    ["~Long chemin presque plat", "Verte de retour, fatigante pour un débutant", "Bleue classique",
     "Rouge classique", "Rouge raide ou noire", "Noire avec un mur", "~Rare"],
    ["~Très rare", "Longue verte, prévoir des pauses", "Longue bleue, les cuisses chauffent",
     "Grande rouge", "Noire soutenue", "Grande noire", "~Rare"],
    ["~Quasi inexistant", "~Route de vallée", "Grande bleue de vallée", "Rouge de vallée, il faut être en forme",
     "Grande noire, de l'endurance", "~Noire longue et engagée", "~Exceptionnel"],
    ["~Inexistant", "~Très rare", "~Rare", "Descente du sommet à la vallée", "Du sommet à la vallée, bon skieur",
     "~Expert endurant", "~Exceptionnel"],
]


def coefficient(l, W, L):
    """Part du mur (longueur l, m) retenue par une fenêtre de W m après lissage
    du profil par une moyenne glissante de L m : intégrale, sur le mur centré,
    du noyau trapézoïdal (créneau W) * (créneau L)."""
    a, b = min(W, L), max(W, L)
    x = np.linspace(-l / 2, l / 2, 4001)
    ax = np.abs(x)
    k = np.where(ax <= (b - a) / 2, 1 / b, np.clip(((a + b) / 2 - ax) / (a * b), 0, None))
    return float(np.trapezoid(k, x) if hasattr(np, "trapezoid") else np.trapz(k, x))


def table_coefficients(hauteurs_cm=(0, 25, 50, 75, 100, 125, 150, 175, 200), murs=(5, 8, 10, 12, 15, 20)):
    return [(h, L0 + K * h / 100, [coefficient(l, 10, L0 + K * h / 100) for l in murs]) for h in hauteurs_cm], murs


# --- Figures --------------------------------------------------------------------
def _plt():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 7, "font.family": "DejaVu Sans", "svg.hashsalt": "txr"})
    return plt


def figure_schemas():
    plt = _plt()
    fig, axs = plt.subplots(1, 3, figsize=(17.4 / 2.54, 5.0 / 2.54), dpi=220)
    # 1. pente sur 30 m
    ax = axs[0]
    s = np.linspace(0, 120, 300)
    z = 60 - 0.25 * s - 9 / (1 + np.exp(-(s - 62) / 4))
    ax.fill_between(s, z, z.min() - 6, color=SOL)
    ax.plot(s, z, color=ENCRE, lw=1.2)
    a, b = 50, 80
    za, zb = np.interp([a, b], s, z)
    ax.plot([a, b], [za, zb], color=ACCENT, lw=1.6)
    ax.plot([a, b], [za, za], color=ACCENT, lw=0.7, ls="--")
    ax.annotate("", xy=(b, zb), xytext=(b, za), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=0.8))
    ax.text(b + 3, (za + zb) / 2, "dénivelé", color=ACCENT, va="center", fontsize=6.5)
    ax.text((a + b) / 2, za + 2.5, "30 m", color=ACCENT, ha="center", fontsize=7)
    ax.text(2, z.min() - 4.5, "9 m de dénivelé sur 30 m = 30 % (17°)", fontsize=6, color=ENCRE)
    ax.set_title("1. La pente d'un passage de 30 m", fontsize=7, loc="left", color=ENCRE)
    # 2. zigzag vu de dessus, à 30° réels
    ax = axs[1]
    larg, t = 3.0, np.tan(np.radians(30))
    ax.add_patch(plt.Rectangle((0, -larg / 2), 10, larg, color="#eef2f6"))
    ax.plot([0, 10], [0, 0], color=ENCRE, lw=0.8, ls=(0, (4, 3)))
    d = larg * 0.85 / t          # avance pour traverser 85 % de la largeur
    xs, ys, x, y, sgn = [0.0], [0.0], 0.0, 0.0, 1
    while x < 10:
        cible = sgn * larg * 0.425
        dx = abs(cible - y) / t
        x, y = min(10, x + dx), y + np.sign(cible - y) * min(abs(cible - y), (10 - x) * t)
        xs.append(x); ys.append(y); sgn = -sgn
    ax.plot(xs, ys, color=ACCENT, lw=1.4)
    ax.annotate("", xy=(9.6, -2.0), xytext=(6.6, -2.0), arrowprops=dict(arrowstyle="->", color=ENCRE, lw=0.8))
    ax.text(0.1, -2.05, "sens de la descente", fontsize=6, color=ENCRE, va="center")
    ax.text(0.1, 1.7, "vue de dessus · largeur de la piste", fontsize=6, color=ENCRE)
    ax.text(d * 0.45 + 0.3, 0.05, "30°", fontsize=6.5, color=ACCENT)
    ax.set_xlim(0, 10); ax.set_ylim(-2.4, 2.1); ax.set_aspect("equal")
    ax.set_title("2. On choisit son passage, en zigzag", fontsize=7, loc="left", color=ENCRE)
    # 3. la neige lisse
    ax = axs[2]
    s = np.linspace(0, 100, 400)
    sol = 40 - 0.3 * s + 1.6 * np.sin(s / 2.2) + 2.2 * np.exp(-((s - 55) / 3) ** 2)
    k = 40
    lisse = np.convolve(np.pad(sol, k, mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="same")[k:-k] + 2.2
    ax.fill_between(s, lisse, sol, where=lisse > sol, color=NEIGE, alpha=0.7, lw=0)
    ax.fill_between(s, sol, sol.min() - 6, color=SOL)
    ax.plot(s, sol, color=ENCRE, lw=1.0)
    ax.plot(s, lisse, color="#2563eb", lw=1.1)
    ax.text(3, lisse[10] + 1.8, "surface de la neige", fontsize=6, color="#2563eb")
    ax.text(62, sol.min() - 3.5, "sol sans neige", fontsize=6, color=ENCRE)
    ax.set_title("3. La neige comble creux et bosses", fontsize=7, loc="left", color=ENCRE)
    for ax in axs:
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
    fig.tight_layout(pad=0.4)
    return _png(fig, plt)


def figure_abaque():
    plt = _plt()
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(17.4 / 2.54, 6.6 / 2.54), dpi=220)
    h = np.linspace(0, 250, 126)
    couleurs = ["#1d2733", "#3b5b7a", "#b4470b", "#7c3aed", "#0f766e", "#9a7b00"]
    for l, c in zip((5, 8, 10, 12, 15, 20), couleurs):
        a1.plot(h, [coefficient(l, 10, L0 + K * x / 100) for x in h], color=c, lw=1.2)
        a1.text(252, coefficient(l, 10, L0 + K * 2.5), f"{l} m", color=c, fontsize=6, va="center")
    a1.axvspan(200, 250, color="#eeeeee", lw=0)
    a1.text(225, 1.04, "hors domaine", fontsize=5.5, color="#666", ha="center")
    a1.set_xlim(0, 272); a1.set_ylim(0.3, 1.08)
    a1.set_xlabel("hauteur de neige au passage (cm)"); a1.set_ylabel("coefficient C")
    a1.set_title("A. Coefficient C selon la longueur du mur", fontsize=7, loc="left")
    a1.grid(color="#dddddd", lw=0.4)
    # exemple : mur de 10 m à 66 % dans une pente de 30 %
    p0, p1 = 30, 66
    g = [p0 + (p1 - p0) * coefficient(10, 10, L0 + K * x / 100) for x in h]
    a2.plot(h, g, color=ACCENT, lw=1.4)
    for cl, s in SEUILS_MUR.items():
        if 45 <= s <= 66:
            a2.axhline(s, color="#888", lw=0.6, ls="--")
            a2.text(2, s + 0.5, f"seuil T{cl} : {s} %", fontsize=5.8, color="#555")
    a2.axvline(123, color=ENCRE, lw=0.6, ls=":")
    a2.text(126, 63.5, "123 cm", fontsize=6)
    a2.axvspan(200, 250, color="#eeeeee", lw=0)
    a2.set_xlim(0, 250); a2.set_ylim(45, 66)
    a2.set_xlabel("hauteur de neige au passage (cm)"); a2.set_ylabel("pente sur 10 m après neige (%)")
    a2.set_title("B. Exemple : mur de 10 m à 66 % dans une pente de 30 %", fontsize=7, loc="left")
    a2.grid(color="#dddddd", lw=0.4)
    fig.tight_layout(pad=0.5)
    return _png(fig, plt)


def formule(tex, taille_pt):
    """Formule LaTeX (sous-ensemble mathtext de matplotlib) -> (png, largeur_pt, hauteur_pt)."""
    import struct
    plt = _plt()
    fig = plt.figure(figsize=(0.01, 0.01))
    tex = tex.replace("\\frac", "\\dfrac")   # fractions en taille normale
    fig.text(0, 0, f"${tex}$", fontsize=taille_pt * 1.15, color=ENCRE)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight", pad_inches=0.03, transparent=True,
                metadata={"Software": None})
    plt.close(fig)
    png = buf.getvalue()
    w, h = struct.unpack(">II", png[16:24])
    return png, w / 300 * 72, h / 300 * 72


def _png(fig, plt):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", metadata={"Software": None})
    plt.close(fig)
    return buf.getvalue()


# --- Fiches PDF -------------------------------------------------------------------
def _polices():
    import matplotlib
    from reportlab.lib.fonts import addMapping
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    d = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
    for nom, f in (("DejaVu", "DejaVuSans.ttf"), ("DejaVu-Bold", "DejaVuSans-Bold.ttf"),
                   ("DejaVu-It", "DejaVuSans-Oblique.ttf"), ("DejaVu-BoldIt", "DejaVuSans-BoldOblique.ttf"),
                   ("DejaVuMono", "DejaVuSansMono.ttf")):
        pdfmetrics.registerFont(TTFont(nom, d / f))
    addMapping("DejaVu", 0, 0, "DejaVu"); addMapping("DejaVu", 1, 0, "DejaVu-Bold")
    addMapping("DejaVu", 0, 1, "DejaVu-It"); addMapping("DejaVu", 1, 1, "DejaVu-BoldIt")


def _inline(t):
    t = t.replace("\u202f", "\u00a0")   # ReportLab coupe sur l'espace fine insécable, pas sur l'insécable
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)\*(?!\w)", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r'<font name="DejaVuMono" size="-1">\1</font>', t)
    return re.sub(r"\[(.+?)\]\((.+?)\)", r'<link href="\2" color="#1d4ed8">\1</link>', t)


def _styles(taille):
    from reportlab.lib.colors import HexColor
    from reportlab.lib.styles import ParagraphStyle

    ink, acc = HexColor(ENCRE), HexColor(ACCENT)
    base = ParagraphStyle("b", fontName="DejaVu", fontSize=taille, leading=taille * 1.32, textColor=ink,
                          spaceAfter=taille * 0.35)
    return {
        "h1": ParagraphStyle("h1", parent=base, fontName="DejaVu-Bold", fontSize=taille * 1.8, leading=taille * 2.1,
                             spaceAfter=2),
        "chapo": ParagraphStyle("c", parent=base, textColor=acc, fontSize=taille * 0.92, spaceAfter=taille * 0.6),
        "h2": ParagraphStyle("h2", parent=base, fontName="DejaVu-Bold", fontSize=taille * 1.15, leading=taille * 1.45,
                             spaceBefore=taille * 0.5, spaceAfter=taille * 0.2, textColor=acc),
        "p": base, "li": ParagraphStyle("li", parent=base, spaceAfter=taille * 0.12),
        "cell": ParagraphStyle("cell", parent=base, fontSize=taille * 0.82, leading=taille * 1.02, spaceAfter=0),
        "cellb": ParagraphStyle("cellb", parent=base, fontName="DejaVu-Bold", fontSize=taille * 0.82,
                                leading=taille * 1.02, spaceAfter=0),
        "note": ParagraphStyle("n", parent=base, fontSize=taille * 0.8, leading=taille * 1.05, textColor=HexColor("#555")),
    }


def _table(lignes, st, largeur_cm=17.4):
    from reportlab.lib.colors import HexColor
    from reportlab.lib.units import cm
    from reportlab.platypus import Paragraph, Table, TableStyle

    data = [[Paragraph(_inline(c), st["cellb"] if i == 0 else st["cell"]) for c in l] for i, l in enumerate(lignes)]
    t = Table(data, colWidths=[largeur_cm * cm / len(lignes[0])] * len(lignes[0]), repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, HexColor("#c8cdd3")),
                           ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f1ece4")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    return t


def _grille(st):
    from reportlab.lib.styles import ParagraphStyle
    st = dict(st, cell=ParagraphStyle("g", parent=st["cell"], fontSize=st["cell"].fontSize * 0.9,
                                      leading=st["cell"].leading * 0.92))
    from reportlab.lib.colors import HexColor
    from reportlab.lib.units import cm
    from reportlab.platypus import Paragraph, Table, TableStyle

    tete = [Paragraph("<b>R</b> ↓<br/><b>T</b> →", st["cell"])]
    tete += [Paragraph(f"<b>{c}</b><br/>{p}<br/><i>{d}</i>", st["cell"]) for c, p, d in GRILLE_T]
    data, style = [tete], []
    for i, ((r, dz), ligne) in enumerate(zip(GRILLE_R, GRILLE), start=1):
        rang = [Paragraph(f"<b>{r}</b><br/>{dz}", st["cell"])]
        for j, txt in enumerate(ligne, start=1):
            rare = txt.startswith("~")
            rang.append(Paragraph(f"<i>{_inline(txt[1:])}</i>" if rare else _inline(txt), st["cell"]))
            if rare:
                style.append(("BACKGROUND", (j, i), (j, i), HexColor("#f2f2f2")))
                style.append(("TEXTCOLOR", (j, i), (j, i), HexColor("#777777")))
        data.append(rang)
    t = Table(data, colWidths=[1.65 * cm] + [2.25 * cm] * 7)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, HexColor("#c8cdd3")),
                           ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f1ece4")),
                           ("BACKGROUND", (0, 1), (0, -1), HexColor("#f1ece4")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)] + style))
    return t


def _coefficients(st):
    rows, murs = table_coefficients()
    lignes = [["neige au passage", "L"] + [f"mur de {l} m" for l in murs]]
    for h, L, cs in rows:
        lignes.append([f"{h} cm", f"{L:.1f} m".replace(".", ",")] + [f"{c:.2f}".replace(".", ",") for c in cs])
    return _table(lignes, st)


def _histoire(md, taille, images):
    from reportlab.lib.units import cm
    from reportlab.platypus import Image, ListFlowable, ListItem, PageBreak, Paragraph, Spacer

    st = _styles(taille)
    out, para, items, kind, table = [], [], [], None, []

    def flush():
        nonlocal para, items, kind, table
        if para:
            out.append(Paragraph(_inline(" ".join(para)), st["p"])); para = []
        if items:
            out.append(ListFlowable([ListItem(Paragraph(_inline(i), st["li"]), leftIndent=taille * 1.2) for i in items],
                                    bulletType="1" if kind == "ol" else "bullet", start="1" if kind == "ol" else "•",
                                    leftIndent=taille * 1.2, bulletFontName="DejaVu", bulletFontSize=taille,
                                    bulletColor=ACCENT))
            items, kind = [], None
        if table:
            out.append(_table([[c.strip() for c in l.strip().strip("|").split("|")] for l in table
                               if not re.match(r"^\|[\s:|-]+\|$", l.strip())], st))
            out.append(Spacer(1, taille * 0.5)); table = []

    for line in md.splitlines():
        l = line.rstrip()
        if l.startswith("|"):
            if para or items:
                f_t = table; table = []; flush(); table = f_t
            table.append(l); continue
        elif table:
            flush()
        if not l:
            flush(); continue
        m = re.match(r"^\[\[(\w+)(?::(.+?))?\]\]$", l.strip())
        fm = re.match(r"^\$\$(.+)\$\$$", l.strip())
        if fm:
            flush()
            png, w, h = formule(fm.group(1).strip(), taille)
            img = Image(io.BytesIO(png), width=w, height=h)
            img.hAlign = "CENTER"
            out.append(Spacer(1, taille * 0.15)); out.append(img); out.append(Spacer(1, taille * 0.35))
            continue
        if l.startswith("# "):
            flush(); out.append(Paragraph(_inline(l[2:]), st["h1"]))
        elif l.startswith("> "):
            flush(); out.append(Paragraph(_inline(l[2:]), st["chapo"]))
        elif l.startswith("## "):
            flush(); out.append(Paragraph(_inline(l[3:]), st["h2"]))
        elif l.startswith("<small>"):
            flush(); out.append(Paragraph(_inline(l[7:].replace("</small>", "")), st["note"]))
        elif m:
            flush()
            nom, arg = m.group(1), m.group(2)
            if nom == "saut":
                out.append(PageBreak())
            elif nom == "grille":
                out.append(_grille(st)); out.append(Spacer(1, taille * 0.6))
            elif nom == "coefficients":
                out.append(_coefficients(st)); out.append(Spacer(1, taille * 0.5))
            elif nom == "image":
                png, hauteur = images[arg]
                out.append(Image(io.BytesIO(png), width=17.4 * cm, height=hauteur * cm)); out.append(Spacer(1, taille * 0.3))
            else:
                raise ValueError(f"directive inconnue : {nom}")
        elif re.match(r"^- ", l):
            if kind == "ol":
                flush()
            if para:
                out.append(Paragraph(_inline(" ".join(para)), st["p"])); para = []
            kind = "ul"; items.append(l[2:])
        elif re.match(r"^\d+\. ", l):
            if kind == "ul":
                flush()
            if para:
                out.append(Paragraph(_inline(" ".join(para)), st["p"])); para = []
            kind = "ol"; items.append(re.sub(r"^\d+\. ", "", l))
        elif items:
            items[-1] += " " + l.strip()
        else:
            para.append(l.strip())
    flush()
    return out


# --- Panneau de bord de piste (demi-page A4 = A5 paysage) ---------------------
T_PANNEAU = [("T0", "< 10 %", "presque plat"), ("T1", "10 à 20 %", "pente douce"),
             ("T2", "20 à 25 %", "pente modérée"), ("T3", "25 à 35 %", "pente marquée"),
             ("T4", "35 à 45 %", "raide"), ("T5", "45 à 60 %", "très raide"), ("T6", "≥ 60 %", "extrême")]
R_PANNEAU = [("R0", "< 80 m", "quelques virages"), ("R1", "80 à 200 m", "courte"),
             ("R2", "200 à 400 m", "moyenne"), ("R3", "400 à 700 m", "longue, avec des pauses"),
             ("R4", "700 à 1 100 m", "très longue"), ("R5", "≥ 1 100 m", "du sommet à la vallée")]


def panneau(chemin):
    """Panneau A5 paysage à afficher au départ des pistes : lire la note T·R."""
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.pagesizes import A5, landscape
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

    W, H = landscape(A5)
    c = canvas.Canvas(str(chemin), pagesize=(W, H), invariant=1)
    c.setTitle("TxR, panneau de bord de piste"); c.setAuthor(AUTEUR); c.setSubject("Méthode TxR, CC BY 4.0")
    ink, acc = HexColor(ENCRE), HexColor(ACCENT)
    m = 9 * mm
    # bandeau
    c.setFillColor(ink); c.rect(0, H - 22 * mm, W, 22 * mm, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("DejaVu-Bold", 19)
    c.drawString(m, H - 12.5 * mm, "Lire la note T·R d'une piste")
    c.setFont("DejaVu", 9.5)
    c.drawString(m, H - 18.5 * mm, "Deux chiffres plutôt qu'une couleur : la technique (T) et l'effort (R). L'un ne rattrape pas l'autre.")
    haut = H - 28 * mm
    # colonne T
    xT, lT = m, 92 * mm
    c.setFillColor(acc); c.setFont("DejaVu-Bold", 11.5)
    c.drawString(xT, haut, "T  la technique")
    c.setFillColor(ink); c.setFont("DejaVu", 7.8)
    c.drawString(xT, haut - 4.3 * mm, "pente du passage le plus raide, sur 30 m (ou un mur de 10 m)")
    y, hl = haut - 9.5 * mm, 7.6 * mm
    for i, (code_, pente, mot) in enumerate(T_PANNEAU):
        c.setFillColor(HexColor(PALETTE_T[i])); c.roundRect(xT, y - hl + 1.2 * mm, 13 * mm, hl - 1.2 * mm, 1.2 * mm, stroke=0, fill=1)
        c.setFillColor(white if i >= 4 else ink); c.setFont("DejaVu-Bold", 12)
        c.drawCentredString(xT + 6.5 * mm, y - hl + 3.0 * mm, code_)
        c.setFillColor(ink); c.setFont("DejaVu-Bold", 10.5)
        c.drawString(xT + 16 * mm, y - hl + 3.0 * mm, pente)
        c.setFont("DejaVu", 10.5)
        c.drawString(xT + 40 * mm, y - hl + 3.0 * mm, mot)
        y -= hl
    # colonne R
    xR = xT + lT + 6 * mm
    c.setFillColor(acc); c.setFont("DejaVu-Bold", 11.5)
    c.drawString(xR, haut, "R  l'effort")
    c.setFillColor(ink); c.setFont("DejaVu", 7.8)
    c.drawString(xR, haut - 4.3 * mm, "d'après le dénivelé de la piste")
    y = haut - 9.5 * mm
    for i, (code_, dz, mot) in enumerate(R_PANNEAU):
        c.setStrokeColor(ink); c.setLineWidth(0.8)
        c.roundRect(xR, y - hl + 1.2 * mm, 13 * mm, hl - 1.2 * mm, 1.2 * mm, stroke=1, fill=0)
        c.setFillColor(ink); c.setFont("DejaVu-Bold", 12)
        c.drawCentredString(xR + 6.5 * mm, y - hl + 3.0 * mm, code_)
        c.setFont("DejaVu-Bold", 10.5); c.drawString(xR + 16 * mm, y - hl + 3.0 * mm, dz)
        c.setFont("DejaVu", 9); c.drawString(xR + 47 * mm, y - hl + 3.0 * mm, mot)
        y -= hl
    # cette piste + exemple
    yb = 33 * mm
    c.setStrokeColor(acc); c.setLineWidth(1.6)
    c.roundRect(xR, yb - 4 * mm, W - xR - m, 15 * mm, 2 * mm, stroke=1, fill=0)
    c.setFillColor(ink); c.setFont("DejaVu-Bold", 15)
    c.drawString(xR + 4 * mm, yb + 3 * mm, "Cette piste :  T ____ · R ____")
    c.setFont("DejaVu", 8.2)
    c.drawString(xT, yb + 6.5 * mm, "Exemple : T3·R2, une piste dont le passage le plus raide fait")
    c.drawString(xT, yb + 2.6 * mm, "25 à 35 % (14 à 19°), pour 200 à 400 m de dénivelé.")
    c.drawString(xT, yb - 1.3 * mm, "T5·R1 : un mur sur une piste courte. T1·R4 : longue et facile.")
    # mises en garde
    c.setStrokeColor(HexColor("#c8cdd3")); c.setLineWidth(0.6); c.line(m, 24 * mm, W - m, 24 * mm)
    c.setFillColor(ink); c.setFont("DejaVu-Bold", 8.4)
    c.drawString(m, 19.5 * mm, "La note ne tient pas compte de la glace, de la neige dure, des bosses, de la visibilité ni de l'affluence.")
    c.setFont("DejaVu", 8.2)
    c.drawString(m, 15.6 * mm, "Notes de recherche, provisoires : les seuils n'ont pas encore été vérifiés sur le terrain.")
    c.drawString(m, 11.9 * mm, "Sur les pistes, le balisage et les consignes de la station font foi.")
    c.setFillColor(HexColor("#666666")); c.setFont("DejaVu", 6.6)
    c.drawString(m, 6 * mm, f"TxR, méthode v{VERSION} · {AUTEUR} · CC BY 4.0 · https://s-geffroy.github.io/txr-methode/")
    c.showPage(); c.save()


FICHES = {  # nom -> (titre du PDF, nombre de pages attendu)
    "grand-public": ("TxR, la méthode pour les skieurs", 3),
    "exploitants": ("TxR, la méthode pour les services des pistes", 3),
    "technique": ("TxR, fiche technique", 1),
    "grille": ("TxR, la grille T × R", 1),
}


def construire():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate

    _polices()
    images = {"schemas": (figure_schemas(), 5.0), "abaque": (figure_abaque(), 6.6)}
    (RACINE / "figures").mkdir(exist_ok=True)
    (RACINE / "figures" / "schemas-mesure.png").write_bytes(images["schemas"][0])
    (RACINE / "figures" / "abaque-neige.png").write_bytes(images["abaque"][0])
    for nom, (titre, pages) in FICHES.items():
        md = (RACINE / "fiches" / "sources" / f"{nom}.md").read_text(encoding="utf-8")
        for taille in (10, 9.5, 9, 8.6, 8.2, 7.8, 7.4):
            buf = io.BytesIO()

            def pied(c, doc, titre=titre):
                c.saveState(); c.setFont("DejaVu", 6.5); c.setFillColorRGB(0.4, 0.4, 0.4)
                c.drawString(1.8 * cm, 0.8 * cm, f"TxR, méthode v{VERSION} · {AUTEUR} · CC BY 4.0 · "
                             "https://s-geffroy.github.io/txr-methode/")
                c.drawRightString(A4[0] - 1.8 * cm, 0.8 * cm, f"{doc.page}")
                c.restoreState()
            doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.4 * cm,
                                    bottomMargin=1.4 * cm, title=titre, author=AUTEUR, subject="Méthode TxR",
                                    keywords="CC BY 4.0", invariant=1)
            doc.build(_histoire(md, taille, images), onFirstPage=pied, onLaterPages=pied)
            if doc.page <= pages:
                break
        else:
            raise ValueError(f"{nom} : plus de {pages} page(s) même en {taille} pt")
        (RACINE / "fiches" / f"{nom}.pdf").write_bytes(buf.getvalue())
        print(f"{nom}.pdf : {doc.page} page(s), {taille:g} pt")
    panneau(RACINE / "fiches" / "panneau.pdf")
    print("panneau.pdf : A5 paysage")


if __name__ == "__main__":
    if "--coefficients" in sys.argv:
        rows, murs = table_coefficients((0, 25, 50, 75, 100, 110, 125, 150, 175, 200))
        for h, L, cs in rows:
            print(h, L, [round(c, 2) for c in cs])
    else:
        construire()
