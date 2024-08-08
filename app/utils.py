import bcrypt  

def hash_password(plain_text_password):
    bytes = plain_text_password.encode('utf-8') 
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)

def verify_password(plain_text_password, hashed_password):
    plain_text_pass_bytes = plain_text_password.encode('utf-8') 
    return bcrypt.checkpw(plain_text_pass_bytes, hashed_password) 

