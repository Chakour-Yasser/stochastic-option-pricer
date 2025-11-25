import numpy as np
import matplotlib.pyplot as plt
from analytic_formulas import black_scholes_price
from monte_carlo import monte_carlo_price

def plot_convergence():
    # Paramètres
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    
    # Vrai prix (Référence)
    bs_price = black_scholes_price(S, K, T, r, sigma, 'call')
    
    # Simulations
    n_simulations_list = range(1000, 510000, 2000) # Pas de 2000 pour aller plus vite
    mc_prices = []
    upper_bound = []
    lower_bound = []
    
    print("Calcul des intervalles de confiance...")
    
    for n in n_simulations_list:
        # On récupère le prix ET l'erreur standard
        price, std_err = monte_carlo_price(S, K, T, r, sigma, num_simulations=n)
        mc_prices.append(price)
        
        # Calcul des bornes (Intervalle de confiance à 95%)
        # On centre le cône sur le VRAI prix pour visualiser la cible
        upper_bound.append(bs_price + 1.96 * std_err)
        lower_bound.append(bs_price - 1.96 * std_err)
        
    # --- Graphique ---
    plt.figure(figsize=(12, 7))
    
    # 1. Le Cône de Confiance (Zone grise)
    plt.fill_between(n_simulations_list, lower_bound, upper_bound, color='gray', alpha=0.3, label='Intervalle de Confiance 95%')
    
    # 2. La ligne de référence Black-Scholes
    plt.axhline(y=bs_price, color='red', linestyle='--', linewidth=2, label=f'Prix Black-Scholes ({bs_price:.2f})')
    
    # 3. La courbe Monte Carlo
    plt.plot(n_simulations_list, mc_prices, color='blue', marker='o', markersize=3, label='Monte Carlo')
    
    plt.title('Convergence de Monte Carlo et Intervalle de Confiance')
    plt.xlabel('Nombre de Simulations (N)')
    plt.ylabel('Prix de l\'Option (€)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('convergence_with_confidence.png')
    print("Terminé ! Regardez le fichier 'convergence_with_confidence.png'")
    plt.show()

if __name__ == "__main__":
    plot_convergence()