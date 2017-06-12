#coding:utf-8
__author__ = 'liuguiru'
import jieba    #分词包
import numpy    #numpy计算包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import pandas
import matplotlib.pyplot as plt
from itertools import *
#%matplotlib inline
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

from wordcloud import WordCloud#词云包


file=codecs.open(u"his.txt",'r')
content=file.read()
file.close()
#jieba.load_userdict(u"西游记分词.txt")
segment=[]
segs=jieba.cut(content)
for seg in segs:
    if len(seg)>1 and seg!='\r\n':
        segment.append(seg)


words_df=pandas.DataFrame({'segment':segment})
#print words_df.head()
stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="utf8")#quoting=3全不引用
#print stopwords.head(50)
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
ancient_chinese_stopwords=pandas.Series(['之','其','或','亦','方','于','即','皆','因','仍','故','尚','呢','了','的','着','一'
                           ,'不','乃','呀','吗',
                            '咧','啊','把','让','向','往','是','在','越','再',
                           '更','比','很','偏','别','好','可','便','就','但','儿','又','也','都','我','他','来','" "'])
words_df=words_df[~words_df.segment.isin(ancient_chinese_stopwords)]


words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort_index(ascending=False)
#print words_stat.head(20)


wordcloud=WordCloud(font_path="simhei.ttf",background_color="black")

xxx =  words_stat.head(39769).itertuples(index=False)
class YYY:
    def __init__(self, xxx):
        self.xxx = xxx
    def items(self):
        return list(self.xxx)
yyy = YYY(xxx)
#wordcloud=wordcloud.fit_words(yyy)
#plt.imshow(wordcloud)
#plt.show()

from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
bimg=imread('xixi2.png')
wordcloud=WordCloud(background_color="white",mask=bimg,font_path='simhei.ttf')
wordcloud=WordCloud(mask=bimg,font_path='simhei.ttf')
wordcloud=wordcloud.fit_words(yyy)
bimgColors=ImageColorGenerator(bimg)
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()