from django.shortcuts import render
from django.views.generic import View
from models import Music,Genres
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse



# Create your views here.

class Add_Music_Details(View):

    def get(self, request):
        genre = Genres.objects.all()

        return render(request, 'add_music_track.html',{'genre':genre})


    def post(self, request):
        title = request.POST['title']
        genre = request.POST['genre']
        rating = request.POST['rating']

        Music(title=title,genres_id=genre,rating=rating).save()
        return HttpResponseRedirect(reverse('music_show'))


class EditMusicTrackDetails(View):
    def get(self, request, id):
        music = Music.objects.get(id=id)

        return render(request, 'edit_music_track.html', {'music':music})

    def post(self, request, id):
        title = request.POST['title']
        genres = request.POST['genres']
        rating = request.POST['rating']

        Music.objects.filter(id=id).update(title=title,genres_id=genres,rating=rating)


        return HttpResponseRedirect(reverse('music_show'))

def MusicTrackDetails(request):
    music = Music.objects.all()
    # genres =Genres.objects.all()
    return render(request, 'show_music_track.html', {'music': music})

class Add_Genres_Details(View):

    def get(self, request):
        return render(request, 'add_genres.html')

    def post(self, request):
        name = request.POST['name']
        genre = request.POST['genre']

        Genres(name=name,genre=genre).save()
        return HttpResponseRedirect(reverse('genres_show'))

class EditGenresDetails(View):
    def get(self, request, id):
        genres = Genres.objects.get(id=id)

        return render(request, 'edit_genres.html', {'genres':genres})

    def post(self, request, id):
        name = request.POST['name']
        genre = request.POST['genre']

        Genres.objects.filter(id=id).update(name=name,genre=genre)


        return HttpResponseRedirect(reverse('genres_show'))


def GenresDetails(request):
    genres = Genres.objects.all()

    return render(request, 'show_genres.html', {'genres': genres})


def get_title_data(request):
    search_data=request.GET.get('get-data','')
    # print search_data
    data = Music.objects.filter(title=search_data)
    return HttpResponse(data)
