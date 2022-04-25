"""Copied from https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
By author unlisted...
Modified for our use"""


import hashlib
import os

"""
salt = os.urandom(32) # Remember this
password = 'password123'
"""

#takes password returns hashednsalted password and salt
def hashnsalt(password):

    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac(
      'sha256', # The hash digest algorithm for HMAC
      password.encode('utf-8'), # Convert the password to bytes
      salt, # Provide the salt
     100000 # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return key,salt


def hashnsalt(password,salt):

    salt = salt

    key = hashlib.pbkdf2_hmac(
      'sha256', # The hash digest algorithm for HMAC
      password.encode('utf-8'), # Convert the password to bytes
      salt, # Provide the salt
     100000 # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return key




#print(hashnsalt(password,salt))
#salt = os.urandom(32)
#print(hashnsalt(password,salt))