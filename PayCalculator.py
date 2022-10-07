'''
A simple app to calculate a non-excempt TM's hourly wage

Author: Thomas Tarango
Date: September 14th, 2022
'''

loop = True
while loop:
    try:
        rate = float(input('Enter Hourly Wage: '))
        assert rate > 0
        loop = False
    except:
        print('You must enter a valid number greater than zero.')
        
def pay(rate):
    '''
    Prints adjusted hourly wage and weekly pay based on payrate*hours+payrate*ot
    Precondition: rate must be a float
    
    Variable bHours: normal hours worked for B keys
    Variable bOT: overtime hours worked for B keys
    Variable bDiff: pay differential for B2
    
    Variable aHours: normal hours worked for A keys
    Variable aOT: overtime hours worked for A keys
    Variable aDiff: pay differential for A keys
    '''
    bHours = 32
    bOT = 8
    bDiff = 1
    aHours = 24
    aOT = 10.5
    aDiff = 2
    
    #overtime hours are paid at 1.5x the rate of base pay
    b1 = (rate*bHours)+(rate*bOT*1.5) 
    #b2 receives same pay as B1 + $1 differential for all hours worked
    b2 = b1 + (bDiff*(bHours+bOT)) 
    #both A1/A2 receives same differential and pay
    a = (rate*aHours)+(rate*aOT*1.5)+(aDiff*(aHours+aOT)) 
    
    print("\n")
    print("B1 Tues-Fri 6AM - 4:30PM")
    print(f"Adjusted Wage: ${round((b1/40), 2)}")
    print(f"Weekly Income: ${round(b1, 2)}")
    print(f"Monthly Income: ${round((b1 * 4), 2)}")
    print("\n")

    print("B2 Tues-Fri 4:30PM - 3AM")
    print(f"Adjusted Wage: ${round(((b2 + 40)/40), 2)}")
    print(f"Weekly Income: ${round((b2 + 40), 2)}")
    print(f"Monthly Income: ${round(((b2 * 4) + 160), 2)}")
    print("\n")

    print("A1 Sat-Mon 6AM - 6PM")
    print(f"Adjusted Wage: ${round((a/34.5), 2)}")
    print(f"Weekly Income: ${round((a), 2)}")
    print(f"Monthly Income: ${round((a * 4), 2)}")
    print("\n")

    print("A2 Sat-Mon 6AM - 6PM")
    print(f"Adjusted Wage: ${round((a/34.5), 2)}")
    print(f"Weekly Income: ${round((a), 2)}")
    print(f"Monthly Income: ${round((a * 4), 2)}")
    print("\n")
    
    
pay(rate)
    