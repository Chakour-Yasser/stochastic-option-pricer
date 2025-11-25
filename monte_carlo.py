import numpy as np

def monte_carlo_price(S, K, T, r, sigma, num_simulations=10000, option_type='call'):
    """
    Retourne le prix ET l'erreur standard (pour l'intervalle de confiance).
    """
    Z = np.random.standard_normal(num_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    if option_type == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
    
    # Actualisation
    payoff_discounted = np.exp(-r * T) * payoff
    
    # 1. Le Prix (Moyenne)
    price = np.mean(payoff_discounted)
    
    # 2. L'Erreur Standard (Ecart-type de la moyenne)
    # C'est sigma / sqrt(N)
    std_dev = np.std(payoff_discounted)
    std_err = std_dev / np.sqrt(num_simulations)
    
    return price, std_err