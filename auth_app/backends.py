from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()
class CustomAuthBackend(ModelBackend):
  def authenticate(self, request, username = None, password = None, **kwargs):
    # authentication logic goes here    
    try:
       # Look for a user where the username OR email matches the input
      user = UserModel.objects.get(Q(username__iexact = username) | Q(email__iexact = username))
    except UserModel.DoesNotExist:
      return None
    
    # Check if the password is correct for the found user
    if user.check_password(password):
      return user
    return None  

  def get_user(self, user_id):
    try:
       return UserModel.objects.get(pk = user_id)
    except UserModel.DoesNotExist:
      return None