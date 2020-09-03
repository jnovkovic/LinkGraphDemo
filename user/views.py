from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Profile
from .serializer.validator.register_user_validator import \
    RegisterUserValidatorSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = RegisterUserValidatorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User(**serializer.validated_data)
            user.set_password(serializer.validated_data['password'])
            user.save()
            Profile.objects.create(owner=user)
            token = Token.objects.create(user=user)

            return Response(
                data={'token': token.key},
                status=status.HTTP_201_CREATED
            )
