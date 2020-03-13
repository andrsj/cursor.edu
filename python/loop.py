

# LOOPS

	i = 1
	while i<=5:
	    print(i)
	    i += 1
	else:
		print("Done")

	for i in "Python":		#|P,y,t,h,o,n
	for i in [1,3,5]:		#| 1,3,5
	for i in range(10): 	#| 0 - 9
	range (5,10):			#| 5 - 9
	range (5,10,2):			#| 5,7,9
	    print(i)
	else:
		print("End")



	for x,y,z in zip(OX,OY,OZ):
		print(f'Coord of point: {x} {y} {z}')

	for i in zip(OX,OY,OZ):
		print(i)

	# OUT: (x,y,z)
	# 	 (x,y,z)
	# 	 (x,y,z)