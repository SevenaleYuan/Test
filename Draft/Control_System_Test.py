import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import control as ctrl

#分子多项式系数
numerator = [1,1]

#分母多项式系数
denominator = [1,5,6,0]

sys = ctrl.TransferFunction(numerator, denominator)

plt.figure()
ctrl.root_locus(sys)

plt.savefig("rootlocus.png")
print("Figure has been saved.")