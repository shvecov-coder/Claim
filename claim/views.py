from http.client import HTTPResponse
from django.shortcuts import render
from claim.models import Claim
from pathlib import Path
import os
from django.http import HttpResponse
import random
import docx

# Create your views here.

def create_report(claims):
    SAVE_NAME = str(random.randint(1, 1001)) + '.docx'

    BASE_DIR = Path(__file__).resolve().parent.parent

    try:
        dir = BASE_DIR / '/static/template_doc/программа_template.docx'
        print(dir)
        currentDocument = docx.Document(dir)
    except FileNotFoundError:
        return
    
    table = currentDocument.add_table(rows=len(claims), cols=3)
    table.style = 'poigraem_table'

    for row in table.rows:
        row.cells[0].width = docx.shared.Inches(0.3)
        row.cells[1].width = docx.shared.Inches(3.5)
    
    hdr_cells = table.rows[0].cells
    hdr_cells[1].paragraphs[0].add_run(claims[0].name_claim)

    try:
        dir = str(BASE_DIR) + os.path.dirname('/static/temp_files/' + SAVE_NAME)
        currentDocument.save(dir)
    except:
        return

'''
def create_programm_from_sxml():
    PATH_MAIN = ''
    count_rows = 0

    for i, row in enumerate(sheet.rows):
        if i == 0:
            continue
        hdr_cells = table.rows[i - 1].cells
        hdr_cells[0].paragraphs[0].add_run(str(i)).bold = False
        hdr_cells[1].paragraphs[0].add_run(row[6].value).bold = True
        if row[1].value is None:
            break
        hdr_cells[1].paragraphs[0].add_run('\n' + row[1].value + ', ')
        if row[2].value != '-' and not row[2].value is None:
            hdr_cells[1].paragraphs[0].add_run(str(row[2].value) + ' кл. ')
        hdr_cells[1].paragraphs[0].add_run('(' + row[3].value + ')')
        hdr_cells[1].paragraphs[0].add_run('\nпреп. ' + row[4].value)
        if row[5].value != '-':
            hdr_cells[1].paragraphs[0].add_run('\nконц. ' + row[5].value)
        hdr_cells[2].text = row[7].value

    name_file = 'tep' + '.docx'
    try:
        currentDocument.save(PATH_MAIN + '/' + name_file)
    except:
        return
'''

def index(request):
    if request.method == 'POST':
        type_cl = request.POST.get('type_claim')
        select_cl = int(request.POST.get('select_claim'))
        name_cl = request.POST.get('name_claim')
        parent_cl = request.POST.get('parent_claim')
        class_cl = request.POST.get('class_claim')
        concert_cl = request.POST.get('concert_claim')
        sity_cl = request.POST.get('sity_claim')
        prog_cl = request.POST.get('prog_claim')
        url_cl = request.POST.get('url_claim')

        data = {'type': type_cl, 'select': select_cl, 'name': name_cl,
                'parent': parent_cl, 'class': class_cl, 'concert': concert_cl,
                'sity': sity_cl, 'prog': prog_cl, 'url': url_cl
                }
        claim = Claim.objects.create(type_claim=type_cl,
                                    select_claim=select_cl,
                                    name_claim=name_cl,
                                    parent_claim=parent_cl,
                                    class_claim=class_cl,
                                    concert_claim=concert_cl,
                                    sity_claim=sity_cl,
                                    prog_claim=prog_cl,
                                    url_claim=url_cl)
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