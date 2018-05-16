'''
compute the recall and precision  即计算招呼率和准确率
一般会选取不同长度N，计算出一组准确率/召回率然后画出准确率/召回率曲线(precision/recall curve)
RMSE主要是由于早起研究是基于电影评分而且netflix大赛也是米娜想评分预测问题，因而很多研究人员都将研究精力集中在优化评分预测的RMSE上
但亚马逊前科学家greglinden有不同的看法，推荐的主要目的是找到用户最优可能感兴趣的电影，而不是预测用户看了之后会给多少评分因此topN推荐更符合实际
的应用需求。也许有一部电影用户看了之后会给很高的份数，但用户看的可能性非常小。因此，预测用户是否会看一部电影比预测用户看了之后给什么评分更重要，因此，
建议使用topN推荐的评价
'''
def precisionRecall (test N):
hit=0
n_recall=0
n_precision=0 
for user ,items in test.items():
rnak=Recommend(user,N)#给用户推荐topN的产品
hit+=len(rqnk&items)#命中
n_reall+=len(items)# 测试集里面产品的个数
n_precision+=N
return[hit/(1.0*n_recall),hit/(2.0*n_precision)]
