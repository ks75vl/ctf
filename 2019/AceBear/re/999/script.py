from struct import pack, unpack


file = open('999', 'rb')

def read_int32(offset):
	global file
	
	file.seek(0xCB0A0 + offset * 4)
	data = file.read(4)
	return unpack('<I', data)[0]

#Check1
def rev_func_0x400D48(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		key[index + i] = (read_int32(offset + i + 5) / 0x1337) & 0xFF
		
	return key

#Check2		
def rev_func_0x400e2b(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):	
		key[index + i] = read_int32(offset + i + 5) ^ 0x04

	return key

#Check3
def rev_func_0x400f4e(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		for k in range(0, 256):
			v3 = k ^ 0xFFFFFFFF
			for j in range(7, -1, -1):
				if v3 & 1 == 0:
					v3 = v3 >> 1
				else:
					v3 = (v3 >> 1) ^ 0xEDB88320
			if (v3 ^ 0xFFFFFFFF) == read_int32(offset + i + 5):
				key[index + i] = k
				break
	return key

#Check4
def rev_func_0x400c0e(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		v3 = 0
		for j in range(0, 256):
			if j & 1:
				v3 += 1
			else:
				v3 += 3
				
			if read_int32(offset + i + 5) == v3:
				key[index + i] = j + 1
				break
	return key

#Check5
def rev_func_0x400eb5(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		for k in range(31, 127):
			v3 = 0
			for j in range(1, k + 1):
				if k % j == 0:
					v3 += j
			if v3 == read_int32(offset + i + 5):
				key[index + i] = k
				break
	return key

#Check6
def rev_func_0x400ca8(offset, key):

	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		v3 = 0xCAFEBABE
		for j in range(0, 256):
			if j & 1:
				v3 -= 0xAAAA
			else:
				v3 -= 0x1337
				
			if v3 == read_int32(offset + i + 5):
				key[index + i] = j + 1
				break
	return key

#Check7			
def rev_func_0x400dba(offset, key):
	
	index = read_int32(offset + 3)
	length = read_int32(offset + 4)
	
	for i in range(length):
		key[index + i] = read_int32(offset + i + 5) ^ 0x1337
		
	return key

def xor_array(a, b):
	return [x ^ y for x, y in zip(a, b)]
#


FLAG = [0x6D, 0x3C, 0x5A, 0x77, 0x2C, 0x3C, 0x50, 0x2E, 0x7C, 0x0C, 0x10, 0x40, 0x2F, 0x20, 0x47, 0x3B, 0x64, 0x50, 0x4B, 0x29, 0x36, 0x3B, 0x50, 0x2A, 0x2E, 0x36, 0x20, 0x6, 0x34, 0x49, 0x56, 0x17, 0x32, 0x2A, 0x42, 0x3E, 0x5F, 0x10, 0x4F, 0x3C, 0x57, 0x25, 0x2A, 0x4D, 0x20, 0x3E, 0x76, 0x40, 0x78, 0x33, 0x3F, 0x2E, 0x13, 0x30, 0x3C, 0x47, 0x55, 0x33, 0x2A, 0x43, 0x59, 0x7D, 0x7C, 0x36]

for index in range(999):
	call_stack = []
	offset = 0
	next = 0

	for i in range(64):
		offset = (index << 9) + next
		if read_int32(offset) >> 16 == 0x40:
			call_stack.append(offset)
		
		next += (read_int32(offset + 4) + 5)
		
	call_stack = call_stack[::-1]
	key = [0] * 64
	
	for s in call_stack:
		if read_int32(s) == 0x400D48:
			key = rev_func_0x400D48(s, key)
		elif read_int32(s) == 0x400e2b:
			key = rev_func_0x400e2b(s, key)
		elif read_int32(s) == 0x400f4e:
			key = rev_func_0x400f4e(s, key)
		elif read_int32(s) == 0x400c0e:
			key = rev_func_0x400c0e(s, key)
		elif read_int32(s) == 0x400eb5:
			key = rev_func_0x400eb5(s, key)
		elif read_int32(s) == 0x400ca8:
			key = rev_func_0x400ca8(s, key)
		elif read_int32(s) == 0x400dba:
			key = rev_func_0x400dba(s, key)
		else:
			print('Error')
	
	print('key[{}] = {}'.format(index, ''.join([chr(x) for x in key])))
	FLAG = xor_array(FLAG, key)


print(''.join([chr(x) for x in FLAG]))

file.close()






