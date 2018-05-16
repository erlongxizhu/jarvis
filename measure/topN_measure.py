py'''
this python file is used to compute measure of the rec system whcich use rmse and mae
imput records : whichi has two columns the first is the truth ui（实际值） and the second is the predict of ui （预测值）
'''
import math
def rmse(records):
    return math.sqrt(sum(rui-pui)*(rui-pui)   for rui,pui in records )/float(len(records
def mae(records):
    return math.sqrt(sum(rui-pui)   for rui,pui in records )/float(len(records)
