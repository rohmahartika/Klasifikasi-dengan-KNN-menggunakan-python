import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics

from google.colab import drive
drive.mount('/content/drive')

# Read dataset to pandas dataframe
df = pd.read_csv('/content/drive/MyDrive/heart.csv')
df.head(3)

df.target.value_counts()

sns.countplot(x="target", data=df, palette="bwr")
plt.show()

fig_dims = (20, 4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='age', hue='target', data = df, palette="bwr", ax = ax,  edgecolor=sns.color_palette("dark", n_colors = 1));

plt.scatter(x=df.age[df.target==1], y=df.thalach[(df.target==1)], c="b")
plt.scatter(x=df.age[df.target==0], y=df.thalach[(df.target==0)], c = 'c')
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.show()

X = df.iloc[:,:-1].values
y = df.iloc[:,13].values
X_train, X_test, y_train, y_test =  train_test_split(X,y,test_size = 0.25, random_state= 0)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

error = []

# Calculating error for K values between 1 and 40
for i in range(1, 30):  
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))  
plt.plot(range(1, 30), error, color='c', linestyle='dashed', marker='o',  
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate Nilai K')  
plt.xlabel('Nilai K')  
plt.ylabel('Error rata-rata')

#k=7
classifier = KNeighborsClassifier(n_neighbors = 7, metric = 'minkowski', p = 2)
classifier = classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
#check accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))

#confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

import seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(8,5))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt=".0f",
ax=ax)
plt.xlabel("y_head")
plt.ylabel("y_true")
plt.show()

from sklearn.metrics import classification_report
print (classification_report(y_test, y_pred))
