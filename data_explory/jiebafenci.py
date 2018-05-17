from sklearn.feature_extraction.text import CountVectorizer# 类会将文本中的词语转换为词频矩阵
from sklearn.metrics.pairwise  import cosine_similarity#  计余弦相似度
from html  import data_html
#开始分词
wordslist = []  # 词列表
titlelist = []  # 文章抬头列表
word ={}
from sklearn.metrics.pairwise  import cosine_similarity
for title,neirong in data_html.items():
    titlelist.append(title)
    seg_list = jieba.cut(neirong, cut_all=False)  #  切词，方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
    result = '/'.join(seg_list)  # 输出分词的词组，本身是seg_list是一个生成器，需要for循环输出
    wordslist.append(result)
    #print('文章标题{}'.format(title ))
    # print('拆分词组{}'.format(wordslist))
    vectorizer = CountVectorizer() # 学习词语词典并返回文档矩阵，矩阵中元素为词语出现的次数。
    word_frequence = vectorizer.fit_transform(wordslist)  #one hot 编码
    print('词频矩阵{}'.format(word_frequence))# 输出文本包含词的频数，,即词在词组中位置，以及相应该词在文本中出现的次数
    words = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语 
    transformer = TfidfTransformer()  # 将文本频次转为词频矩阵
    print('词矩阵{}'.format(vectorizer.get_feature_names()))#输出词矩阵即分词后文章对应包含的词矩阵
    tfidf = transformer.fit_transform(word_frequence)#onehot编码 
    weight = tfidf.toarray()  #将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重 参考http://scikit-learn.org/stable/modules/feature_extraction.html
    print('词的tf-idf{}'.format(weight))# 输出词的tf-idf
    data_last=pd.DataFrame(weight) 
    print('type(weight)')    
    print(type(weight))
similarity={}    
if len (titlelist)>1:
    for title1 in titlelist:
        for title2 in titlelist:
            if title1 == title2: 
                continue
            similarity.setdefault(title1,{})
            similarity[title1].setdefault(title2,{})       
            similarity[title1][title2]=cosine_similarity(weight[titlelist.index(title1)].reshape(1,-1),weight[titlelist.index(title2)].reshape(1,-1))
print(similarity)# 输出文章相似度
print(similarity[278][279])
