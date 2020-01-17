from sympy import *
def Pt100():
    A,B,C,R0 = 3.94*10**-3,-5.802*10**-7,-4.274*10**-12,100
    x,y = symbols('x,y')
    f1,f2 = R0+R0*A*x+R0*B*x**2-y,R0+R0*A*x+R0*B*x**2+R0*C*(x-100)**3-y
    if input('是否改变温度系数:') == '1' :
        A,B,C,R0 = int(input('输入系数A：')),int(input('输入系数B：')),int(input('输入系数C：')),int(input('输入铂电阻零度时电阻：'))
    Rt = input('输入数值，请务必输入单位：')
    Temperture = float(Rt[:-1])
    if Rt[-1] == 'r' or Rt[-1] == 'R':
        f3 = Temperture-y
        if Temperture >=100 :
            Temperture = solve([f1,f3],(x,y))
            Temperture = min(Temperture[0][0],Temperture[1][0])
        elif Temperture <100 :
            Temperture = solve([f2,f3],(x,y))
            Temperture = [Temperture[i][0].args[0] for i in range(len(Temperture)) if (Temperture[i][0].args[0]>-273.15 and Temperture[i][0].args[0]<850)]
    elif Rt[-1] == 'k' or Rt[-1] == 'K' or Rt[-1] == 'c' or Rt[-1] == 'C':
        if Rt[-1] == 'k' or Rt[-1] == 'K':
            Temperture = Temperture-273.15
        if Temperture >=0 :
            f3 = x-Temperture
            if Temperture >= 850 :
                print ('输入温度高于850度公式可能失效，输出值可能有较大误差，请注意')  
            Temperture = solve([f1,f3],(x,y))[0][1]
        elif Temperture <0 :
            f3 = x+Temperture
            if Temperture <= -200:
                print ('输入温度低于-200度公式可能失效，输出值可能有较大误差，请注意')
            Temperture = solve([f2,f3],(x,y))[0][1]
    print(Temperture)
    return 1
def Pt1000():
    return print('2')
def Diode():
    return print('3')
def Exit():
    Sign = 0
    return Sign
Sign = 1 
Switch = {'pt100':Pt100,'pt1000':Pt1000,'diode':Diode,'exit':Exit}
if __name__ == '__main__' :
    while (Sign):
        Cat = input('输入测温类型：')
        try:
            Sign = Switch.get(Cat)()
        except KeyError as e:
            pass