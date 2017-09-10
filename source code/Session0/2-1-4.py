def calculator(i1, i2, i3, i4, i5):
	l = [i1, i2, i3, i4, i5]
	sum = 0
	idx = 0
	for i in l:
		if i != 0:
			sum += i
			idx += 1
		else:
			break
	return (sum, int(sum/idx))

print(calculator(1,2,3,4,5))
print(calculator(1,2,0,4,5))