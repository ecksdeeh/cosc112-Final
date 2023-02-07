import Taxes
def main():
  print('Welcome to the Income and Sales Tax Calculator! Please enter the following information as prompted below: ')
  print('===========================')
  total_income = float(input('Enter your total income below: '))
  if 0 <= total_income <=  9950:
    percent = 0.10
  elif 9951 <= total_income <=  40525:
    percent = 0.12
  elif 40526 <= total_income <=  86375:
    percent = 0.22
  elif 86376 <= total_income <=  164925:
    percent = 0.24
  elif 164926  <= total_income <=  209425:
    percent = 0.32
  elif 209426 <= total_income <=  523600:
    percent = 0.35
  elif total_income >= 523601:
    percent = 0.37
  sales_percent = 0.06
  
  retail = input('What store are you shopping at? ')
  total = int(input('Enter the total for the sale below: '))
  total_sales_tax = total + (total * sales_percent)
  total_taxes = total_income * percent
  
  t = Taxes.Taxes(percent, total_taxes)  
  st = Taxes.SalesTax(sales_percent, total_sales_tax, retail)
  
  print('Tax Percent Rate: ', t.Get_Tax_Percentage(), '%')
  print('Total Income Taxes: $', t.Get_Payment())
  print('Retailer: ', st.Get_Retail())
  print('Sales Tax Rate: ', st.Get_Tax_Percentage())
  print('Total Costs of product(s) with sales tax: $', st.Get_Payment())
  
main()
