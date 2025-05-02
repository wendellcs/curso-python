import re 

def is_password_valid(password):
    if re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password):
        return True 
    else:
        return False
    
is_password_valid('Password567') # True
is_password_valid('ExemploSenha1') # True
is_password_valid('senha123') # False
is_password_valid('12345678aA') # True