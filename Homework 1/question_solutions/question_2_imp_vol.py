from context import fe621

import numpy as np
import pandas as pd


# Defining dates
data1_date = '2019-02-06'
data2_date = '2019-02-07'

# Loading DATA1
spy_data1 = fe621.util.loadData(folder_path='Homework 1/data/DATA1/SPY',
                                date=data1_date)
amzn_data1 = fe621.util.loadData(folder_path='Homework 1/data/DATA1/AMZN',
                                    date=data1_date)
vix_data1 = fe621.util.loadData(folder_path='Homework 1/data/DATA1/VIX',
                                date=data1_date)

# Loading DATA2
spy_data2 = fe621.util.loadData(folder_path='Homework 1/data/DATA2/SPY',
                                date=data2_date)
amzn_data2 = fe621.util.loadData(folder_path='Homework 1/data/DATA2/AMZN',
                                    date=data2_date)
vix_data2 = fe621.util.loadData(folder_path='Homework 1/data/DATA2/VIX',
                                date=data2_date)

# Loading Risk-free rate (effective federal funds rate)
rf = pd.read_csv('Homework 1/data/ffr.csv')

# Tolerance level for optimization
tol = 1e-6

def computeImpVolatilities():
    """Function to compute the implied volatilities for the SPY and AMZN option
    chains, for all maturities. Computed implied volatilities are output to
    CSV files.
    """

    # SP 500
    spy_data1_vol = fe621.util.computeAvgImpliedVolBisection(
                                                    data=spy_data1,
                                                    name='SPY',
                                                    rf=rf[data1_date][0],
                                                    current_date=data1_date,
                                                    tol=tol)
    # Saving to CSV
    spy_data1_vol.to_csv('Homework 1/bin/spy_data1_vol.csv', index=False)

    # AMZN
    amzn_data1_vol = fe621.util.computeAvgImpliedVolBisection(
                                                     data=amzn_data1,
                                                     name='AMZN',
                                                     rf=rf[data1_date][0],
                                                     current_date=data1_date,
                                                     tol=tol)
    # Saving to CSV
    amzn_data1_vol.to_csv('Homework 1/bin/amzn_data1_vol.csv', index=False)


if __name__ == "__main__":
    # Part 1 - Implied Volatility Computation
    computeImpVolatilities()
