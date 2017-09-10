def xor(x, y):
	if x == y:
		return False
	else:
		return True

print('True + True = ', xor(True, True))
print('True + False = ', xor(True, False))
print('False + True = ', xor(False, True))
print('False + False = ', xor(False, False))