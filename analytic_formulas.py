import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    """
    Calcule le prix d'une option Européenne via la formule fermée de Black-Scholes.
    """
    # 1. Calcul de d1 et d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # 2. Calcul du prix selon le type (Call ou Put)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("L'option doit être 'call' ou 'put'")
        
    return price

def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    # Delta (Call) = N(d1)
    # C'est la dérivée première du prix par rapport à S
    delta = norm.cdf(d1)

    # Gamma = N'(d1) / (S * sigma * sqrt(T))
    # C'est la dérivée seconde (convexité)
    # norm.pdf est la densité de probabilité (la courbe en cloche)
    gamma = norm.pdf(d1)/( S* sigma *np.sqrt(T))

    return delta , gamma 
