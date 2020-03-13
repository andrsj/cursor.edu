import time

start_cpu = time.clock()
start_real= time.time()

end_cpu = time.clock()
end_real = time.time()
print("Дійсний час в сек. : %f" % (end_real – start_real))
print("Процесорний час в сек. : %f" % (end_cpu - start_cpu))