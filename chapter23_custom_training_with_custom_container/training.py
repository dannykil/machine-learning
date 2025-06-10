#!/usr/bin/env python
# coding: utf-8

# # This is Custom Training

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[4]:


data = pd.read_csv("gs://training_custom_container/IRIS.csv")
# data = pd.read_csv("/Users/danniel.kil/Documents/workspace/machine-learning/chapter23_custom_training_with_custom_container/IRIS.csv")


# In[5]:


type(data)


# In[6]:


data


# In[7]:


from sklearn.model_selection import train_test_split
array = data.values
X = array[:, 0:4]
y = array[:, 4]

# Split the data to train and test dataset.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
# X
# y


# In[8]:


# X_train
X_train.shape # 120개의 훈련 데이터셋 생성(test_size=0.20)


# In[19]:


X_test.shape


# In[20]:


y_train.shape


# In[21]:


y_test.shape


# In[9]:


from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, y_train)


# In[10]:


predictions = svn.predict(X_test)

# Calculate the accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)


# # model is ready

# In[13]:


# model 직렬화(?)
import pickle
import logging

with open('model.pkl', 'wb') as model_file:
    pickle.dump(svn, model_file)


# In[14]:


# 모델 생성해서 GCS 업로드 : 이 방법은 사용하지 않을 예정으로 스토리지에서 삭제
# 도커 컨테이너 사용 예정
from google.cloud import storage
storage_path = "gs://training_custom_container/model.pkl"
blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
blob.upload_from_filename('model.pkl')
logging.info("model expected to : {}".format(storage_path))

