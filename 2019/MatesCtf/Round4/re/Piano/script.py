from hashlib import md5
from Crypto.Cipher import AES
import itertools
import base64
import gmpy2


space = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '#']

def rev_Verify_part1():
	n = 56284818775451078755885861126837882068425195371796962491046599655945450614341
	p = 204696599145043053272995403404251221471
	q = 274967043959382144647000841401293946971
	e = 65537
	cipher = 38954226075224880655326447817877801384556465215250032715236825825268127338226
	
	phi = (p - 1) * (q - 1)
	d = gmpy2.invert(e, phi)
	
	part1 = gmpy2.powmod(cipher, d, n)
	return hex(part1)[2:].zfill(32).decode('hex')
#

md5_part1 = rev_Verify_part1()
part1 = ''#'BEF#GABG'

print('Find part1...')
for i in itertools.product(space, repeat=8):
	if md5(''.join(i)).digest() == md5_part1:
		part1 = ''.join(i)
		print('   Found part1 ~> ' + part1)
		break
#

print('Find part2...')
flag_enc = base64.b64decode('5MZSqLE6UKfFW24TVluQPWvJKqpEGY0f40J5Nc3yCks=')
for i in itertools.product(space, repeat=9):
	key = md5(part1 + ''.join(i)).digest()
	aes_256_key = key[:-1] + key + '\x00'
	flag = AES.new(aes_256_key, AES.MODE_ECB).decrypt(flag_enc)
	if (flag.find('matesctf') != -1):
		print('   Found part2 ~> ' + ''.join(i))
		print('Flag ~> ' + flag)
		break













