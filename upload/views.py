from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Document
from .forms import DocumentAddForm
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', {'documents': documents})


def add_document(request):
    if request.method == 'POST':
        form = DocumentAddForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = DocumentAddForm()
    return render(request, 'add_document.html', {'form': form})

def send_mail(request, pk):

    if request.method == 'POST':

        #name = request.POST.get('author')
        #email = request.POST.get('email1')
        #subject = request.POST.get('author')
        #message = request.POST.get('pdf')

        document = get_object_or_404(Document, pk=pk)
        name = Document.author
        email = Document.email1
        subject = Document.title
        message = Document.pdf.url

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
            New Message: {}

            From: {}

        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['to@gmail.com'])

        return HttpResponse('Your mail is sent successfully')
    return redirect('home')

def delete_document(request, pk):
    if request.method == 'POST':
        document = get_object_or_404(Document, pk=pk)
        document.delete()
        messages.success(request, "Document deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
