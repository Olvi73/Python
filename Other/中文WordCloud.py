import wordcloud,cv2
import jieba

str=jieba.lcut('此情可待成追忆,只是当时已惘然。与君初相识，犹如故人归。')
text=' '.join(str)
img=cv2.imread('Cloud.jpg')
cloud=wordcloud.WordCloud(mask=img,background_color="white",width=1000,height=1000,font_path="C:\\Windows\\Fonts\\STHEITI_1.TTF").generate(text)
cloud.to_file('chinese_cloud.jpg')


