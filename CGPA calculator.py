class LPU:
  def __init__(self):
    self.MTH174 = MTH174
    self.INT108 = INT108
    self.ECE249 = ECE249
    self.ECE279 = ECE279
    self.PES318 = PES318
    self.CHE110 = CHE110
    self.CSE326 = CSE326
    self.CSE111 = CSE111
  def CGPA(self):
    return (((self.MTH174*4)+(self.INT108*4)+(self.ECE249*4)+(self.ECE279*1)+(self.PES318*3)+(self.CHE110*2)+(self.CSE326*2)+(self.CSE111*2))/22)
MTH174=int(input("Enter grade of MTH174: "))
INT108=int(input("Enter grade of INT108: "))
ECE249=int(input("Enter grade of ECE249: "))
ECE279=int(input("Enter grade of ECE279: "))
PES318=int(input("Enter grade of PES318: "))
CHE110=int(input("Enter grade of CHE110: "))
CSE326=int(input("Enter grade of CSE326: "))
CSE111=int(input("Enter grade of CSE111: "))
Raj = LPU()
print("Your CGPA is:",Raj.CGPA())

