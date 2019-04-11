from struct import unpack


origin = open('999', 'rb')
patch = open('999-patched', 'wb')

#Copy
data = origin.read()
patch.write(data)

def read_int32(file, address):
	file.seek(address)
	data = file.read(4)
	return unpack('<I', data)[0]

def write_bytes(file, address, bytes):
	file.seek(address)
	file.write(bytes)
	
def read_bytes(file, address, size):
	file.seek(address)
	return file.read(size)

def xor_bytes(a, b):
	return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, b)])
#

unk_6CB0A0 = 0x6CB0A0 - 0x600000
patched = []

for i in range(999):
	base_addr = unk_6CB0A0 + (i << 9) * 4
	offset = 0
	
	for j in range(64):
		
		address = read_int32(origin, base_addr + offset + 4 * 0)
		size = read_int32(origin, base_addr + offset + 4 * 1)
		key = read_int32(origin, base_addr + offset + 4 * 2)
		n = read_int32(origin, base_addr + offset + 4 * 4)
		
		offset = offset + (n + 5) * 4
		
		if (address >> 16) >= 0x40:	#check if address in text segment
			if address not in patched:	#Check for patched address
				patched.append(address)
				print('Patching {}'.format(hex(address)))
				
				old_bytes = read_bytes(origin, address - 0x400000, size)
				new_bytes = xor_bytes(old_bytes, chr(key) * size)
				write_bytes(patch, address - 0x400000, new_bytes)
	
origin.close()
patch.close()
