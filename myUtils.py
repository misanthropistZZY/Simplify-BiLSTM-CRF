
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


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


# In[5]:


import json


# In[2]:


def json_to_obj(d):
    return SerialSentce(d['text'], d['entity_list'])


# In[3]:


def get_sent_list(trans_f):
    sent_list = []
    line = trans_f.readline()
    while line:
        serial = json.loads(line, object_hook=json_to_obj)
        sent_list.append(serial)
        line = trans_f.readline()
    trans_f.close()
    return sent_list


# In[4]:


def loadData(path):
    trans_f = open(path)
    sent_list = get_sent_list(trans_f)
    company_dic = {}
    project_dic = {}
    contract_dic = {}
    for s in sent_list:
        for e in s.entity_list:
            if 'B-jiafang' in e:
                company_dic[e] = e
            if 'B-yifang' in e:
                company_dic[e] = e
            if 'xiangmu' in e:
                project_dic[e] = e
            if 'hetong' in e:
                contract_dic[e] = e
    return sent_list, company_dic, project_dic, contract_dic

