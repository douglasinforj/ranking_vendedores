import csv
from django.shortcuts import render, redirect
from .models import Venda
from .forms import UploadFileForm
from datetime import datetime

from django.db.models import Sum


def upload_vendas(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            decoded_file = arquivo.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            next(reader)  # Pular cabeçalho

            for row in reader:
                usuario = row[0]
                total_vendas = int(row[1])
                horario = datetime.strptime(row[2], "%H:%M").time()
                
                Venda.objects.create(usuario=usuario, total_vendas=total_vendas, horario=horario)

            return redirect('ranking')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})
    

def ranking_vendas(request):
    vendedores = Venda.objects.values('usuario').annotate(total=Sum('total_vendas')).order_by('-total')

    return render(request, 'ranking.html', {'vendedores': vendedores})