from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.urls import reverse
from joolbabackend.settings import EMAIL_HOST_USER
from rest_framework.authtoken.models import Token
from django.db import IntegrityError

from django.core.mail import EmailMessage
from django.template.loader import render_to_string



# this is file contains functions i might need 

# send verification mail

# def send_verification_mail(current_site, user):
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     verification_token = default_token_generator.make_token(user)
#     verification_link = reverse('account_verification', kwargs={'uuidb64':uid, 'token':verification_token})
#     verification_url = f'http://{current_site}{verification_link}'
#     subject = 'Confirm your email address for Joolba Account'
#     message = f'Dear {user.name}, \n\nThank you for creating an account with Joolba, your go-to source for the latest news and updates. To access our premium content and stay up to date on breaking news, please verify your email address by clicking on the link below: \n\n{verification_url}\n\nIf you did not create an account with Joolba, please ignore this email. Your account will not be actiavted until you verify your email address\n\nThank you for choosing Joolba as your trusted news source. We look forward to keeping you informed on the latest news and event\n\nBest regards,\n\nThe Joolba Team.'
#     from_email = EMAIL_HOST_USER
#     recipient_list = [user.email]
#     send_mail(subject, message, from_email, recipient_list)

def send_verification_mail(current_site, user):


    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_token = default_token_generator.make_token(user)
    verification_link = reverse('account_verification', kwargs={'uuidb64':uid, 'token':verification_token})
    verification_url = f'http://{current_site}{verification_link}'
    subject = 'Confirm your email address for Joolba Account'

    email_body = render_to_string('authentications/verify_account.html', {
        'username': user.name,
        'verification_url': verification_url,
    })

    from_email = EMAIL_HOST_USER
    recipient = user.email


    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email = EMAIL_HOST_USER,
        to = [recipient],
        reply_to=[from_email],
    )
    
    email.content_subtype = 'html'
    
    # Send the email
    email.send()

def send_congratulations_mail(user, site_domain):
    login_link = reverse('token_obtain_pair')
    login_url = f'http://{site_domain}{login_link}'
    email_body = render_to_string('authentications/congratulations.html', {
        'login_url':login_url
    })

    from_email = EMAIL_HOST_USER
    recipient = user.email
    email = EmailMessage(
        subject="Congratulations! Your Joolba account has been verified successfully",
        body=email_body,
        from_email = EMAIL_HOST_USER,
        to = [recipient],
        reply_to=[from_email],
    )
    
    email.content_subtype = 'html'
    
    email.send()


def send_password_reset_token(current_site, user):
    token_generator = PasswordResetTokenGenerator()
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    url_token = token_generator.make_token(user)

    # Remember to replace the current site with settings.FRONTEND_URL
    password_reset_url = reverse('password_reset', kwargs={'uuidb64':uid, 'url_token':url_token})
    password_reset_link = f'http://{current_site}{password_reset_url}'
    subject = 'Password reset for your joolba account'
    message = f'Dear {user.name}, \n\nYour request to change your password is being processed, Kindly click on this url, you will be redirected to a page where you can change your password: \n\n{password_reset_link}\n\nNote that this link expires and you will not be able to use it to change your password once it expires. If you did not request for a password reset, kindly ignore this mail.\n\nThank you for choosing Joolba as your trusted news source. We look forward to keeping you informed on the latest news and event\n\nBest regards,\n\nThe Joolba Team.'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)




# i didn't used it again, just kept it there for incasity
# def create_token_for_user(user):
#     try:
#         token = Token.objects.create(user=user)
#     except IntegrityError:
#         token = Token.objects.get(user=user)

#     return token