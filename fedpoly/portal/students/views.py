from django.shortcuts import render




def blog_details(request):

    return render(request, 'blog-details.html')


def soon(request):

    return render(request, 'soon.html')
