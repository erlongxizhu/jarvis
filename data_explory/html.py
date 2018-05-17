#-*-coding:utf-8-*-
from html.parser import HTMLParser  #sh使用解模块解析html语言 
#    HtmlParser是一个类，在使用时一般继承它然后重载它的方法，来达到解析出需要的数据的目的。
# 　handle_startendtag(tag, attrs) ，处理自己结束的标签，如<img />
# 　handle_comment(data) ，处理注释，<!-- -->之间的文本

class hp(HTMLParser):
    a_text = True  # False
    def __init__(self):
        HTMLParser.__init__(self)
        self.a_data = ''  # 存放数据
        self.a_text = False
        self.tag_lag= ['p','br','section','span','h2']  ## 处理的标签
        
        
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
<section class=""_135editor"" data-tools=""135编辑器"" data-id=""25463"" style=""border: 0px none;"">
    <section style=""border: 0px rgb(40, 127, 180); margin: 0px; overflow: hidden; padding: 0px;"">
        <section style=""display: inline-block; font-size: 1em; font-family: inherit; font-weight: inherit; text-align: inherit; text-decoration: inherit; color: rgb(254, 254, 254); border-color: rgb(40, 127, 180); background-color: transparent;"">
            <section class=""135brush"" data-bcless=""darken"" data-brushtype=""text"" style=""border-left: 8px solid rgb(21, 68, 97); border-top-color: rgb(21, 68, 97); border-right-color: rgb(21, 68, 97); border-bottom-color: rgb(21, 68, 97); display: inline-block; line-height: 1.4em; padding: 5px 10px; height: 32px; vertical-align: top; font-size: 16px; font-family: inherit; font-weight: bold; float: left; color: inherit; background: rgb(40, 127, 180); box-sizing: border-box !important;"">
                流言
            </section>
            <section style=""width: 0.5em; display: inline-block; height: 32px; vertical-align: top; border-bottom: 1em solid rgb(40, 127, 180); border-top: 1em solid rgb(40, 127, 180); font-size: 16px; border-left-color: rgb(40, 127, 180); color: inherit; box-sizing: border-box !important; border-right: 1em solid transparent !important;""></section>
        </section>
    </section>
</section>
<p>
    有报道称|研究发现辣椒可能导致胃癌|最好拒绝这辛辣的味道胃癌胃癌胃癌胃癌胃癌胃癌胃癌。<br/>
</p>
''','''<p>
    <br/>
</p>
<h2>
    辣椒吃太多易导致胃癌
</h2>
<p>
    <br/>
</p>
<section class=""_135editor"" data-tools=""135编辑器"" data-id=""25463"" style=""border: 0px none;"">
    <section style=""border: 0px rgb(40, 127, 180); margin: 0px; overflow: hidden; padding: 0px;"">
        <section style=""display: inline-block; font-size: 1em; font-family: inherit; font-weight: inherit; text-align: inherit; text-decoration: inherit; color: rgb(254, 254, 254); border-color: rgb(40, 127, 180); background-color: transparent;"">
            <section class=""135brush"" data-bcless=""darken"" data-brushtype=""text"" style=""border-left: 8px solid rgb(21, 68, 97); border-top-color: rgb(21, 68, 97); border-right-color: rgb(21, 68, 97); border-bottom-color: rgb(21, 68, 97); display: inline-block; line-height: 1.4em; padding: 5px 10px; height: 32px; vertical-align: top; font-size: 16px; font-family: inherit; font-weight: bold; float: left; color: inherit; background: rgb(40, 127, 180); box-sizing: border-box !important;"">
                流言
            </section>
            <section style=""width: 0.5em; display: inline-block; height: 32px; vertical-align: top; border-bottom: 1em solid rgb(40, 127, 180); border-top: 1em solid rgb(40, 127, 180); font-size: 16px; border-left-color: rgb(40, 127, 180); color: inherit; box-sizing: border-box !important; border-right: 1em solid transparent !important;""></section>
        </section>
    </section>
</section>
<p>
    有报道称|研究发现辣椒可能导致胃癌|最好拒绝这辛辣的味道味道味道味道味道味道味道。<br/>
</p>
''']
yk = hp() # 实例化hp类
# 解析html语言里文章内容即文本
for i in [1,2]: 
    yk.feed(page[i-1])
    yk.close()
    data_html.setdefault(277+i ,yk.a_data)
    yk.a_data=''
print(data_html)

#{278: '辣椒吃太多易导致胃癌流言有报道称|研究发现辣椒可能导致胃癌|最好拒绝这辛辣的味道胃癌胃癌胃癌胃癌胃癌胃癌胃癌。', 279: '辣椒吃太多易导致胃癌流言有报道称|研究发现辣椒可能导致胃癌|最好拒绝这辛辣的味道味道味道味道味道味道味道。'}
print(len(data_html))#输出解析后的长度
