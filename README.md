# stochastic-option-pricer
A robust Python pricing engine for European Options comparing Analytical (Black-Scholes) and Numerical (Monte Carlo) methods. Includes Variance Reduction techniques and 3D Greeks visualization.
# Stochastic Option Pricer 📉🎲

## Overview
This project implements a pricing engine for **European Call and Put Options**, bridging the gap between analytical solutions and stochastic simulations. Ideally suited for validating theoretical pricing models against numerical convergence.

## Key Features
* **Analytical Pricing:** Full implementation of the **Black-Scholes-Merton** closed-form solution.
* **Monte Carlo Engine:** Vectorized simulation of Geometric Brownian Motion (GBM) paths ($dS_t = rS_tdt + \sigma S_tdW_t$).
* **Variance Reduction:** Implements Antithetic Variates to improve convergence speed and precision.
* **Risk Management:** Automatic calculation of **Greeks** (Delta, Gamma, Vega, Theta, Rho).
* **Visualization:** * Convergence analysis of Monte Carlo estimator vs Black-Scholes price (Law of Large Numbers).
    * 3D Heatmaps of option sensitivities (Spot vs Time).

## Mathematical Background
The pricer solves the valuation problem under the risk-neutral measure $\mathbb{Q}$:
$$V_0 = e^{-rT} \mathbb{E}^{\mathbb{Q}} [ \Phi(S_T) ]$$
Where $S_T$ follows a GBM and $\Phi$ is the payoff function.

## Results

<img width="1200" height="700" alt="Image" src="https://github.com/user-attachments/assets/d526db24-d3a2-4178-bf42-d76049a4de90" />

> *Figure 1: Monte Carlo convergence with 95% Confidence Interval.*

<img width="1000" height="800" alt="Image" src="https://github.com/user-attachments/assets/ed6a3520-c750-40e1-b500-29a38eb78eb1" />

> *Figure 2: Delta sensitivity surface (Spot Price vs Time to Maturity)*

## Installation & Usage
```bash
pip install -r requirements.txt
python main.py
