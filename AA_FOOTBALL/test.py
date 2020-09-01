import pandas as pd
import numpy as np
import os as os

define_a=1.55
define_b=2.4
define_c=1.6

min_i = min(define_a,define_b,define_c)
max_i = max(define_a,define_b,define_c)
for t in [define_a,define_b,define_c]:
    if t != min(define_a,define_b,define_c) and t != max(define_a,define_b,define_c):
        mid_i = t

define_d=''
define_d=define_a*define_b*define_c/(define_a*define_b+define_a*define_c+define_b*define_c)

P_min_i=round(define_d/min_i,3)
P_mid_i=round(define_d/mid_i,3)
P_max_i=round(define_d/max_i,3)


pay=1
h=[]
for i in range (101):
    for ii in range (101):
        for iii in range (101):
            if i/100+ii/100+iii/100==1:
                h+=[i,ii,iii]
pay_list=pd.DataFrame(np.reshape(h,(len(h)//3,3)),columns=['min','mid','max'])#reshape矩阵重构（目标，行，列）
pay_list['index']=np.arange(len(pay_list))
pay_list['min_i_pay']=pay_list['min']+pay_list['min']*min_i
pay_list['mid_i_pay']=pay_list['mid']+pay_list['mid']*mid_i
pay_list['max_i_pay']=pay_list['max']+pay_list['max']*max_i
pay_list['down']= np.min([pay_list['min_i_pay'],pay_list['mid_i_pay']],axis=0)
pay_list_result = pay_list.loc[(pay_list['min_i_pay']>=100)&(pay_list['mid_i_pay']>=100),].sort_values(['down'],ascending=False).head(1)
print(pay_list_result)