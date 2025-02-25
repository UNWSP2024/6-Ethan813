# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
STATE = 0.05
COUNTY =0.025
def salestax():
    sales = float(input('please enter the total sales for a month: '))
    state_tax = sales * STATE
    county_tax = sales * COUNTY
    print('state tax is $',state_tax,'county tax is $',county_tax)
    return state_tax + county_tax
print('total tax is $',salestax())
#ethan collins 2/25/2025 tax calc