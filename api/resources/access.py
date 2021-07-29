from services.cache_config import Cache

redis = Cache()
cache = redis.cache()

def set_cache_access_authorization(authorization):
    # cache authorization for one hour
    if authorization == True:
        authorization = 1
    else:
        authorization = 0

    cache.set("access_authorization", authorization, ex=60*60)

def get_access_authorization():
    authorization = cache.get("access_authorization")

    if authorization == None:
        authorization = False
    elif int(authorization) == 1:
        authorization = True
    elif int(authorization) == 0:
        authorization = False

    return authorization

def revoke_access_authorization():
    cache.delete("access_authorization")

def access_authorization_time_left():
    time_left = cache.ttl("access_authorization")

    return time_left