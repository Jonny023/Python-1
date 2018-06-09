# coding=gbk  
import urllib.request
import re

url = "https://xiaoshuo.sogou.com/list/6632040968"
urlpre="https://xiaoshuo.sogou.com"
# decode ����  encode����
data = urllib.request.urlopen(url).read().decode('UTF-8', 'ignore')
data.encode('UTF-8')
#��ȡС˵������
title=re.findall(r'<title>.*?_(.*?)-.*?</title>', data,re.S)[0]
print(title)
#�½�һ���ļ��������
fb=open('%s.txt' % title,'w',encoding='utf-8')
# �õ����е��½�
resulttext = re.findall(r'<ul class="chapter clear" pbflag="�½��б�">(.*?)</ul>', data, re.S)[0]
# �õ�ÿ���½ڵ�url��title
chapter_info_list = re.findall(r'href=\"(.*?)\" target=\"_blank\"><span>(.*?)<', resulttext, re.S)
for chapter_info in chapter_info_list:
 chapter_uri,chapter_title=chapter_info
 chapter_url=urlpre+chapter_uri
 
 #�����½�����
 chapter_html=urllib.request.urlopen(chapter_url).read().decode('UTF-8', 'ignore')
 
 chapter_text=re.findall(r'<div id="contentWp" style="display:none">(.*?)</div>', chapter_html, re.S)[0]
 
 chapter_text=chapter_text.replace(' ','')
 chapter_text=chapter_text.replace('\r\n','')
 chapter_text=chapter_text.replace('&rdquo;','')
 chapter_text=chapter_text.replace('</p>','')
 chapter_text=chapter_text.replace('<p>','')
 chapter_text=chapter_text.replace('&hellip;','')
 chapter_text=chapter_text.replace('&ldquo;','')
 
 
 #д������
 fb.write(chapter_title)
 fb.write(chapter_text)
 fb.write('\n')
 fb.write('\r\n')
 print(chapter_title,chapter_text)


