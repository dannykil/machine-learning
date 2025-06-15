#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow


# In[3]:


tensorflow.__version__


# In[9]:


from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score, KFold
import numpy as np
import pandas as pd
np.random.seed(7)


import argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    '--input_data',
    type = str
)

parser.add_argument(
    '--mod_out',
    type = str
)

args = parser.parse_args()
arguments = args.__dict__

input_file = arguments['input_data']
mod_out = arguments['mod_out']

df = pd.read_csv(input_file)


# df = pd.read_csv("gs://training_prebuilt_container/IRIS.csv")
# df


# In[10]:


X = df.drop(["species"], axis=1)
Y = df['species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})


# In[15]:


# X
# Y


# In[23]:


encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# encoded_Y

dummy_y = np_utils.to_categorical(encoded_Y)
# dummy_y


# In[24]:


# model 생성
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[25]:


model.fit(X, dummy_y, epochs=150, batch_size=5)


# In[26]:


# model 정확도 평가
scores = model.evaluate(X, dummy_y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[27]:


predictions = model.predict(X)


# In[29]:


test = np.argmax(predictions, axis=1)
test


# In[30]:


# model save(하지만 사용안하므로 영상에서는 다시 삭제함)
# model.save("gs://training_prebuilt_container/model_output")


model.save(mod_out)

