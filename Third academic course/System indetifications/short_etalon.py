from matplotlib.pyplot import plot,text,show
from random import uniform as uni
def dist(a,b): return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)
def etalons(t): return ((sum([x for x,y in t[:int(len(t) / 2)]]) / (len(t)/2), sum([y for x,y in t[:int(len(t) / 2)]]) / (len(t)/2)), (sum([x for x,y in t[int(len(t) / 2):]]) / (len(t)/2), sum([y for x,y in t[int(len(t) / 2):]]) / (len(t)/2)))
def res(c,ex): return [(i, dist(i,c[0]) > dist(i,c[1])) for i in ex]
def gen(xy,e,c): return [(xy[0] + uni(-e, e), xy[1] + uni(-e, e)) for i in range(c)]
if __name__ == '__main__':
    cs,*c,e = 100,(1,1),(3,3),1
    A,B = gen(c[0],e,cs), gen(c[1],e,cs)
    plot([x for x,y in A[:int(len(A)*0.8)]+B[:int(len(B)*0.8)]],[y for x,y in A[:int(len(A)*0.8)]+B[:int(len(B)*0.8)]],"ob")
    plot([x for x,y in A[int(len(A)*0.8):]+B[int(len(B)*0.8):]],[y for x,y in A[int(len(A)*0.8):]+B[int(len(B)*0.8):]],"or")
    et = etalons(A[:int(len(A)*0.8)] + B[:int(len(B)*0.8)])
    for i in et: plot(i[0],i[1], 'gs')
    for i in res(et,A[int(len(A)*0.8):] + B[int(len(B)*0.8):]): text(i[0][0],i[0][1],str(i[1]))
    show()