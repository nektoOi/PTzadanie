def my_code(dicts):
	i = 0
	trasform(dicts,i)

def trasform(dicts,i):
	
	for k, val in dicts.items():
		print(' '*i +k +':')

		if isinstance(val, dict):
			trasform(val,i+3)

		else:
			print(' '*(i+3) +val)



my_code({
'1': {
'child': '1/child/value'
},
'2': '2/value'
})