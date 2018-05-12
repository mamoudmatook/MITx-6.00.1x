mir=annualInterestRate/12.0
initbalance=balance
mfmp=10.0
while True:
       for i in range(1,13):
            mub=balance-mfmp
            balance=mub+mir*mub
       if balance<=0:
            print("Lowest Payment: "+str(mfmp))
            break
       else:
            balance=initbalance
            mfmp=mfmp+10.0
