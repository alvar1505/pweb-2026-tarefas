from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")


def base(request):
    lista_users = [
        {"nome": "Álvaro", "matricula": 17, "idade": 17, "cidade": "spp"},
        {"nome": "Kaio", "matricula": 11, "idade": 17, "cidade": "spp"},
        {"nome": "julio", "matricula": 112233, "idade": 34, "cidade": "calçada da pague menos"},
        {"nome": "gustavo", "matricula": 123, "idade": 17, "cidade": "São Tomé"},
        {"nome": "dedé", "matricula": 110, "idade": 9, "cidade": "nao sei"},
    ]

    context = {
        "usuarios": lista_users,
    }
  
    return render(request, "app/base.html", context)
   