from werkzeug.security import generate_password_hash

s = "Python Bootcamp"
s_hsh=generate_password_hash(s)
print('hashed string: ',s_hsh)
