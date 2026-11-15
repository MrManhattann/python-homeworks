from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Contact
from .forms import ContactForm


def contact_list(request):
    query = request.GET.get('q', '').strip()

    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        'contacts': contacts,
        'query': query,
    }

    return render(request, 'contacts/contact_list.html', context)


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(
        request,
        'contacts/contact_form.html',
        {
            'form': form,
            'title': 'Додати контакт',
        }
    )


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        'contacts/contact_form.html',
        {
            'form': form,
            'title': 'Редагувати контакт',
        }
    )


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(
        request,
        'contacts/contact_confirm_delete.html',
        {'contact': contact}
    )