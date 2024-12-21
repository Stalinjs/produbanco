from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verificar que los datos lleguen
        print(f"Usuario: {username}, Contraseña: {password}")

        # Guardar los datos
        nuevo_usuario = User(username=username, password=password)
        nuevo_usuario.save()
        # Aquí puedes agregar lógica para validar las credenciales
        return HttpResponse("Login attempt")
    return render(request, 'loginn.html')
def registro_view(request):
    return render(request, 'registro.html')

