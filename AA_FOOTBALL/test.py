import pandas as pd
import numpy as np
import os as os

define_a=1.45
define_b=2.4
define_c=1.8

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

h

AllocateList = pd.DataFrame(np.reshape(h,(len(h)//3,3)),columns=['胜','平','负'])

AllocateList.to_csv(r'./data/cmb_list.csv',index=None)

v_win = 1.45
v_tie = 2.4
v_los = 1.8

bet_amt = 200

def GetArbitrage(v_win,v_tie,v_los,bet_amt,keep_side):

    AllocateList = pd.read_csv(r'./data/cmb_list.csv',index_col=None)

    AllocateList['胜'] = (AllocateList['胜']*bet_amt)/100
    AllocateList['平'] = (AllocateList['平']*bet_amt)/100
    AllocateList['负'] = (AllocateList['负']*bet_amt)/100

    AllocateList['胜入'] = AllocateList['胜']*(v_win+1)
    AllocateList['平入'] = AllocateList['平']*(v_tie+1)
    AllocateList['负入'] = AllocateList['负']*(v_los+1)

    AllocateList['总出'] = AllocateList['胜'] + AllocateList['平'] + AllocateList['负']

    AllocateList['胜利'] = AllocateList['胜入'] - AllocateList['总出']
    AllocateList['平利'] = AllocateList['平入'] - AllocateList['总出']
    AllocateList['负利'] = AllocateList['负入'] - AllocateList['总出']

    if keep_side == '留胜':
        OPTAllocateList = AllocateList.loc[(AllocateList['平利']>0) & (AllocateList['负利']>0),]

        OPTAllocateList['最小胜'] = (OPTAllocateList['总出']/OPTAllocateList['胜']) - 1

        return OPTAllocateList.loc[OPTAllocateList['最小平'] == OPTAllocateList['最小平'].min(),]

    elif keep_side == '留平':
        OPTAllocateList = AllocateList.loc[(AllocateList['胜利']>0) & (AllocateList['负利']>0),]

        OPTAllocateList['最小平'] = (OPTAllocateList['总出']/OPTAllocateList['平']) - 1

        return OPTAllocateList.loc[OPTAllocateList['最小平'] == OPTAllocateList['最小平'].min(),]
    elif keep_side == '留负':
        OPTAllocateList = AllocateList.loc[(AllocateList['平利']>0) & (AllocateList['胜利']>0),]

        OPTAllocateList['最小负'] = (OPTAllocateList['总出']/OPTAllocateList['负']) - 1

        return OPTAllocateList.loc[OPTAllocateList['最小平'] == OPTAllocateList['最小平'].min(),]


(OPTAllocateList['总出']/AllocateList['平']) - 1

OPTAllocateList['最小平'] = (OPTAllocateList['总出']/OPTAllocateList['平']) - 1

OPTAllocateList.loc[OPTAllocateList['最小平'] == OPTAllocateList['最小平'].min(),]

max_c = AllocateList.loc[(AllocateList['胜利']>0) & (AllocateList['负利']>0),'平'].max()

AllocateList.loc[(AllocateList['胜利']>0) & (AllocateList['负利']>0)&(AllocateList['平']==max_c),]

OPTAllocateList['均差'] = np.std(OPTAllocateList[['胜利','平利','负利']],axis=1)

min_std = OPTAllocateList['均差'].min()

return OPTAllocateList.loc[OPTAllocateList['均差']==min_std,]

def GetArbitrage(v_win,v_tie,v_los,bet_amt):

    AllocateList = pd.read_csv(r'./data/cmb_list.csv',index_col=None)

    AllocateList['胜'] = (AllocateList['胜']*bet_amt)/100
    AllocateList['平'] = (AllocateList['平']*bet_amt)/100
    AllocateList['负'] = (AllocateList['负']*bet_amt)/100

    AllocateList['胜入'] = AllocateList['胜']*(v_win+1)
    AllocateList['平入'] = AllocateList['平']*(v_tie+1)
    AllocateList['负入'] = AllocateList['负']*(v_los+1)

    AllocateList['胜利'] = AllocateList['胜入'] - AllocateList['平'] - AllocateList['负']
    AllocateList['平利'] = AllocateList['平入'] - AllocateList['胜'] - AllocateList['负']
    AllocateList['负利'] = AllocateList['负入'] - AllocateList['胜'] - AllocateList['平']

    OPTAllocateList = AllocateList.loc[(AllocateList['胜利']>AllocateList['胜'])&
                                (AllocateList['平利']>AllocateList['平'])&
                                (AllocateList['负利']>AllocateList['负']),]

    OPTAllocateList['均差'] = np.std(OPTAllocateList[['胜利','平利','负利']],axis=1)

    min_std = OPTAllocateList['均差'].min()

    return OPTAllocateList.loc[OPTAllocateList['均差']==min_std,]

BinaryDF = pd.DataFrame([[ix,100-ix] for ix in np.arange(0,101)],columns=['胜','负'])

h=[]
for i1 in range (101):
    for i2 in range (101):
        for i3 in range (101):
            for i4 in range (101):
                if i1/100+i2/100+i3/100+i4/100==1:
                    h+=[i,i2,i3,i4]

AllocateList = pd.DataFrame(np.reshape(h,(len(h)//4,4)),columns=['小左','小','大','大右'])


v_s_left = 1.9
v_s = 0.364
v_b = 0.3
v_b_right = 70

AllocateList['小左入'] = AllocateList['小左']*(v_s_left+1)
AllocateList['小入'] = AllocateList['小']*(v_s+1)
AllocateList['大入'] = AllocateList['大']*(v_b+1)
AllocateList['大右入'] = AllocateList['大右']*(v_b_right+1)

AllocateList['小左利'] = AllocateList['小左入'] - AllocateList['小左'] - AllocateList['小'] - AllocateList['大'] - AllocateList['大右']
AllocateList['小利'] = AllocateList['小入'] - AllocateList['小左'] - AllocateList['小'] - AllocateList['大'] - AllocateList['大右']
AllocateList['大利'] = AllocateList['大入'] - AllocateList['小左'] - AllocateList['小'] - AllocateList['大'] - AllocateList['大右']
AllocateList['大右利'] = AllocateList['大右入'] - AllocateList['小左'] - AllocateList['小'] - AllocateList['大'] - AllocateList['大右']

AllocateList.loc[(AllocateList['小左利']>0)&
                (AllocateList['小利']>0)&
                (AllocateList['大利']>0)&
                (AllocateList['大右利']>0),]


[[1.875,2,1.55],
[],]

# 爱媛-町田泽维亚
GetArbitrage(1.9,2,1.55,10)

# 甲府风林-草津温泉
GetArbitrage(1.05,2.3,2.6,10)

# 德岛漩涡-水户霍力克
GetArbitrage(0.8,2.5,3.333,10)

# 德岛漩涡-水户霍力克
GetArbitrage(0.75,2.7,3.4,100)

# 栎木-北九州向日葵
GetArbitrage(2.2,1.9,1.4,10)

# 金泽赛维根-琉球足球俱乐部
GetArbitrage(1.3,2.75,2.5,10)

# 冈山-松本山雅
GetArbitrage(1.55,1.9,2,10)

# 山形山神-雷法山口
GetArbitrage(0.727,2.6,3.75,10)

GetArbitrage(0.003,1,15,2.4)


max_income = np.std(AllocateList.loc[(AllocateList['胜入']>0)&
                (AllocateList['平入']>0)&
                (AllocateList['负入']>0),['胜入','平入','负入']],axis=1)

AllocateList.loc[(AllocateList['胜入']>0)&
                (AllocateList['平入']>0)&
                (AllocateList['负入']>0)&
                (AllocateList['均入']==max_income),]

df = AllocateList.pivot(values=['胜入','平入','负入'])

sns.lineplot(data=df, x='x', y='y', hue='color')

df = AllocateList.pivot(index='x', columns='color', values='y')



pay_list=pd.DataFrame(np.reshape(h,(len(h)//3,3)),columns=['min','mid','max'])#reshape矩阵重构（目标，行，列）
pay_list['index']=np.arange(len(pay_list))
pay_list['min_i_pay']=pay_list['min']+pay_list['min']*min_i
pay_list['mid_i_pay']=pay_list['mid']+pay_list['mid']*mid_i
pay_list['max_i_pay']=pay_list['max']+pay_list['max']*max_i
pay_list['down']= np.min([pay_list['min_i_pay'],pay_list['mid_i_pay']],axis=0)
pay_list_result = pay_list.loc[(pay_list['min_i_pay']>=100)&(pay_list['mid_i_pay']>=100),].sort_values(['down'],ascending=False).head(1)
print(pay_list_result)


#-----------------
import pandas as pd
import numpy as np
import os as os

define_a=1.45
define_b=2.4
define_c=1.8

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


GetArbitrage(0.118,4.75,22,10)