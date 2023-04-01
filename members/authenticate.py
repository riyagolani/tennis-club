from members.models import Member
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect

def authenticate(username, password):
    if Member.objects.count() > 0:
        try:
            user = Member.objects.get(username=username)
        except:
            print("User does not exist. Please register")
            return redirect("/")
        if check_password(password, user.password):
            print("Login Successful")
            return True
        else:
            print("Incorrect Username or Password")
            return False
    else:
        print("No Members registered")
        return False


