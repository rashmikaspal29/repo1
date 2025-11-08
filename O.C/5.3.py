def main():
    initialInv = float(input("Enter initial investment: "))
    annualRate = float(input("Enter the annual interest rate: "))
    monthlyRate = annualRate / 1200 #here annualRate is in percentage & equals(annualRate/100)/12: 5% = 5/100
    totalBalance = initialInv # we need to initialize the totalbalance to get the actual total
    target = initialInv * 2
    months = 0

    while totalBalance < target: #if totalBalance > target, it stops.
        totalBalance = totalBalance + (totalBalance * monthlyRate)
        months += 1
    
    years = months // 12
    month = months % 12  #all months convert to year and remaining becomes main
    print(f"After {years} years and {month} months, balance is $ {totalBalance:.2f}")
main()




