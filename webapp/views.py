from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from webapp.models.baseModel import *
from .forms import ClientForm
# Create your views here.


def index(request, pagename=None):
    context = {}

    if (pagename) and (pagename != 'index') and not (str(pagename)).__contains__('.html'):
        return render(request, f'{pagename}.html', context=context)
    return render(request, 'index.html', context=context)


def clientSubmitForm(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Send email
            subject = f'New Form Submission from {firstName} {lastName}'
            message = f'You have a new form submission from:\n\nName: {firstName} {lastName}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            from_email = f'{email}'
            recipient_list = ['okechuquofficial@gmail.com']

            send_mail(subject, message, from_email, recipient_list)

            messages.success(
                request, 'Message Recieved, we will contact you in the next few Hours!')
            return redirect('index')
        messages.error(request, 'Not sent please retry!')
    else:
        form = ClientForm()
    return render(request, 'index.html', {'form': form, 'messages': messages.get_messages(request)})
