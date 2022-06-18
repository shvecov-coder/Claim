from http.client import HTTPResponse
from django.shortcuts import render
from claim.models import Claim
from pathlib import Path
import os
from django.http import HttpResponse
import random
import docx

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

def create_report(claims):
    SAVE_NAME = str(random.randint(1, 1001)) + '.docx'

    try:
        dir = os.path.abspath(str(BASE_DIR) + '/static/template_doc/программа_template.docx')
        currentDocument = docx.Document(dir)
    except FileNotFoundError:
        return
    
    table = currentDocument.add_table(rows=len(claims), cols=3)
    table.style = 'poigraem_table'

    for row in table.rows:
        row.cells[0].width = docx.shared.Inches(0.3)
        row.cells[1].width = docx.shared.Inches(3.5)
    
    for i, claim in enumerate(claims):
        hdr_cells = table.rows[i].cells
        hdr_cells[0].paragraphs[0].add_run(str(i + 1)).bold = False
        hdr_cells[1].paragraphs[0].add_run(claim.city_claim).bold = True
        hdr_cells[1].paragraphs[0].add_run('\n' + claim.name_claim + ', ')
        hdr_cells[1].paragraphs[0].add_run(str(claim.class_claim) + ' кл. ')
        hdr_cells[1].paragraphs[0].add_run('(' + str(claim.select_claim) + ')')
        hdr_cells[1].paragraphs[0].add_run('\nпреп. ' + claim.parent_claim)
        if claim.concert_claim != '':
            hdr_cells[1].paragraphs[0].add_run('\nконц. ' + claim.concert_claim)
        hdr_cells[2].text = claim.prog_claim
    try:
        dir = os.path.abspath(str(BASE_DIR) + ('/static/temp_files/' + SAVE_NAME))
        currentDocument.save(dir)
    except:
        return

def index(request):
    if request.method == 'POST':
        print('POST POST POST')
        type_cl = request.POST.get('type_claim')
        select_cl = request.POST.get('select_claim')
        name_cl = request.POST.get('name_claim')
        parent_cl = request.POST.get('parent_claim')
        class_cl = request.POST.get('class_claim')
        concert_cl = request.POST.get('concert_claim')
        city_cl = request.POST.get('city_claim')
        prog_cl = request.POST.get('prog_claim')
        url_cl = request.POST.get('url_claim')

        data = {'type': type_cl, 'select': select_cl, 'name': name_cl,
                'parent': parent_cl, 'class': class_cl, 'concert': concert_cl,
                'city': city_cl, 'prog': prog_cl, 'url': url_cl
                }
        claim = Claim.objects.create(type_claim=type_cl,
                                    select_claim=select_cl,
                                    name_claim=name_cl,
                                    parent_claim=parent_cl,
                                    class_claim=class_cl,
                                    concert_claim=concert_cl,
                                    city_claim=city_cl,
                                    prog_claim=prog_cl,
                                    url_claim=url_cl,
                                    place_claim=0)
        data['id'] = claim.id
        return render(request, 'apply.html', context=data)
    return render(request, 'index.html')

def admin(request):
    if request.GET.get('code') == 'report':
        claims = Claim.objects.all()
        create_report(claims)
        return HttpResponse('Report Success')
    else:
        claims = Claim.objects.all()
        return render(request, 'admin.html', context={'claims': claims})

def generate(request):
    return render(request, 'generate.html')

def excel(request):
    return render(request, 'excel.html')

def apply(request):
    if request.method == 'POST':
        type_cl = request.POST.get('type_claim')
        select_cl = request.POST.get('select_claim')
        name_cl = request.POST.get('name_claim')
        parent_cl = request.POST.get('parent_claim')
        class_cl = request.POST.get('class_claim')
        concert_cl = request.POST.get('concert_claim')
        city_cl = request.POST.get('city_claim')
        prog_cl = request.POST.get('prog_claim')
        url_cl = request.POST.get('url_claim')

        data = {'type': type_cl, 'select': select_cl, 'name': name_cl,
                'parent': parent_cl, 'class': class_cl, 'concert': concert_cl,
                'city': city_cl, 'prog': prog_cl, 'url': url_cl
                }
        claim = Claim.objects.create(type_claim=type_cl,
                                    select_claim=select_cl,
                                    name_claim=name_cl,
                                    parent_claim=parent_cl,
                                    class_claim=class_cl,
                                    concert_claim=concert_cl,
                                    city_claim=city_cl,
                                    prog_claim=prog_cl,
                                    url_claim=url_cl,
                                    place_claim=0)
        data['id'] = claim.id
        return render(request, 'apply.html', context=data)
    else:
        return HttpResponse('Error')