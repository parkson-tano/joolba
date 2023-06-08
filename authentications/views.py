from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, MyTokenObtainPairSerializer, UserSerializer, ForgotPasswordSerializer, ResetPassWordSerializer
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework.generics import CreateAPIView, views
from rest_framework.response import Response
from .utils import send_verification_mail, send_password_reset_token, send_congratulations_mail
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


User = get_user_model()


class AccountVerification(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request, uuidb64, token, *args, **kwargs):

        # decode the user's id so we can retrieve the user
        uid = force_str(urlsafe_base64_decode(uuidb64))
        user = User.objects.get(pk=uid)
        current_site = request.get_host()

        send_congratulations_mail(user, current_site)
        return Response({'message': 'Account verified!'})


# create new user
class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # get the domain name of the site
        current_site = request.get_host()
            
        # send mail
        send_verification_mail(current_site, user)

        return Response({
            
            'user': UserSerializer(user, context={'request': request}).data,
            'message':'Sign up successful! A verification mail has been sent to your email address, please click on the mail'
            }, status=status.HTTP_201_CREATED)
    
    
    

# using jwt to handle token when user log in
class UserLogin(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]


# view that sends a token to email for password reset

class ForgotPassword(CreateAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            return Response({'error': 'No active account found with the given email address'}, status=status.HTTP_404_NOT_FOUND)

        # send a password reset link to user
        current_site = request.get_host()
        send_password_reset_token(current_site, user)

        return Response({
            'message':'A password reset link has been sent to your email address, please click on the link to reset your password',
            }, status=status.HTTP_201_CREATED)



class ResetPassword(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPassWordSerializer
    
    def post(self, request, uuidb64, url_token):
        token_generator = PasswordResetTokenGenerator()

        try:
            uid = force_str(urlsafe_base64_decode(uuidb64))
            user = User.objects.get(pk=uid)
        except(ValueError, TypeError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, url_token):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                password = serializer.validated_data['password']
                user.set_password(password)
                user.save()
                return Response({'success':'Password reset successful'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response({{"error": "Invalid or expired password reset link. Please request a new link."}}, status=status.HTTP_200_OK)
        