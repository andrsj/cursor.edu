import matplotlib.pyplot as plt



# print(plt.style.available)
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')


plt.rcParams.update({'figure.autolayout': True})
data = {
    'Barton LLC': 109438.50,
    'Frami, Hills and Schmidt': 103569.59,
    'Fritsch, Russel and Anderson': 112214.71,
    'Jerde-Hilpert': 112591.43,
    'Keeling LLC': 100934.30,
    'Koepp Ltd': 103660.54,
    'Kulas Inc': 137351.96,
    'Trantow-Barrows': 123381.38,
    'White-Trantow': 135841.99,
    'Will LLC': 104437.60
}
group_data = list(data.values())
group_names = list(data.keys())

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(group_names, group_data)
plt.xticks(group_names, rotation=45, horizontalalignment='right')
ax.set_yticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])

for group in [3, 5, 8]:
    ax.text(group, 130000, "New Company", fontsize=10, verticalalignment="center",horizontalalignment='center')

ax.set(ylim=[0, 140000], ylabel='Total Revenue', xlabel='Company', title='Company Revenue')
plt.show()