from sklearn import datasets
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle
import numpy as np

iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.target.shape)


# print(iris.data)
# print(iris.target_names)
#
# print(digits.data.shape)
# print(digits.target)

n_test = 100
train_x = digits.data[:-n_test, :]
train_y = digits.target[:-n_test]
# print(train_x.data.shape)
# print(train_y)

test_x = digits.data[-n_test:, :]
y_true = digits.target[-n_test:]

svm_model = svm.SVC(gamma=0.001, C=100.)
svm_model.fit(train_x, train_y)
print(svm_model)

lr_model = LogisticRegression()
lr_model.fit(train_x, train_y)
print(lr_model)

y_pred_svm = svm_model.predict(test_x)
y_pred_lr = lr_model.predict(test_x)

print('SVM:', accuracy_score(y_true, y_pred_svm))
print('LR:', accuracy_score(y_true, y_pred_lr))

with open('svm_model.pkl', 'wb') as f:
    pickle.dump(svm_model, f)

with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)




