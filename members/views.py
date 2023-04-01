from django.shortcuts import render, redirect
from members.models import Member
from members.forms import MemberForm, LoginForm
from django.contrib import messages
from members.authenticate import authenticate

def homePage(request):
  return render(request, 'common/index.html')

def members(request):
  members = Member.objects.all().values()
  context = {
    'members': members,
  }
  return render(request, 'common/all_members.html', context)

def details(request, username):
  member=Member.objects.get(username=username)
  context = {
    "member": member
  }
  return render(request, 'common/member_details.html', context)

def delete_session(request):
  try:
    del request.session['user']
  except:
    print('No session is set')

def register(request):
  if request.method == "POST":
    delete_session(request)
    form = MemberForm(request.POST)
    username = request.POST.get('username')
    try:
      if form.is_valid(): # Check if form values are valid
        messages.success(request, "Registration successful." )
        form.save()
        request.session['user'] = username # Set session for this user
        return redirect(f"/home/{username}") # If successful, save data to DB and redirect to home page.
      else:
        print(form.errors)

    except Exception as e:
      messages.error(request, "Unsuccessful registration. Invalid information.")

  form = MemberForm()
  return render(request, 'registration/register.html', context={"form": form})


def login(request):
  if request.method == "POST":
    delete_session(request)
    form = LoginForm(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    if authenticate(username=username, password=password):
      request.session['user'] = username
      return redirect(f"/home/{username}")

  form = LoginForm()
  return render(request, 'registration/login.html', context={'form': form})


def logout(request):
  delete_session(request)
  return redirect("/")


def memberHome(request, username):
  try:
    if request.session['user'] == username:
      member=Member.objects.get(username=username)
      context = {
        "member": member
      }
      return render(request, 'member/member_home.html', context)
    else: 
      return redirect("/login/")
  except:
    return redirect("/login/")