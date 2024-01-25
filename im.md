def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password = request.POST.get('password')
        passwordconfirmation = request.POST.get('passwordconfirmation')

        if not first_name or not last_name or not email or not phonenumber or not country or not city or not password or not passwordconfirmation:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'registration/signup.html')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return render(request, 'registration/signup.html')

        if password != passwordconfirmation:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=email,
            email=email,
            password=password
        )
        profile = Profile.objects.create(
            user=user,
            phonenumber=phonenumber,
            country=country,
            city=city
        )
        login(request, user)
        return render(request, 'registration/signup.html')
    else:
        
        return render(request, 'registration/signup.html')

.............................
    /* ff 3.6+ */
    background:-moz-linear-gradient(90deg, rgba(220, 0, 255, 0.71) 50%, rgba(0, 188, 212, 1) 100%, rgba(238, 130, 130, 1) 100%); 

    /* safari 5.1+,chrome 10+ */
    background:-webkit-linear-gradient(90deg, rgba(220, 0, 255, 0.71) 50%, rgba(0, 188, 212, 1) 100%, rgba(238, 130, 130, 1) 100%);

    /* opera 11.10+ */
    background:-o-linear-gradient(90deg, rgba(220, 0, 255, 0.71) 50%, rgba(0, 188, 212, 1) 100%, rgba(238, 130, 130, 1) 100%);

    /* ie 6-9 */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#EE8282', endColorstr='#DC00FF', GradientType=0 );

    /* ie 10+ */
    background:-ms-linear-gradient(90deg, rgba(220, 0, 255, 0.71) 50%, rgba(0, 188, 212, 1) 100%, rgba(238, 130, 130, 1) 100%);

    /* global 94%+ browsers support */
    background:linear-gradient(90deg, rgba(220, 0, 255, 0.71) 50%, rgba(0, 188, 212, 1) 100%, rgba(238, 130, 130, 1) 100%);

..................................
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4908173502472152"
     crossorigin="anonymous"></script>

................................
https://mohamedibrahim27.github.io/mohamed/?fbclid=IwAR00Oyb6G6yK-FVqqgZbsGG3BjMvJY_-WbcW6CpBxF2WJwGgm_RxmR-hrJI

...............

https://cssfx.netlify.app/
btn btn-outline-success-modify my-2 my-sm-0

