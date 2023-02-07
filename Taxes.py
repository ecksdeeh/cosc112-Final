class Taxes:
  def __init__(self, tp, top):
    self.__Tax_Percentage = tp
    self.__Total_Payment = top
  def Set_Tax_Percentage(self, tp):
    self.__Tax_Percentage = tp
  def Get_Tax_Percentage(self):
    return self.__Tax_Percentage
  def _Set_Payment(self, top):
    self.__Total_Payment = top
  def Get_Payment(self):
    return self.__Total_Payment
  
  
class SalesTax(Taxes):
  def __init__(self, tp, top, r):
    Taxes.__init__(self, tp, top)
    self.__Total_Payment = top
    self.__Retail = r
  def Set_Retail(self, r):
    self.__Retail = r
  def Get_Retail(self):
    return self.__Retail
  def Set_Payment(self, top):
    self.__Total_Payment = top
  def Get_Payment(self):
    return self.__Total_Payment
  
