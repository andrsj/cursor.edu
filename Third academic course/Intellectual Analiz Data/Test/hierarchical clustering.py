# Подключение библиотек
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn import datasets
import matplotlib.pyplot as plt


# Создание полотна для рисования
fig = plt.figure(figsize=(15, 30))
fig.patch.set_facecolor('white')


# Загрузка набора данных "Ирисы Фишера"
iris = datasets.load_iris()


# Реализация иерархической кластеризации при помощи функции linkage
mergings = linkage(iris.data, method='complete')
# single
# average
# complete
# weighted
# centroid
# ward
# median


# Построение дендрограммы. Разными цветами выделены автоматически определенные кластеры
R = dendrogram(mergings, labels=[iris.target_names[i] for i in iris.target], orientation = 'left', leaf_font_size = 10)


# Отображение дендрограммы
plt.show()