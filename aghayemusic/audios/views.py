from django.http import Http404
from django.shortcuts import render
from .models import Audios_file
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Singer
# Create your views here.
def search_music(request):
    q = request.GET.get('q')
    if q != None:
        audios = Audios_file.objects.search(q)
        last_music = Audios_file.objects.all().order_by('time')
        singers =Singer.objects.all()
        paginator = Paginator(audios,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'audios':audios,
            'lasts':last_music,
            'singers':singers,
            'lasts_2':last_music[:6]
            }
        return render(request,'search.html',context)
    else:
        raise Http404('404')