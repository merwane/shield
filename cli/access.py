from cli.api import ShieldApi
from PyInquirer import prompt

api = ShieldApi()

def is_unlocked():
    unlocked = api.get("access")

    return unlocked

def password_exists():
    exists = api.get("password")

    return exists

def access_cli(password):
    authorization = api.post("access", data={'password': password})
    if authorization == True:
        pass
    else:
        print('Invalid password. Please retry...')
        print("\n")
        exit()
    
    return authorization

def create_new_password():
    shield_password = [{
        'type': 'password',
        'name': 'shield_password',
        'message': 'Enter your new password'
    }]

    shield_password_confirm = [{
        'type': 'password',
        'name': 'shield_password_confirm',
        'message': 'Confirm your password'
    }]

    password = prompt(shield_password)
    password_confirm = prompt(shield_password_confirm)

    if password['shield_password'] != password_confirm['shield_password_confirm']:
        print('Passwords do not match. Please retry...')
        print("\n")
        exit()

    api.post("password", data={"password": password['shield_password']})

    print('Password saved. Please log in.')
    print("\n")
    exit()
    

def password_check():
    # check if Shield is unlocked
    unlocked = is_unlocked()
    if unlocked == True:
        return True

    # check if password doesn't exist
    # create one if not
    exists = password_exists()
    if exists == False:
        create_new_password()
    
    shield_password = [{
        'type': 'password',
        'name': 'shield_password',
        'message': 'Enter your password'
    }]

    password = prompt(shield_password)
    authorization = access_cli(password['shield_password'])

    return authorization

# revokes Shield access by uncaching the password
def revoke_access():
    api.revoke_access()
    print('Shield access revoked.')
    print("\n")
    exit()