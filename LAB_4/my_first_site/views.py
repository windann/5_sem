from django.shortcuts import render

from django.views import View


# Create your views here.

def index(request):
    return render(request, 'my_first_site/welcome.html')


def variable(request):
    return render(request, 'my_first_site/variable.html', {'my_variable': 'Самый красивый цветок'})

class FlowersView(View):
    def get(self,request):
        data = {
            'flowers': [
                {'name': 'Роза', 'kolvo' : 25,'id':1},
                {'name': 'Кактус', 'kolvo': 1,'id':2},
                {'name': 'Лилия', 'kolvo': 46,'id':3},
                {'name': 'Хризантема', 'kolvo': 29,'id':4},

            ]
        }
        return render(request,'my_first_site/flowers.html',data)

class FlowerView(View):

    def get(self,request,id):
        data = {
            'flower': {
                'id' : id,
            }
        }
        return render(request,'my_first_site/flower.html',data)
