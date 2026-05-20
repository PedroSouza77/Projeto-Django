from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import LinkModel
from .forms import LinkForm, LoginForm

def login(request):

    form = LoginForm(
        request.POST or None
    )

    if request.method == 'POST':

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        try:

            user_db = User.objects.get(
                email=email
            )

            user = authenticate(
                username=user_db.username,
                password=password
            )

        except User.DoesNotExist:

            user = None


        if user:

            auth_login(
                request,
                user
            )

            return redirect(
                'home'
            )

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )
    
def logout(request):

    auth_logout(request)

    return render(
     request,
        'logout.html'
    )

@login_required
def home(request):

    links = LinkModel.objects.all()

    return render(
        request,
        'index.html',
        {
            'links': links
        }
    )
    
@login_required
def list_links(request):

    links = LinkModel.objects.all()

    return render(
        request,
        'list.html',
        {
            'links': links
        }
    )
    
@login_required
def edit_links(request):

    links = LinkModel.objects.all()

    return render(
        request,
        'edit.html',
        {
            'links': links
        }
    )


@login_required
def delete_links(request):

    links = LinkModel.objects.all()

    return render(
        request,
        'delete_list.html',
        {
            'links': links
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
            'form': form
        }
    )


@login_required
def update(request, id):

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
            'form': form
        }
    )


@login_required
def delete(request, id):

    link = get_object_or_404(
        LinkModel,
        id=id
    )

    link.delete()

    return redirect(
        'home'
    )

