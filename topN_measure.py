py'''
this python file is used to compute measure of the rec system whcich use rmse and mae
imput records : whichi has two columns the first is the truth ui��ʵ��ֵ�� and the second is the predict of ui ��Ԥ��ֵ��
'''
import math
def rmse(records):
    return math.sqrt(sum(rui-pui)*(rui-pui)   for rui,pui in records )/float(len(records
def mae(records):
    return math.sqrt(sum(rui-pui)   for rui,pui in records )/float(len(records)