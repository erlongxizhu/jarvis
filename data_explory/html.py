from html.parser import HTMLParser   
import numpy as np
import pandas as pd 
import jieba  # 用于对文章内文本分词
# HtmlParser是一个类，在使用时一般继承它然后重载它的方法，来达到解析出需要的数据的目的。
# 　　　　handle_startendtag(tag, attrs) ，处理自己结束的标签，如<img />
# 　　　　handle_comment(data) ，处理注释，<!-- -->之间的文本

class hp(HTMLParser):
    a_text = True  # False
    tag_lag = 'p'  # 处理的标签
    def __init__(self):
        HTMLParser.__init__(self)
        self.a_data = ''  # 存放数据
        self.a_text = False
        self.tag_lag= ['p','br','span','h2']
    def handle_starttag(self,tag,attr):
        '''识别处理的开始标签
        :param tag: html的标签，比如<div> <p>
        :param attrs: 属性列表，以元组(属性，值)的方式展示，自动将二者转为小写
                      比如<p style="text-align: left;">，则attrs为[('style', 'text-align: left;')]
        :return:
        '''
        if tag in self.tag_lag:
            self.a_text = True
            # print (attr)             
    def handle_data(self,data):
        '''处理数据，识别html里面content string
        # 每一个标签，无论<> 还是</>，均会调用handle_data()，除非<></>中间无任何东西，开始结束都调用解析数据函数
        :param data: 标签之间的文本
        :return:
        '''
        if self.a_text: 
            if len(data.strip())==0:
                pass
            else:
                self.a_data=self.a_data + data.strip()# 文本合并   
    def handle_endtag(self,tag):
        '''识别处理的结束标签
        :param tag: 比如</div> </p>
        :return:
        '''
        if tag == self.tag_lag:
            self.a_text = False
            pass
#开始对上述数据进行解析

# data = pd.read_csv('C:\\Users\\liuxiangdong.ZAONLINE\\py_code\\MovieLens\\zhongan_dev_s_lxd_temp_05152_201805152.csv',header=None)
# print(data.head())
data_html= {}
page=['''<p>
    <br/>
</p>
<h2>
    辣椒吃太多易导致胃癌
</h2>
<p>
    <br/>
</p>

<p>
   天地玄黄。<br/>
</p>''',
'''<p>
    <br/>
</p>
<h2>
    辣椒吃太多易导致胃癌
</h2>
<p>
    <br/>
</p>

<p>
   阴阳无极。<br/>
</p>
''','''<p>
    <br/>
</p>
<h2>
    我爱你中国
</h2>
<p>
    <br/>
</p>
<p>
    陈凯歌得得张国荣。<br/>
</p>
''']
yk = hp() 
# 解析html语言里文章内容即文本
for i in [1,2,3]: # data.shape[0]
    yk.feed(page[i-1])
    yk.close()
    data_html.setdefault(277+i ,yk.a_data)
    yk.a_data=''
print(data_html)
print(len(data_html))
