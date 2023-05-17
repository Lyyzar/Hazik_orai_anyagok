from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256


secretkey = DSA.generate(2048)
publickey = secretkey.publickey()

fp_secretkey = open("private.pem","w")
fp_publickey = open("public.pem","w")

fp_secretkey.write(secretkey.export_key().decode())
fp_publickey.write(publickey.export_key().decode())

uzenet = b"This is the message!"
hash_obj = SHA256.new(uzenet)

alairo = DSS.new(secretkey, 'fips-186-3')
alairas = alairo.sign(hash_obj)
validator = DSS.new(publickey, 'fips-186-3')

uzenet2 = b"This is another message!"
hash_obj2 = SHA256.new(uzenet2)


try:
    validator.verify(hash_obj, alairas)
    print("Ervenyes alairas")
except ValueError:
    print("Ervenytelen alairas")

try:
    validator.verify(hash_obj2, alairas)
    print("Ervenyes alairas")
except ValueError:
    print("Ervenytelen alairas")
