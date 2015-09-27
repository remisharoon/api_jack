from django.contrib.auth.models import User
from api_jack.models import UserInfo
from django.db import IntegrityError



try:
    user = User()
    info = UserInfo()    
    user.username = 'apiuser005'
    user.email = 'apiuser005@mail.com'
    user.password = 'pass123'
    user.save()
    
    info = UserInfo()
    info.user = user
    info.age = 31
    info.city = 'mumbai'
    info.job = 'developer'
    info.save()
except IntegrityError as e:
    print e

try:
    user = User()
    info = UserInfo()
    user.username = 'apiuser006'
    user.email = 'apiuser006@mail.com'
    user.password = 'pass123'
    user.save()
     
    info = UserInfo()
    info.user = user
    info.age = 32
    info.city = 'bangalore'
    info.job = 'tester'
    info.save()
except IntegrityError as e:
    print e
