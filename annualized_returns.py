import pandas as pd
import numpy as np
def annualize_rets(seires_of_returns, periods_per_year):
    """
    Annualizes a set of returns

    1- We should infer the periods per year, periods could be month, day or quarter
    2- Annual return is defined as the percentage change in an investment over a one-year period.
    3- Annualized return is the percentage change in an investment measured over periods longer than one year.
   
    """
    compounded_growth = (1+seires_of_returns).prod()
    n_periods = seires_of_returns.shape[0]
    return compounded_growth**(periods_per_year/n_periods)-1