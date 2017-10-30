from django.core import serializers
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

from .forms import ContactForm
import logging

from .models import Project
from .forms import ContactForm



def about(request):
    return render(request, 'about.html')

def projects(request):
    projects_array = Project.objects.all()
    projects_array_json = serializers.serialize("json", Project.objects.all())
    context = {
        'projects_array': projects_array,
        'projects_array_json': projects_array_json
    }
    return render(request, 'projects.html', context)

def index(request):
    return render(request, 'home.html')

def contact(request):
    logger = logging.getLogger(__name__)
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'name'
            , '')
            contact_email = request.POST.get(
                'email'
            , '')
            contact_message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                contact_message,
                "ManuelBG" +'',
                ['manuelabaezg@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
        else:
            logger.error('Derp')

    return render(request, 'contact.html', {
        'form': form_class,
    })
def success(request):
    return HttpResponse('Success! Thank you for your message.')
