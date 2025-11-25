# Stochastic Option Pricing Engine 📉⚡

[![Language](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Academic%20Project-orange.svg)]()

## 📖 Overview
This project implements a robust pricing engine for **European Call and Put Options**, developed as part of the **Applied Mathematics (MACS)** curriculum at **Télécom Paris**.

It bridges the gap between analytical solutions and numerical simulations, providing a comparative analysis of:
1.  **Black-Scholes-Merton (BSM)** closed-form solution.
2.  **Monte Carlo (MC)** simulations with variance reduction techniques.

The engine also includes a risk management module to compute and visualize **Greeks** (Sensitivities).

## 🧮 Mathematical Framework

### 1. Underlying Asset Dynamics
The asset price $S_t$ is modeled using a **Geometric Brownian Motion (GBM)** under the risk-neutral measure $\mathbb{Q}$:

$$dS_t = r S_t dt + \sigma S_t dW_t^\mathbb{Q}$$

Where:
* $r$: Risk-free interest rate.
* $\sigma$: Constant volatility.
* $W_t^\mathbb{Q}$: Wiener process under $\mathbb{Q}$.

### 2. Pricing Valuation
The value of a European option $V_0$ with payoff $\Phi(S_T)$ is given by the risk-neutral expectation:

$$V_0 = e^{-rT} \mathbb{E}^{\mathbb{Q}} [ \Phi(S_T) ]$$

### 3. Numerical Integration (Monte Carlo)
We approximate the expectation using the Law of Large Numbers. To ensure faster convergence ($\mathcal{O}(1/\sqrt{N})$), we implement **Antithetic Variates** as a variance reduction technique:

$$\hat{V}_{MC} = \frac{e^{-rT}}{2N} \sum_{i=1}^{N} \left( \Phi(S_T^{(i)}) + \Phi(\tilde{S}_T^{(i)}) \right)$$

## 🚀 Key Features

* **Vectorized Implementation:** Fully vectorized utilizing `NumPy` broadcasting for high-performance simulations ($>10^6$ paths in seconds).
* **Convergence Analysis:** Automated plotting of the MC estimator convergence with **95% Confidence Intervals** (Central Limit Theorem).
* **Risk Management (Greeks):** Analytical computation of Delta ($\Delta$), Gamma ($\Gamma$), Vega ($\nu$), Theta ($\Theta$), and Rho ($\rho$).
* **3D Visualization:** Interactive surfaces showing the impact of "Moneyness" and "Time to Maturity" on hedging parameters.

## 📊 Results & Visualization

### Convergence Analysis
The following plot demonstrates the asymptotic stability of the Monte Carlo estimator towards the analytical BSM price. The gray area represents the confidence interval shrinking as $N$ increases.

<img width="1200" height="700" alt="convergence_with_confidence" src="https://github.com/user-attachments/assets/40054928-ca1f-4b55-9465-7561710df6e3" />

*Figure 1: Monte Carlo convergence (500k simulations) vs Black-Scholes benchmark.*

### Delta Sensitivity Surface
This heatmap illustrates the **Delta Hedging** risk profile. Note the steep transition (Gamma risk) as $T \to 0$ for At-The-Money options.

<img width="1000" height="800" alt="delta_heatmap" src="https://github.com/user-attachments/assets/361b3113-dfd8-4eaa-8c35-2731c1e37572" />

*Figure 2: Delta sensitivity across Spot Price and Time to Maturity.*

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Chakour-Yasser/stochastic-option-pricer.git](https://github.com/Chakour-Yasser/stochastic-option-pricer.git)
    cd stochastic-option-pricer
    ```

2.  **Install dependencies:**
    ```bash
    pip install numpy scipy matplotlib seaborn
    ```

3.  **Run the analysis:**
    ```bash
    python main.py
    ```

## 📚 References
* **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives*. Pearson.
* **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.

---
*Author: Yasser Chakour - Engineering Student at Télécom Paris.*
