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
    近日|一组歌手陈红疑身患重病被送到急症室的照片在网上引发轩然大波。照片中的陈红表情痛苦|看起来十分虚弱。
</p>
<p>
    <br/>
</p>

    <br/>
</p>

<p>
    看来腰椎问题十分严重。<br/>
</p>
<p>
    <br/>
</p>
<p>
    <br/>
</p>
<section class="_135editor" data-tools="135编辑器" data-id="92152" style="border: 0px none;">
    <section class="_135editor" style="border: 0px none;">
        <section style="width:100%;min-width:300px;max-width: 750px;margin: 0 auto" data-width="100%">
            <section style="display: inline-block;width: auto;border-width:5px 20px;border-style: solid; -webkit-border-image: url(http://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9wbmcvdU4xTElhdjdvSmljT1RzODgya2wzUVVKaWNtZnVOVVExaWFzczkzRHI1SEVkTlp5Snl4bFMzMUExZ05RVFNzMXlnNkxBUGRTbnNZdnNqYTJzbEpEQjNUMHcvMD93eF9mbXQ9cG5n) 10 40;color: #6a6e6c;background-color: #edd50a;padding: 0 25px">
                <p style="margin: 0;white-space: nowrap;" class="135brush" data-brushtype="text">
                    据卫生部统计显示：
                </p>
            </section>
            <section style=" border-width:25px;border-style: solid; -webkit-border-image: url(http://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9wbmcvdU4xTElhdjdvSmljT1RzODgya2wzUVVKaWNtZnVOVVExaWF0T1FjakpGUGFoOEZVVElPNTJCUDdodEhYUTB5VXNmV0x0dk5YTDhnTjlTZzREOWljemdzQ1ZnLzA/d3hfZm10PXBuZw==) 40;padding-top:25px;font-size: 14px;color: #6d6c6a;background-color: #edd50a;line-height: 25px;text-align: justify;margin-top: -36px" class="135brush">
                <p>
                    我国腰椎病患者已突破2亿。我国30岁至40岁人群中|59.1%患有颈椎或腰椎疾病；50至60岁人群中|患此病者比例达到71%；60岁以上人群|该比例更攀至82%。
                </p>
            </section>
        </section>
    </section>
</section>
<p>
    <br/>
</p>s
<p>
    <strong>会导致瘫痪？</strong><br/>
</p>
<p>
    腰椎出现问题有极大可能导致腰椎间盘突出|如果进一步发展可能造成下身瘫痪。<br/>
</p>
''']
yk = hp() 
# 解析html语言里文章内容即文本

for i in [1,2]: # data.shape[0]
    yk.feed(page[i-1])
    yk.close()
    data_html.setdefault(277+i ,yk.a_data)
    yk.a_data=''
print(data_html)
print(len(data_html))
