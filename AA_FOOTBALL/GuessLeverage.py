import pandas as pd
import numpy as np
import os as os

def GetArbitrageKeep(v_win,v_tie,v_los,bet_amt,keep_side):

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
        OPTAllocateList['杠杆差'] = OPTAllocateList['最小胜'] - v_win

        return OPTAllocateList.loc[OPTAllocateList['最小胜'] == OPTAllocateList['最小胜'].min(),]

    elif keep_side == '留平':
        OPTAllocateList = AllocateList.loc[(AllocateList['胜利']>0) & (AllocateList['负利']>0),]

        OPTAllocateList['最小平'] = (OPTAllocateList['总出']/OPTAllocateList['平']) - 1
        OPTAllocateList['杠杆差'] = OPTAllocateList['最小平'] - v_tie

        return OPTAllocateList.loc[OPTAllocateList['最小平'] == OPTAllocateList['最小平'].min(),]
    elif keep_side == '留负':
        OPTAllocateList = AllocateList.loc[(AllocateList['平利']>0) & (AllocateList['胜利']>0),]

        OPTAllocateList['最小负'] = (OPTAllocateList['总出']/OPTAllocateList['负']) - 1
        OPTAllocateList['杠杆差'] = OPTAllocateList['最小负'] - v_los

        return OPTAllocateList.loc[OPTAllocateList['最小负'] == OPTAllocateList['最小负'].min(),]

# 波黑-波兰
GetArbitrage(1.6,2.125,1.8,100,'留胜') # 2.125
GetArbitrage(1.6,2.125,1.8,100,'留平') # 3.0
GetArbitrage(1.6,2.125,1.8,100,'留负') # 2.7

# 艾美尼亚
GetArbitrage(0.8,2.3,4,100,'留平')
GetArbitrageKeep(0.8,2.3,4,100,'留负')

56*(1+.8)-(56+31)

31*(1+2.3)-(56+31)

# --鹿儿岛
GetArbitrageKeep(1.15,2.25,1.875,10,'留平')

4.7*(1+1.15)-8.3-1
10.11/8.3
3.6*(1+1.875)-8.3-1

1*5.25-9.3

(4.7+3.6)/7

1.7*(1+7)-10

x*(1+7)=(4.7+3.6)+x