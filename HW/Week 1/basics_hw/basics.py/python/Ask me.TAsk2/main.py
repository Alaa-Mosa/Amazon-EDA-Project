from models.regression import LinearRegModel
from models.classification import KNNModel
from utils.metrics import accuracy_score

reg = LinearRegModel()
reg.fit([1, 2, 3], [10, 20, 30])
print(reg.predict([5, 6]))
knn = KNNModel()
knn.train([1, 2, 3], ["A", "A", "B"])
pred = knn.predict([10, 11])
print(pred)
score = accuracy_score(["A", "A"], pred)
print("Accuracy:", score)