


def my_code(data, start_versh):
	if not start_versh in vershini: # Добавляем в список вершину с которой начинаем. 
		vershini.append(start_versh) # Без этого условия получим чистый список достижимых вершин из точки вхождения.
	try:
		for val in data[start_versh]: 
			if not val  in vershini:
				vershini.append(val)
				my_code(data, val)
			else:
				return
	except:
		pass

vershini = []

data = {
	
	1:[2, 3],
	2:[4],
	4:[2]	
	}	

my_code(data, 2)

for ver in vershini:
	print(ver)

