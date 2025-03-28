from django.shortcuts import render,redirect
from .models import movie_info
from . form import movieForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def create(request):
    if request.POST:
       print("hi")
       
       frm = movieForm(request.POST,request.FILES)
       print(request.FILES) 
       if frm.is_valid():
           frm.save()
           return redirect('create')
    else:
        frm = movieForm()
        
        
    return render(request,'create.html',{'frm':frm})
@login_required(login_url='login')
def edit(request, pk):
    instance_of_the_movie = movie_info.objects.get(id = pk)
    print(instance_of_the_movie)
    frm =  movieForm(instance=instance_of_the_movie)
    if request.POST:
        
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # plot = request.POST.get('plot')
        # instance_of_the_movie.title = title
        # instance_of_the_movie.year = year
        # instance_of_the_movie.plot = plot
        # instance_of_the_movie.save()
        frm1 = movieForm(request.POST,instance=instance_of_the_movie)
        if frm1.is_valid():
            frm1.save()
        return redirect('list')
    else:
        movies_visited = request.session.get('movies_visited',[])
        movies_visited.insert(0,pk)
        request.session['movies_visited'] = movies_visited


    return render(request,'edit.html',{'frm':frm})

# deleteing a movie 
@login_required(login_url='login')
def delete(request,pk):
    
    instance = movie_info.objects.get(id = pk)
    instance.delete()
    return redirect('list')



@login_required(login_url='login')
def list(request):
    # field lookup year__gt =2020
    movies_visited = request.session.get('movies_visited',[])
    movies_visited_details = movie_info.objects.filter(pk__in = movies_visited)
    visits = int(request.COOKIES.get('visits',0))
    visits += 1
    movie_data = movie_info.objects.all()
    responce = render(request,'list.html',{'movie':movie_data,'visits':visits,'movies_visited_details':movies_visited_details})
    responce.set_cookie('visits',visits)
    return responce


