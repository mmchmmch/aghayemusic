from email.mime import audio
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from audios.models import Singer
from audios.models import Audios_file
def index_page(request):
    audios = Audios_file.objects.all().order_by('view')[:100]
    last_music = Audios_file.objects.all().order_by('time')
    singers =Singer.objects.all()
    paginator = Paginator(audios, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',
    context=
    {
        'page_obj': page_obj,
        'audios':audios,
        'lasts':last_music,
        'singers':singers,
        'lasts_2':last_music[:6]
    }
    )
