from django.shortcuts import render, redirect
from . forms import ContactForm
from . import models
from django.contrib import messages
from  .models import Contact
from django.shortcuts import get_object_or_404  



def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato salvo com sucesso.')
            return redirect('contacts:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso.')
            return redirect('contacts:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        messages.success(request, 'Contato deletado com sucesso.')
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})