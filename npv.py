import numpy as np
import matplotlib.pyplot as plt

def calculate_npv(rate: float, cashflows: list[int]) -> int:
    npv = 0
    for t in range(len(cashflows)):
        npv += cashflows[t]/(1+rate)**t
    return npv

def npvs(rates: list[float], cashflows: list[int]) -> list[float]:
    npvs = []
    for rate in rates:
        npvs.append(calculate_npv(rate, cashflows))
    return npvs

discount_rates = np.linspace(0.01, 0.50, 100)
my_project_cashflows = [-1000000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1000000]
my_project_npvs = npvs(discount_rates, my_project_cashflows)
  
plt.plot(discount_rates,my_project_npvs, linewidth = 2.0, color = "green")
plt.axhline(y=0, linewidth = 0.5, color = "black")
plt.title('NPV Profile for Different Discount Rates')
plt.xlabel('Discount Rate')
plt.ylabel('Net Present Value in USD')
plt.show()