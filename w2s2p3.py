# Paste your code into this box
MIR=annualInterestRate/12.0
initbalance=balance
Mlb=balance/12
Mub=(balance*(1 +annualInterestRate )**12)/12.0
fixed=balance/12
while True:
    for i in range(12):
        balance=(balance-fixed)+((balance-fixed)*MIR)
    if abs(balance) < 0.1:
        print("Lowest Payment: ", round(fixed, 2))
        break
    else:
       
        if balance < 0:
            Mub = fixed
         
        elif balance > 0:
            Mlb = fixed
        
        
        fixed = (Mlb + Mub)/2
        balance = initbalance
