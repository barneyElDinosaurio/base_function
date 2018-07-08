# -*-coding=utf-8-*-
# 书本《零起点python大数据与量化交易》
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
#mpl.style.use('seaborn-whitegrid')
class FinaceTool():
    # 每年追加存款
    def fuli(self):
        d1 = [np.fv(0.2, i, -1.4, -1.4) for i in range(1, 40)]
        # print(d1)
        d2 = [np.fv(0.15, i, -1.4, -1.4) for i in range(1, 40)]
        d3 = [np.fv(0.1, i, -1.4, -1.4) for i in range(1, 40)]
        d4 = [np.fv(0.05, i, -1.4, -1.4) for i in range(1, 40)]
        df = pd.DataFrame(columns=['d1','d2','d3','d4'])
        df['d1']=d1
        df['d2']=d2
        df['d3']=d3
        df['d4']=d4
        #print(df.tail())
        #df.plot()
        #plt.show()
        #
        #plt.savefig('data/fv1.png')
        #self.plot_style(df)
        self.style_color(df)

    def plot_style(self,data):

        for xss in plt.style.available:
            print(xss)
            plt.style.use(xss)
            data.plot()
            #plt.show()
            plt.savefig('data\\'+xss+'fv.png')

    def style_color(self,data):
        data.plot(colormap='Blues')
        plt.show()

    # 存多少年的利息
    def fuli2(self):
        d = 14000 * (1 + 0.05) ** 40
        print(d)




if __name__ == '__main__':
    obj = FinaceTool()

    obj.fuli()
    #obj.fuli2()
    #obj.style_color()