from matplotlib.pyplot import plot,text,show
from random import uniform as u
def etalons(t):return((sum([x for x,y in t[:int(len(t)/2)]])/(len(t)/2),sum([y for x,y in t[:int(len(t)/2)]])/(len(t)/2)),(sum([x for x,y in t[int(len(t)/2):]])/(len(t)/2),sum([y for x,y in t[int(len(t)/2):]])/(len(t)/2)))
def res(c,e):return[(i,((i[0]-c[0][0])**2+(i[1]-c[0][1])**2)**(1/2)>((i[0]-c[1][0])**2+(i[1]-c[1][1])**2)**(1/2)) for i in e]
def gen(z,e,c):return[(z[0]+u(-e,e),z[1]+u(-e,e)) for i in range(c)]
if __name__=='__main__':
    s,*c,e=100,(1,1),(3,3),1
    A,B=gen(c[0],e,s), gen(c[1],e,s)
    plot([x for x,y in A[:int(len(A)*0.8)]+B[:int(len(B)*0.8)]],[y for x,y in A[:int(len(A)*0.8)]+B[:int(len(B)*0.8)]],"ob",[x for x,y in A[int(len(A)*0.8):]+B[int(len(B)*0.8):]],[y for x,y in A[int(len(A)*0.8):]+B[int(len(B)*0.8):]],"or")
    t = etalons(A[:int(len(A)*0.8)]+B[:int(len(B)*0.8)])
    for i in t: plot(i[0],i[1],'gs')
    for i in res(t,A[int(len(A)*0.8):]+B[int(len(B)*0.8):]): text(i[0][0],i[0][1],str(i[1]))
    show()