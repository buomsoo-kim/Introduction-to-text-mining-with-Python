def search_element(l, e):
	if e in l:
		return l.index(e)
	else:
		return False

l = [1,2,3]
e1 = 2
e2 = 10

print(search_element(l, e1))
print(search_element(l, e2))