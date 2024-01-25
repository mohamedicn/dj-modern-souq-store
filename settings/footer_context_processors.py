from.models import Settings

def footer(request):
    footer=Settings.objects.last()
    return{
        'footer':footer,
    }