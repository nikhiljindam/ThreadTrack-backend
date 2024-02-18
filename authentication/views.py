from rest_framework.decorators import permission_classes
from django.contrib.auth import logout, authenticate, login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from vendors.db_oprations import fetch_vendor_details_by_user
from vendors.serializer import ReadUserVendor


class Login(TokenObtainPairView):
    """
    Login view

    """
    def post(self, request, *args, **kwargs):
        password = request.data.get("password")
        username = request.data.get("username")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = super().post(request, *args, **kwargs)
            if refresh.status_code == status.HTTP_200_OK:
                token = refresh.data.get("access")
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            vendor_details = fetch_vendor_details_by_user(user)
            serializer = ReadUserVendor(data=vendor_details)
            serializer.is_valid(raise_exception=True)

            data = {
                "token": token,
                "user_id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "vendor": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
def Logout(request):
    logout(request)
