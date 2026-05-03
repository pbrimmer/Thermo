import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from scipy.optimize import brentq
import ipywidgets as widgets
from IPython.display import display

def P_vdw(Vr, Tr):
    return 8 * Tr / (3 * Vr - 1) - 3 / Vr**2

def find_roots(Tr, P0):
    Vr = np.linspace(0.35, 6, 2000)
    f = P_vdw(Vr, Tr) - P0

    roots = []
    for i in range(len(Vr)-1):
        if f[i] * f[i+1] < 0:
            try:
                r = brentq(lambda x: P_vdw(x, Tr) - P0, Vr[i], Vr[i+1])
                roots.append(r)
            except:
                pass

    # remove duplicates
    roots = np.unique(np.round(roots, 4))
    return roots

def area_diff(Tr, P0):
    roots = find_roots(Tr, P0)
    if len(roots) < 3:
        return None, roots

    V1, V2, V3 = roots[:3]

    V_left = np.linspace(V1, V2, 500)
    V_right = np.linspace(V2, V3, 500)

    A_left = simpson(P_vdw(V_left, Tr) - P0, x=V_left)
    A_right = simpson(P0 - P_vdw(V_right, Tr), x=V_right)

    return A_left - A_right, roots

def find_maxwell(Tr):
    P_vals = np.linspace(0.05, 1.0, 200)
    diffs = []

    for P0 in P_vals:
        diff, roots = area_diff(Tr, P0)
        if diff is not None:
            diffs.append((P0, diff))

    for (P1, d1), (P2, d2) in zip(diffs[:-1], diffs[1:]):
        if d1 * d2 < 0:
            return brentq(lambda P: area_diff(Tr, P)[0], P1, P2)

    return None

def plot_vdw(Tr=0.85, P0=0.4, show_maxwell=False):
    Vr = np.linspace(0.35, 6, 2000)
    Pr = P_vdw(Vr, Tr)

    plt.figure(figsize=(7,5))
    plt.plot(Vr, Pr, label=f"T_r={Tr:.2f}")
    plt.axhline(P0, linestyle="--", label=f"P_r={P0:.3f}")

    diff, roots = area_diff(Tr, P0)

    if roots is not None and len(roots) >= 3:
        V1, V2, V3 = roots[:3]

        V_left = np.linspace(V1, V2, 300)
        V_right = np.linspace(V2, V3, 300)

        plt.fill_between(V_left, P_vdw(V_left, Tr), P0, alpha=0.3)
        plt.fill_between(V_right, P0, P_vdw(V_right, Tr), alpha=0.3)

        if diff is not None:
            plt.text(4.5, 1.2, f"ΔA = {diff:.4f}")

    if show_maxwell:
        P_star = find_maxwell(Tr)
        if P_star:
            plt.axhline(P_star, linewidth=2, label=f"Maxwell P_r={P_star:.3f}")

    plt.xlabel("Reduced volume V_r")
    plt.ylabel("Reduced pressure P_r")
    plt.ylim(-0.5, 1.5)
    plt.xlim(0.35, 6)
    plt.grid()
    plt.legend()
    plt.show()

widgets.interact(
    plot_vdw,
    Tr=(0.65, 1.2, 0.01),
    P0=(0.05, 1.0, 0.01),
    show_maxwell=False
)
