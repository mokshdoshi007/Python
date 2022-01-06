from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib
import random
import string
from myapp.models import TempUsers, Users
from random import randint

def sendmail(subject,template,to,context):
    subject='Django'
    template_str=template+'.html'
    html_message=render_to_string(template_str,{'data':context})
    plain_message=strip_tags(html_message)
    from_email='emailid'
    send_mail(subject,plain_message,from_email,[to],html_message=html_message)

def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_pw_hash(password,hash):
    if make_pw_hash(password)==hash:
        return True
    return False
    
def token_request():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(40)))
    return result_str

def clearall():
    TempUsers.objects.all().delete()

def swaptoken(authToken,at):
    authToken.remove(at)
    authToken.append(at)
    return authToken

def addtoken(authToken,at):
    if len(authToken)==3:
        authToken.pop(0)
    authToken.append(at)
    return authToken