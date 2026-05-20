from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .forms import LinkForm
from .models import LinkModel


@login_required
def home(request):

    links = LinkModel.objects.all()

    return render(
        request,
        'index.html',
        {
            'links':links
        }
    )


@login_required
def create(request):

    form = LinkForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'home'
        )

    return render(
        request,
        'create.html',
        {
            'form':form
        }
    )


@login_required
def update(request,id):

    link = get_object_or_404(
        LinkModel,
        id=id
    )

    form = LinkForm(
        request.POST or None,
        instance=link
    )

    if form.is_valid():

        form.save()

        return redirect(
            'home'
        )

    return render(
        request,
        'update.html',
        {
            'form':form
        }
    )


@login_required
def delete(request,id):

    link = get_object_or_404(
        LinkModel,
        id=id
    )

    link.delete()

    return redirect(
        'home'
    )