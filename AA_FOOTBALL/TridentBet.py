'''
Author: Ray
Date: 2020-09-10 22:08:50
LastEditTime: 2020-09-10 23:34:29
LastEditors: Ray
Description: In User Settings Edit
FilePath: \PAFutures\AA_FOOTBALL\TridentBet.py
'''
import numpy as np
import pandas as pd

v_win = 1.15
v_tie = 3.2
v_los = 1.51

tot_amt = 100
profit_ratio = 0.1

def GetTridentBet(game_info,v_win,v_tie,v_los,tot_amt,profit_ratio):
    if (v_win<v_tie) & (v_tie<v_los):
        tie_amt = round(tot_amt/(1+v_tie),2)
        bet_amt = round(min(tot_amt*(1+profit_ratio)/(1+v_win),10-tie_amt),2)
        hedge_amt = max(round(tot_amt-(tie_amt+bet_amt),2),0)

        AllocateList = pd.DataFrame([[game_info,v_win,v_tie,v_los,bet_amt,tie_amt,hedge_amt]],columns=['比赛','胜赔','平赔','负赔','胜投','平投','负投'])

        AllocateList['胜入'] = round(AllocateList['胜投']*(1+v_win)-tot_amt,2)
        AllocateList['平入'] = round(AllocateList['平投']*(1+v_tie)-tot_amt,2)
        AllocateList['负入'] = round(AllocateList['负投']*(1+v_los)-tot_amt,2)

        AllocateList['最大损失'] = AllocateList['负入']

        AllocateList['对冲最小赔率'] = np.round(tot_amt/AllocateList['负投']-1,2)

        #AllocateList['投产比'] = np.round(AllocateList['攻入']/abs(np.min(AllocateList['守入'],0)),2)

        return AllocateList
    
    elif (v_los<v_tie) & (v_tie<v_win):
        tie_amt = round(tot_amt/(1+v_tie),2)
        bet_amt = round(min(tot_amt*(1+profit_ratio)/(1+v_los),10-tie_amt),2)
        hedge_amt = max(round(tot_amt-(tie_amt+bet_amt),2),0)

        AllocateList = pd.DataFrame([[game_info,v_win,v_tie,v_los,hedge_amt,tie_amt,bet_amt]],columns=['比赛','胜赔','平赔','负赔','胜投','平投','负投'])

        AllocateList['胜入'] = round(AllocateList['胜投']*(1+v_win)-tot_amt,2)
        AllocateList['平入'] = round(AllocateList['平投']*(1+v_tie)-tot_amt,2)
        AllocateList['负入'] = round(AllocateList['负投']*(1+v_los)-tot_amt,2)

        AllocateList['最大损失'] = AllocateList['胜入']

        AllocateList['对冲最小赔率'] = np.round(tot_amt/AllocateList['胜投']-1,2)

        #AllocateList['投产比'] = np.round(AllocateList['攻入']/abs(np.min(AllocateList['守入'],0)),2)

        return AllocateList
    
    else:
        win_amt = round(tot_amt*(1+profit_ratio)/(1+v_win),2)

        los_amt = round(tot_amt*(1+profit_ratio)/(1+v_los),2)

        hedge_amt = round(max(tot_amt - win_amt - los_amt,0),2)

        AllocateList = pd.DataFrame([[game_info,v_win,v_tie,v_los,win_amt,hedge_amt,los_amt]],columns=['比赛','胜赔','平赔','负赔','胜投','平投','负投'])

        AllocateList['胜入'] = AllocateList['胜投']*(1 + v_win) - tot_amt
        AllocateList['负入'] = AllocateList['负投']*(1 + v_los) - tot_amt
        AllocateList['平入'] = AllocateList['平投']*(1 + v_tie) - tot_amt

        AllocateList['最大损失'] = AllocateList['平入']

        AllocateList['对冲最小赔率'] = np.round(tot_amt/AllocateList['平投']-1,2)

        #AllocateList['投产比'] = np.round(((AllocateList['攻胜入']+AllocateList['攻负入'])/2)/abs(np.min(AllocateList['平入'],0)),2)

        return AllocateList

info_lst = [
#['冠军联赛-奥摩尼亚-贝尔格莱德红星',2.5,2.25,1.25],
#['中国超级联赛-青岛黄海制药-重庆斯威',2.7,2.5,0.95],
['中国超级联赛-天津泰达-石家庄永昌',2.6,2.7,0.925],
['日本职业联赛J1-FC东京-大分三神',0.7,2.8,3.75],
#['日本职业联赛J1-神户胜利船-大阪樱花',1.45,2.6,1.7],
['日本职业联赛J1-横滨水手-清水心跳',0.5,4,4.25],
#['日本职业联赛J1-鸟栖沙岩-札幌冈萨多FC',1.7,2.5,1.5],
#['南韩职业联赛-釜山偶像-江原',1.75,2.3,1.6],
#['南韩职业联赛-仁川联-首尔FC',2.1,2.1,1.5],
['南韩职业联赛-水原三星蓝翼-浦项制铁',2.5,2.5,1.1],
#['南韩职业联赛-大邱-城南一和天马',1.05,2.3,2.9],
#['日本职业联赛J2-大宫松鼠-福冈黄蜂',1.375,2,2.2],
['中国甲级联赛-杭州绿城-江西联盛',0.222,4.75,10],
['中国甲级联赛-安徽力天-四川九牛',2.25,2.6,1],
['中国甲级联赛-成都兴城-北京北体大',0.571,2.8,4.5],
['俄罗斯杯-FK Leninggradets-乌法',4,2.4,0.6],
['澳大利亚昆士兰州联赛-伊普斯维奇骑士-洛根利泰柠',3.2,3.5,0.615],
['澳大利亚昆士兰州联赛-阳光海岸流浪者-布里斯班市',0.95,3.1,2.1],
['智利甲级联赛-帕莱斯蒂诺-伊库伊奎',0.727,2.7,3.6],
['冰岛甲级联赛-格连戴域克-莱尼雷克查域克',1.5,2.4,1.45],
#['芬兰甲级联赛-瓦萨-奥陆',2.6,2.5,1],
['芬兰甲级联赛-科特卡-吉尼斯坦',0.364,4,7],
['斯洛文尼亚杯-Nd Ilirija-多姆萨莱',7,4.5,0.222],
['波兰丁级联赛-Pomorzanin Torun-Unia Janikowo',1.4,2.4,1.55],
['波兰丁级联赛-卢宾盆地II-Polonia-Stal Swidnica',0.7,2.8,3],
['波黑超级联赛-奥林匹克萨拉热窝-萨拉热窝',5,3.1,0.4],
#['埃及联赛-高纳-史莫哈',1.625,1.8,2],
['克罗地亚乙级联赛-杜国坡吉-奥西耶克II',1.5,2.25,1.5],
#['克罗地亚乙级联赛-萨格勒布迪纳摩II-鲁达士',1.05,2.2,2.4],
['克罗地亚乙级联赛-古斯图西加-杜布后瓦',1.25,2.2,1.9],
['克罗地亚乙级联赛-NK祖纳克-NK克罗地亚 Zmijavci',1.75,2.1,1.4],
['克罗地亚乙级联赛-BSK比耶洛波布尔多-索林',0.95,2.25,2.6],
['泰国甲级联赛-清迈FC-拉纳维',1.15,2.3,2.25],
['泰国甲级联赛-农业大学-清迈连',3,2.4,0.87],
['日本天皇杯-奈良俱乐部-Ococias Kyoto',0.7,2.9,3.8]]

tmp_df = pd.DataFrame(columns=['比赛','胜赔','平赔','负赔','胜投','平投','负投','胜入','平入','负入','最大损失','对冲最小赔率'])
for ix in info_lst:
    tmp_df = pd.concat([tmp_df,GetTridentBet(ix[0],ix[1],ix[2],ix[3],10,0.1)])

tmp_df.sort_values('最大损失',ascending=False)