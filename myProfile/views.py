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

from .models import Project, AboutUpToInfo, AboutInfo, HomeInfo
from .forms import ContactForm



def about(request):
    page_info = AboutInfo.objects.first()
    up_to_info = AboutUpToInfo.objects.all()
    context = {
        'page_info': page_info,
        'up_to_info': up_to_info
    }
    return render(request, 'about.html', context)

def projects(request):
    projects_array = Project.objects.all()
    projects_array_json = serializers.serialize("json", Project.objects.all())
    context = {
        'projects_array': projects_array,
        'projects_array_json': projects_array_json
    }
    return render(request, 'projects.html', context)

def index(request):
    page_info = HomeInfo.objects.first()
    context={
        'page_info': page_info
    }
    return render(request, 'home.html', context)

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
            contact_subject = request.POST.get('subject', '')

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
                "ManuelBG: " + str(contact_subject),
                content,
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
