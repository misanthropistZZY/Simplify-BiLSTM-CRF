
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#金融序列化数据读取" data-toc-modified-id="金融序列化数据读取-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>金融序列化数据读取</a></span></li><li><span><a href="#句法依存分析" data-toc-modified-id="句法依存分析-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>句法依存分析</a></span></li></ul></div>

# ## 金融序列化数据读取
# ---
# >句子形式

# In[1]:


trans_f = open(r'./data/transf.txt', 'r', encoding='utf-8')


# In[2]:


import json


# In[3]:


class SerialSentce:
    def __init__(self, text, entity_list):
        self.text = text
        self.length = len(text)
        if len(entity_list) < 1:
            self.entity_list = []
        else:
            self.entity_list = entity_list

    def display(self):
        print('text--->', self.text)
        print('length--->', self.length)
        print('entitys--->', self.entity_list)


# In[4]:


def json_to_obj(d):
    return SerialSentce(d['text'], d['entity_list'])


# In[5]:


def get_sent_list(trans_f):
    sent_list=[]
    line=trans_f.readline()
    while line:
        serial=json.loads(line,object_hook=json_to_obj)
        sent_list.append(serial)
        line=trans_f.readline()
    trans_f.close()
    return sent_list


# In[6]:


sent_list=get_sent_list(trans_f)


# In[7]:


len(sent_list)


# In[8]:


s=sent_list[10]
s.display()


# In[9]:


company_dic={}
project_dic={}
contract_dic={}
for s in sent_list:
    for e in s.entity_list:
        if 'B-jiafang' in e:
            company_dic[e]=e
        if 'B-yifang' in e:
            company_dic[e]=e
        if 'xiangmu' in e:
            project_dic[e]=e
        if 'hetong' in e:
            contract_dic[e]=e


# In[10]:


print('公司--->', len(company_dic))
print('项目--->', len(project_dic))
print('合同--->', len(contract_dic))


# In[52]:


for key in project_dic:
    print(key)


# In[11]:


for key in contract_dic:
    print(key)


# ## 句法依存分析
# ---
# >采用jieba分词

# In[43]:


import jieba
import jieba.posseg as pseg


# In[45]:


words=pseg.cut(s.text,HMM=True)
for word,flag in words:
    print(word,'--->',flag)

