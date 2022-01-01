from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photo

# Create your views here.
@login_required(redirect_field_name='', login_url='/account/login/')
def photo_list(request):
    photos = Photo.objects.all()
    print(request.GET.get("next"))
    print(photos)
    return render(request, 'photo/list.html', {'photos' : photos})


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    login_url = '/account/login'
    redirect_field_name =''

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form' : form})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'

    login_url = '/account/login'
    redirect_field_name =''

    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']

    login_url = '/account/login'
    redirect_field_name =''
    
    template_name = 'photo/update.html'