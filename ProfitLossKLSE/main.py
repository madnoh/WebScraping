''' Stocks net profit/loss calculator
'''
brokerRate = 0.0042
units = 1000
buyPrice = 1.00
sellPrice = 1.25
buyValue = units * buyPrice
sellValue = units * sellPrice

def clearingFees(value, rate=0.0003):
# 0.03% of contract value, or a maximum of RM1000
    cF = value * rate
    return cF if cF < 1000 else 1000

def stampDuty(value):
# RM1 for every RM1000 contract value, up to maximum of RM200
    sD = value/1000
    if sD >= 200:
        return 200
    elif sD < 1:
        return 1
    return round(sD,0)

buySettlement = buyValue + (buyValue * brokerRate) + clearingFees(buyValue) + stampDuty(buyValue)
sellSettlement = sellValue - (sellValue * brokerRate) - clearingFees(sellValue) - stampDuty(sellValue)
netProfit = sellSettlement - buySettlement

print(f'Sell Settlement = {round(sellSettlement,2)}')
print(f'Buy Settlement = {round(buySettlement, 2)} \n')


print(f'Net Profit = {round(netProfit,2)}\n')

print(clearingFees(900))
print(clearingFees(1500))
print(clearingFees(21033000))