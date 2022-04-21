from rest_framework.exceptions import APIException

class NotYourProfile(APIException):
    status_code = 403
    default_detail = "This is not your profile. You can't edit this."
    
class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You can't follow yourself."
    
