from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256


# Create a new DSA key

sk = DSA.generate(2048)
pk = sk.publickey()

fp_sk = open("private.pem","w")
fp_pk = open("public.pem","w")

fp_sk.write(sk.export_key().decode())
fp_pk.write(pk.export_key().decode())

message = b"Hello"
hash_obj = SHA256.new(message)

signer = DSS.new(sk, 'fips-186-3')
signature = signer.sign(hash_obj)
validator = DSS.new(pk, 'fips-186-3')

message2 = b"Hellllo"
hash_obj2 = SHA256.new(message2)
# Verify the authenticity of the message

try:
    validator.verify(hash_obj, signature)
    print("Ervenyes alairas")
except ValueError:
    print("Ervenytelen alairas")

try:
    validator.verify(hash_obj2, signature)
    print("Ervenyes alairas")
except ValueError:
    print("Ervenytelen alairas")
