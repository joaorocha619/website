from django.shortcuts import render

def user_login(request):
    user = {'username': 'John'}
    items = ['Item 1', 'Item 2', 'Item 3']
    context = {
        'user': user,
        'items': items,
    }
    return render(request, 'website/user_login.html', context)