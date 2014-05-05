from django.shortcuts import redirect, render_to_response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from hackaglobal.models import Event, Attendee, HackaCity
from django.core.mail import send_mail

from hackaglobal.tools.forms import HGUserEditForm, EFPasswordChangeForm, HGUserCreationForm, HGProfileEditForm


def signup(request):

    form = request.POST.get("form", "")

    if request.method =='POST':
        form = HGUserCreationForm(request.POST)

    if form:
        if form.is_valid():
            user = form.save()

            # We use this to set the user as authenticated, as we have just created the user
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)
            return redirect('home') # Redirect after POST
    else:
        form = HGUserCreationForm() # An unbound form

    return render_to_response('accounts/signup.html', { 'form': form, }, context_instance=RequestContext(request))

def apply(request):
    if request.method =='POST':
        post = request.POST
        name = post.get('name','')
        email = post.get('email','')
        hackacity = post.get('hackacity','')
        content = post.get('content', '')

        send_mail('New HackaCity Application!!', "Email: " + email + " from: " + name + ". Application for ["+ hackacity +"] Content: " + content, 'hackaglobal@gmail.com',
            ['hackaglobal@gmail.com'], fail_silently=False)

        try:
            print email
            send_mail('Thanks for your application', "Thank you for your application to kick start "+ hackacity +"! We'll get back to you as fast as we can! We're looking forward to have you in this awesome community!", 'hackaglobal@gmail.com',
                [email], fail_silently=False)
        except:
            print "email error"



    return render_to_response('accounts/apply.html', {}, context_instance=RequestContext(request))

def view_account(request, username):

    user = User.objects.get(username=username)

    hackacities = HackaCity.objects.filter(team=request.user)
    attendee_all = Attendee.objects.filter(attendee=user)
    attending = []
    for a in attendee_all:
        attending.append(a.event)

    return render_to_response('accounts/account_view.html', { 'hackacities': hackacities, 'attending': attending, 'otheruser' : user }, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_account(request):

    if request.method == "POST":
        userform = HGUserEditForm(request.POST, instance=request.user)
        profileform = HGProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save()
    else:
        userform = HGUserEditForm()
        profileform = HGUserEditForm()

    return render_to_response('accounts/account_edit.html', { 'userform': userform, 'profileform': profileform }, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_password(request):

    if request.method == "POST":
        form = EFPasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()

            # We use this to set the user as authenticated, as we have just created the user
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)
    else:
        form = EFPasswordChangeForm(user=request.user)

    return render_to_response('accounts/account_edit_password.html', { 'form': form, }, context_instance=RequestContext(request))