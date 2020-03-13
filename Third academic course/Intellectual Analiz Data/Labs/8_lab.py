import matplotlib.pyplot as plt
import xlrd
import xlwt


files = xlrd.open_workbook(filename = "00_0204.xls") # зчитання файлу
sheet = files.sheet_by_index(0) # номер листка

years = [i for i in range(1989,2020)]
year = str(sheet.row(4)[4]).split(":")[1].split(".")[0]

counts = []
for row in range(5,31):
    counts.append(str(sheet.row(row)[5]))
for count in counts:
    counts[counts.index(count)] = int(float(count.split(":")[1]))



L = [counts[0],]
T = [0,]
Y_ = []
alpha = 0.5
beta = 0.5
p = 1

# Ln = a * y + (1-a)(Ln-1 - Tn-1)
# L1 = y1

# Tn = b * (Ln - Ln-1) + (1 - b) * Tn-1
# T1 = 0

# Y_ n+p = Ln + p * Tn

for i in counts[1:]:
    L.append(alpha * i + (1 - alpha) * (L[-1] - T[-1]))
    T.append(beta * (L[-1] - L[-2]) + (1 - beta) * T[-1])
    Y_.append(L[-2] + p * T[-2])
Y_.append(L[-1] + p * T[-1])
c = 0
for i,j,k in zip(L,T,Y_):
    c += 1
    print("L = {} \t T = {} \t Y_ = {} \t {}".format(i,j,k,c))

c = 0
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Test")
for i,j,k in zip(years[1:-1],counts[1:],Y_[:-1]):
    worksheet.write(c, 0, i)
    worksheet.write(c, 1, j)
    worksheet.write(c, 2, k)
    c += 1

workbook.save("8_.xls")

plt.title('Вікова група - {}'.format(year))
plt.plot(years[:len(counts)],counts)
plt.plot(years[p : len(Y_) + p],Y_)
print(p,len(Y_) + p + 1)
plt.grid()
plt.show()
