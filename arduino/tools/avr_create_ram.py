import sys

argc = len(sys.argv)

if argc == 6:
	filename, output, offset, start, end = sys.argv[1:]
else:
	print('Usage: avr_create_ram.py input output address start end')
	print('Example: avr_create_ram.py ./rom ./ram 0x32da 0x100 0x2fa\n')
	sys.exit()
#

offset = int(offset, 16)
start = int(start, 16)
end = int(end, 16)

file = open(filename, 'rb')
file.seek(offset)
data = file.read(end - start)
file.close()

ram = '\x00' * 0x100 + data
ram += ('\x00' * (0x800 - len(ram)))

out = open(output, 'wb')
out.write(ram)
out.close()