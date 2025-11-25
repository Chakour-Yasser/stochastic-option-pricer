from analytic_formulas import black_scholes_price
from monte_carlo import monte_carlo_price

# --- Paramètres du marché ---
S = 100      # Prix de l'action aujourd'hui
K = 100      # Prix d'exercice (Strike)
T = 1.0      # Maturité (1 an)
r = 0.05     # Taux sans risque (5%)
sigma = 0.2  # Volatilité (20%)

# --- 1. Prix Exact (Black-Scholes) ---
bs_price = black_scholes_price(S, K, T, r, sigma, "call")
print(f"Prix Théorique (Black-Scholes) : {bs_price:.4f} €")

# --- 2. Prix Simulé (Monte Carlo) ---
mc_price , _ = monte_carlo_price(S, K, T, r, sigma, num_simulations=1_000_000, option_type="call")
print(f"Prix Simulé (Monte Carlo)      : {mc_price:.4f} €")

# --- 3. Vérification ---
error = abs(bs_price - mc_price)
print(f"Erreur d'approximation         : {error:.4f} €")