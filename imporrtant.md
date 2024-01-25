Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x000001FE780B11E0>>.

هذا الخطا يظهر في 
context_proceor 
 بسبب انه مش متحقق ان اليوزر تم تسجيله بالفعل ولحا هذا الايروو 


 def get_detail(request):
    if  request.user.is_authenticated:

        ###### هنا يتم وضع الكود الخاص بك 
    else:
        return {} 