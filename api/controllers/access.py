from flask_restful import Resource
from flask import request
from encryption.hash_pass import ShieldPassword
from api.resources import access

class AccessAuthorization(Resource):
    def get(self):
        authorization = access.get_access_authorization()

        return authorization
    
    def post(self):
        pswd = ShieldPassword()
        password = request.json['password']

        if pswd.password_hash == "":
            abort(404, error="Password hash not found", message="Create a password and retry")
        
        authorization_check = pswd.check_password(password)

        # cache authorization
        access.set_cache_access_authorization(authorization_check)

        return authorization_check

    def delete(self):
        # revoke authorization
        access.revoke_access_authorization()

        return True

class CreatePassword(Resource):
    # check if a password exists
    def get(self):
        pswd = ShieldPassword()
        exists = pswd.is_file

        return exists

    # create a new password
    def post(self):
        pswd = ShieldPassword()
        password = request.json['password']

        password_hash = pswd.write_new_password(password)
        pswd.save_password()

        return True