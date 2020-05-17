from flask_bcrypt import generate_password_hash, check_password_hash

def set_password(user, pwstr):
    hashed_pw = generate_password_hash('secret')
    user.password = hashed_pw
    return User

def validate_password(user, password):
    return check_password_hash(user.password, password)