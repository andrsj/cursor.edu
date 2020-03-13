# Подключение библиотек
# from scipy.cluster.hierarchy import linkage, dendrogram
# from sklearn import datasets
# import matplotlib.pyplot as plt


# Создание полотна для рисования
# fig = plt.figure(figsize=(15, 30))
# fig.patch.set_facecolor('white')


# Загрузка набора данных "Ирисы Фишера"
# iris = datasets.load_iris()


# Реализация иерархической кластеризации при помощи функции linkage
# mergings = linkage(iris.data, method='complete')
# single
# average
# complete
# weighted
# centroid
# ward
# median


# Построение дендрограммы. Разными цветами выделены автоматически определенные кластеры
# R = dendrogram(mergings, labels=[iris.target_names[i] for i in iris.target], orientation = 'left', leaf_font_size = 10)


# Отображение дендрограммы
# plt.show()


from sklearn import datasets
iris = datasets.load_iris()
print(type(iris))
print(dir(iris))
# print("DESCR:\n",iris.DESCR)
print("data:\n",iris.data, '\t', len(iris.data))
print()
print()
print("feature names:\n",iris.feature_names,'\t',len(iris.feature_names))
# print("filename:\n",iris.filename)
print("target:\n", iris.target,'\t', len(iris.target))
print("target_names:\n",iris.target_names,'\t', len(iris.target_names))