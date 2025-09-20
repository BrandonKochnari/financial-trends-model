# Financial Trends Model 📈💹

**Financial Trends Model** is a Python-based simulation project that imitates **stock price movements** using probability distributions.  
The program generates multiple trials of price paths, applies random volatility, and visualizes possible outcomes through **line charts**.

---

## Features

- **Stock price simulation** over a given time period.  
- Adjustable parameters:  
  - `s_i`: initial stock price  
  - `sd`: standard deviation (volatility)  
  - `mu`: average rate of increase over 11 months  
  - `dt`: number of months (time steps)  
  - `trial`: number of simulated trials  
- **Randomized price movement** using uniform noise.  
- **Graphical output** with Matplotlib, showing multiple possible stock trajectories.  
- **Detailed console report** listing coordinates for each simulated price path.  

---

## Requirements

- **Python 3.9+**  
- Packages:  
  - `numpy`  
  - `matplotlib`

Install dependencies with:
```bash
pip install numpy matplotlib
```

## Usage 

1. Clone the repository:
   ```bash
   git clone https://github.com/BrandonKochnari/financial-trends-model.git
   cd financial-trends-model

2. Run the program:
   ```bash
   python Confetti.py
3. The script will:  
  • Simulate trial stock paths.  
  • Print coordinate logs of price changes.  
  • Display a Matplotlib chart of all outcomes.  

## Future Improvements

• Add more realistic stochastic models (e.g., Geometric Brownian Motion).  
• Allow user input for parameters instead of hardcoding.  
• Save results to CSV or Excel for deeper financial analysis.  
