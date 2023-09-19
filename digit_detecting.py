from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

digits = load_digits()
# print(digits.data.size)
# print(dir(digits))
# print(digits.data[0])

# plt.gray()
# for item in range(0, 5):
#     plt.matshow(digits.images[item])
#     plt.show()

x = digits.data
y = digits.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# print(x_train.shape)
# print(x_test.shape)

model = LogisticRegression()
model.fit(x_train, y_train)

# print("target value of the test", digits.target[1700])
# result = model.predict([digits.data[1700]])
# print("rest result: ", result)

accuracy = model.score(x_test, y_test)
# print("model accuracy", accuracy)

y_predicted = model.predict(x_test)
confusion = confusion_matrix(y_test, y_predicted)

# print(confusion)

plot_confusion_matrix(model, x_test, y_test)
plt.show()
