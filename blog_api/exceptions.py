from rest_framework.exceptions import APIException


class PostNotFoundError(APIException):
    status_code = 404
    default_detail = "The post was not found!"
