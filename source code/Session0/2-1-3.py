def area_expand(w, l):
	area_original = w * l
	w = w + 5
	l = l * 2
	area_expanded = w * l
	print('Width = ', w)
	print('Length = ', l)
	print('Area Ratio = ', area_original/area_expanded)

area_expand(5, 10)