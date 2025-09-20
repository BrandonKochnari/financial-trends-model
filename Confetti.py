# Project Structure
# Python Version: 3.9
# Packages Required: numpy, matplotlib

# Project Main Concept
# Objective: Imitate stock movement in the stock market
# Pre-planning:
#   - Method: Apply distribution to create a probability distribution function with range
#   - Desired Outcome: A general trend should be discovered if sample size is increased
#   - Varying Factors:
#       - s_i: the initial value of the stock(s)
#       - sd: standard deviation (volatility of stock)
#       - mu(µ): average rate of increase over 11 months
#       - dt (delta time): domain / number of experiments to be conducted
#       - trials: the number of trials to be conducted overall and recorded


# Execution
import random
import numpy as np
from matplotlib import pyplot as pl


# Initialize
def init():
    global history, s_i, rand, mu, dt, sd, trial
    history = []
    rand = random.Random()
    s_i = 158.37
    sd = 22.8
    mu = 6.06
    dt = 11
    trial = 100


# Start
if __name__ == "__main__":
    init()

    global trial
    # Main loop - Simulate the ups and downs of a stock trend
    for attempts in range(trial):
        tempHistory = []
        current_price = s_i
        tempHistory.append(s_i)
        for i in range(dt):
            current_price += (mu / dt) + rand.uniform(-sd, +sd)
            tempHistory.append(current_price)
        history.append(tempHistory)


    # Plot the data
    for i in range(trial):
        # Compile data
        x = np.arange(0, (dt+1), 1)  # Arrange an array from 0 to 'dt+1' with increment of 1
        y = history[i]  # Experimental values
        pl.plot(x, y)
        #Compile Report
        coordinates = str(i) + ": "
        for index in range(len(x)):
            coordinates += "(" + str(round(x[index], 1)) + ', ' + str(round(y[index], 2)) + ") "
        print(coordinates)
    pl.title('Possible Outcomes of AMD Market Share Price')
    pl.xlabel('Time (months since 01/11/2021)')
    pl.ylabel('Price (USD)')
    pl.show()

