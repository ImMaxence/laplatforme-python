initiale = 10000
annual_yield = 5

def calculateYield(money, rate):
    return (rate * money) / 100

# Initiale benefit
initiale_benefit = calculateYield(initiale, annual_yield)
print(initiale_benefit)

# Increase money and rate
initiale = initiale + 5000
annual_yield = annual_yield + 2
increase_benefit = calculateYield(initiale, annual_yield)
print(increase_benefit)

# User remove 10% money and rate -1%
newInitiale = initiale * (10 / 100)
initiale = initiale - newInitiale

annual_yield = annual_yield - 1
remove_benefit = calculateYield(initiale, annual_yield)
print(remove_benefit)