import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from analytic_formulas import calculate_greeks

def plot_delta_heatmap():
    print("Génération de la Heatmap du Delta...")
    
    # 1. On définit les plages de données
    # Le prix de l'action (Spot) va de 50 à 150
    spots = np.linspace(50, 150, 20)
    # Le temps restant (Maturité) va de 0.1 an (bientôt fini) à 1 an
    times = np.linspace(0.1, 1.0, 20)
    
    # Paramètres fixes
    K = 100
    r = 0.05
    sigma = 0.2
    
    # Matrice pour stocker les Deltas
    # On initialise une matrice vide de taille 20x20
    delta_matrix = np.zeros((len(times), len(spots)))
    
    # 2. Double boucle (On remplit la grille)
    for i, t in enumerate(times):
        for j, s in enumerate(spots):
            # On appelle votre fonction existante
            delta, _ = calculate_greeks(s, K, t, r, sigma)
            delta_matrix[i, j] = delta
            
    # 3. Visualisation avec Seaborn (C'est plus beau que matplotlib pur)
    plt.figure(figsize=(10, 8))
    
    # Création de la heatmap
    # On inverse l'axe Y pour avoir le temps long en haut (convention)
    ax = sns.heatmap(delta_matrix, xticklabels=np.round(spots, 1), yticklabels=np.round(times, 2), cmap="coolwarm", annot=False)
    
    ax.invert_yaxis() # Pour avoir le temps qui passe de haut en bas ou l'inverse selon préférence
    
    plt.title("Heatmap du Delta (Sensibilité)\nPrix (X) vs Temps (Y)")
    plt.xlabel("Prix du Sous-jacent (Spot)")
    plt.ylabel("Temps à Maturité (Années)")
    
    plt.savefig('delta_heatmap.png')
    print("Heatmap sauvegardée sous 'delta_heatmap.png'")
    plt.show()

if __name__ == "__main__":
    plot_delta_heatmap()