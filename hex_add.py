def hex_add(s):
	i = int(s,16)
	i+=4
	return(hex(i))
i = input()
print(hex_add(i))