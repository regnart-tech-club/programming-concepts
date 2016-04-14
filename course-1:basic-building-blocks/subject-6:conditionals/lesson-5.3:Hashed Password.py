#!/usr/bin/python

import hashlib

md5 = hashlib.md5()
md5.update('my password')
password_hash = md5.hexdigest()
print password_hash

password = raw_input('Password: ')
md5 = hashlib.md5()
md5.update(password)
if (md5.hexdigest() == password_hash):
  print 'You may enter'
else:
  print 'Begone!'
