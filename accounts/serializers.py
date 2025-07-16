from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username",]

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password",]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data['password'],
        )

        return user
