'''
@Author: your name
@Date: 2019-11-26 20:24:29
@LastEditTime: 2019-11-26 22:14:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\function\mergeStone.py
'''
'''
    购买1级石头
'''
l1_value = 0.75 # 1颗1级石头消耗0.75金
l1_value_diamond = 8 # 1颗1级石头同时还需要消耗8颗钻石

'''
    1级合成3级
'''
l1_to_l3 = 12 # 1颗1级石头变成1颗3级石头，需要消耗12颗1级石头
l1_to_l3_gold = 0.39 # 同时还需要消耗0.39金
l1_to_l3_vit = 10 # 同时还需要消耗10点体力

'''
    3级合成4级
'''
l3_to_l4 = 16 # 1颗3级石头变成1颗4级石头，需要消耗16个1级石头
l3_to_l4_gold = 0.897 # 1颗3级石头变成1颗4级石头，需要消耗0.897金
l3_to_l4_vit = 10
l3_to_l4_rate = 0.4878 # 1颗3级石头变成1颗4级石头，成功概率只有0.4878，并非100%
                        # 如果失败，则金和16颗1级五行石也将被扣除，但不消耗体力

'''
    四级合成6级
'''
l4_to_l6 = 12 # 1颗4级石头变成6级石头，概率为100%，需要消耗12颗4级石头
l4_to_l6_gold = 19.75 #需要消耗 19.75金
l4_to_l6_vit = 10

'''
已知1颗6级石头的市场售价为750金，请问是自己合成石头划算还是直接购买划算
其他数据：
    1颗砖石diamond 卖出 0.05金
    1点体力vit 可以卖出 1金
'''
def l1_merge_l3(l3num):
    stone = l3num * 13
    gold = l3num * 0.39
    vit = l3num * 10
    return stone, gold, vit

def l3_merge_l4(l4num):
    l4CostNum /= 0.4878;
    stone, gold, vit = l1_merge_l3(l4CostNum)
    stone += l4CostNum * 16;
    gold += l4CostNum * 0.897;
    vit += l4num * 10;
    return stone, gold, vit

def l4_merge_l6(l6num):
    stone, gold, vit = l3_merge_l4(l6num * (1 + 12))
    gold += 19.75
    vit += 10
    return stone, gold, vit

def calc_gold(stone, vit):
    diamond = stone * 8
    gold = diamond * 0.05 + stone * 0.75 + vit * 1
    return gold

stone, gold, vit = l4_merge_l6(1)
total_gold = gold + calc_gold(stone, vit)
print("total_gold=%f, stone=%f, gold=%f, vit=%f" % (total_gold, stone, gold, vit))