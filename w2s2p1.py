def func(balance,annualInterestRate,monthlyPaymentRate):
    mir=annualInterestRate/12.0
    i=1
    while i<13:
        mmp=monthlyPaymentRate*balance
        mup=balance-mmp
        balance=mup+mir*mup
        i=i+1
    
    print("Remaining balance: " + str(round(balance,2)))
func(42,.2,.04)


