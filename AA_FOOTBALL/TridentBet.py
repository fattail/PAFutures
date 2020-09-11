'''
Author: your name
Date: 2020-09-10 22:08:50
LastEditTime: 2020-09-10 23:34:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PAFutures\AA_FOOTBALL\TridentBet.py
'''
import numpy as np
import pandas as pd

v_win = 0.55
v_tie = 2.6
v_los = 6.5

tot_amt = 100
profit_ratio = 0.1

def GetTridentBet(v_win,v_tie,v_los,tot_amt,profit_ratio):

    tie_amt = tot_amt/(1+v_tie)
    bet_amt = tot_amt/(1+v_win-profit_ratio)
    hedge_amt = tot_amt-(tie_amt+bet_amt)

    AllocateList = pd.DataFrame([[bet_amt,tie_amt,hedge_amt]],columns=['攻投','平投','守投'])

    AllocateList['攻入'] = AllocateList['攻投']*(1+v_win)-tot_amt
    AllocateList['守入'] = AllocateList['守投']*(v_los)

    return AllocateList


GetTridentBet(0.7,2.8,3.75,10,0.1)