import pandas as pd
import numpy as np
import os as os

def GetLverage(v_win,v_tie,v_los,bet_amt,keep_side):

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
GetArbitrage(1.55,2.125,1.875,100,'留胜') # 2.125
GetArbitrage(1.55,2.125,1.875,100,'留平') # 3.0
GetArbitrage(1.55,2.125,1.875,100,'留负') # 2.7



