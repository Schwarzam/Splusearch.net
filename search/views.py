from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
from search.graph import Graph, searchcords
from io import BytesIO
import matplotlib.pyplot as plt
import base64
from index.models import create_model, Ref, Saved
from django.db import connections, transaction
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required()
def searchby(request):
    cache.clear()
    return render(request, 'search/searchby.html')

@login_required()
def searchid(request):
    if request.method == 'POST':
        cache.clear()
        id = request.POST.get("gal")
        if ' ' or '  ' in id:
            mylist = id.replace(' ', '')
        if ', ' in id:
            mylist = id.split(', ')
        else:
            mylist = id.split(',')

        df = pd.DataFrame(columns = ['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                                  'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])

        for x in mylist:
            try:
                FIELD = x.split(sep='.')
                FIELD = FIELD[1]
                Fieldx = FIELD
                if '-' in FIELD:
                    FIELD = FIELD.replace('-','_')
                Galaxy = create_model(FIELD).objects.filter(id = x).first()
                Field = Ref.objects.filter(name = str(FIELD)).first()
                Status = Field.status

                #Legacy survey image link
                image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.ra}&dec={Galaxy.dec}&layer=dr8&pixscale=0.50"
                #SPLUS image link
                image2 = f"https://datalab.noao.edu/svc/cutout?col=splus_dr1&siaRef={Fieldx}_R_swp.fz&extn=1&POS={Galaxy.ra},{Galaxy.dec}&SIZE=0.04,0.04&preview=true"

                ## Plotting the 12 filters
                plot = Graph(Galaxy)
                figfile = BytesIO()
                fig = plot.autoplot().savefig(figfile, format='png')
                figfile.seek(0)
                figdata_png = base64.b64encode(figfile.getvalue())
                result = str(figdata_png)[2:-1]
                petro = BytesIO()
                fig2 = plot.petroplot().savefig(petro, format='png')
                petro.seek(0)
                petro_png = base64.b64encode(petro.getvalue())
                result2 = str(petro_png)[2:-1]

                ## APPENDING RESULT TO DATAFRAME ##
                data = {'result':[result],'result2':[result2],'SFRA':[None], 'SFDec':[None], 'ID':[Galaxy.id],'RA':[Galaxy.ra],'Dec':[Galaxy.dec],'PhotoFlag':[Galaxy.photoflag],'FWHM':[Galaxy.fwhm],
                        'uJAVA_auto':[Galaxy.ujava_auto], 'F378_auto':[Galaxy.f378_auto], 'F395_auto':[Galaxy.f395_auto],'F410_auto':[Galaxy.f410_auto], 'F430_auto':[Galaxy.f430_auto],
                        'g_auto':[Galaxy.g_auto],'F515_auto':[Galaxy.f515_auto] , 'r_auto':[Galaxy.r_auto], 'F660_auto':[Galaxy.f660_auto],
                        'i_auto':[Galaxy.i_auto], 'F861_auto':[Galaxy.f861_auto], 'z_auto':[Galaxy.z_auto], 'FieldS': [Status], 'image':[image],'image2':[image2]}

                df1 = pd.DataFrame(data, columns=['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                                  'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
                df = df.append(df1)
            except:
                continue
        return render(request, 'search/searchcoords.html', {'df':df})

@login_required()
def searchcoords(request):
    if request.method == 'POST':
        cache.clear()
        ra = request.POST.get('RA')
        dec = request.POST.get('Dec')

        ## Splitting the RAs and Decs
        if ' ' or '  ' in ra:
            ml = ra.replace(' ', '')
        if ', ' in ra:
            ml = ra.split(', ')
        else:
            ml = ra.split(',')
        if ' ' or '  ' in dec:
            ml2 = dec.replace(' ', '')
        if ', ' in dec:
            ml2 = dec.split(', ')
        else:
            ml2 = dec.split(',')

        df1 = pd.DataFrame({'RA':ml})
        df2 = pd.DataFrame({'Dec':ml2})
        result = pd.concat([df2, df1], axis=1)
        df = pd.DataFrame(columns = ['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                          'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
        for index, row in result.iterrows():
            try:
                #Giving coordinates to the matching function
                Galaxy = searchcords(float(row.RA), float(row.Dec))
                Galaxy = Galaxy.search() #It returns the closest one
                Status = Galaxy[1]
                Galaxy = Galaxy[0] #Here's the query result

                Fieldx = Galaxy.id
                FIELD = Fieldx.split(sep='.')
                Fieldx = FIELD[1] #Getting the Galaxy Field

                #Legacy survey image link
                image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.ra}&dec={Galaxy.dec}&layer=dr8&pixscale=0.50"
                #SPLUS image link
                image2 = f"https://datalab.noao.edu/svc/cutout?col=splus_dr1&siaRef={Fieldx}_R_swp.fz&extn=1&POS={Galaxy.ra},{Galaxy.dec}&SIZE=0.04,0.04&preview=true"

                ## Plotting the 12 filters
                plot = Graph(Galaxy)
                figfile = BytesIO()
                fig = plot.autoplot().savefig(figfile, format='png')
                figfile.seek(0)
                figdata_png = base64.b64encode(figfile.getvalue())
                result = str(figdata_png)[2:-1]
                petro = BytesIO()
                fig2 = plot.petroplot().savefig(petro, format='png')
                petro.seek(0)
                petro_png = base64.b64encode(petro.getvalue())
                result2 = str(petro_png)[2:-1]


                ## APPENDING RESULT TO DATAFRAME ##
                data = {'result':[result],'result2':[result2],'SFRA':[row.RA], 'SFDec':[row.Dec], 'ID':[Galaxy.id],'RA':[Galaxy.ra],'Dec':[Galaxy.dec],'PhotoFlag':[Galaxy.photoflag],'FWHM':[Galaxy.fwhm],
                        'uJAVA_auto':[Galaxy.ujava_auto], 'F378_auto':[Galaxy.f378_auto], 'F395_auto':[Galaxy.f395_auto],'F410_auto':[Galaxy.f410_auto], 'F430_auto':[Galaxy.f430_auto],
                        'g_auto':[Galaxy.g_auto],'F515_auto':[Galaxy.f515_auto] , 'r_auto':[Galaxy.r_auto], 'F660_auto':[Galaxy.f660_auto],
                        'i_auto':[Galaxy.i_auto], 'F861_auto':[Galaxy.f861_auto], 'z_auto':[Galaxy.z_auto], 'FieldS': [Status], 'image':[image],'image2':[image2]}

                df1 = pd.DataFrame(data, columns=['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                                  'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
                df = df.append(df1)
            except:
                continue
        return render(request, 'search/searchcoords.html', {'df':df})

@login_required()
def upload(request):
    if request.method == "POST":
        f = request.FILES['csvfile']
        data = pd.read_csv(f, nrows=20)
        df = pd.DataFrame(columns = ['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                          'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
        for index, row in data.iterrows():
            try:
                #Giving coordinates to the matching function
                Galaxy = searchcords(float(row.RA), float(row.Dec))
                Galaxy = Galaxy.search() #It returns the closest one
                Status = Galaxy[1]
                Galaxy = Galaxy[0] #Here's the query result

                Fieldx = Galaxy.id
                FIELD = Fieldx.split(sep='.')
                Fieldx = FIELD[1] #Getting the Galaxy Field

                #Legacy survey image link
                image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.ra}&dec={Galaxy.dec}&layer=dr8&pixscale=0.50"
                #SPLUS image link
                image2 = f"https://datalab.noao.edu/svc/cutout?col=splus_dr1&siaRef={Fieldx}_R_swp.fz&extn=1&POS={Galaxy.ra},{Galaxy.dec}&SIZE=0.04,0.04&preview=true"

                ## Plotting the 12 filters
                plot = Graph(Galaxy)
                figfile = BytesIO()
                fig = plot.autoplot().savefig(figfile, format='png')
                figfile.seek(0)
                figdata_png = base64.b64encode(figfile.getvalue())
                result = str(figdata_png)[2:-1]
                petro = BytesIO()
                fig2 = plot.petroplot().savefig(petro, format='png')
                petro.seek(0)
                petro_png = base64.b64encode(petro.getvalue())
                result2 = str(petro_png)[2:-1]


                ## APPENDING RESULT TO DATAFRAME ##
                data = {'result':[result],'result2':[result2],'SFRA':[row.RA], 'SFDec':[row.Dec], 'ID':[Galaxy.id],'RA':[Galaxy.ra],'Dec':[Galaxy.dec],'PhotoFlag':[Galaxy.photoflag],'FWHM':[Galaxy.fwhm],
                        'uJAVA_auto':[Galaxy.ujava_auto], 'F378_auto':[Galaxy.f378_auto], 'F395_auto':[Galaxy.f395_auto],'F410_auto':[Galaxy.f410_auto], 'F430_auto':[Galaxy.f430_auto],
                        'g_auto':[Galaxy.g_auto],'F515_auto':[Galaxy.f515_auto] , 'r_auto':[Galaxy.r_auto], 'F660_auto':[Galaxy.f660_auto],
                        'i_auto':[Galaxy.i_auto], 'F861_auto':[Galaxy.f861_auto], 'z_auto':[Galaxy.z_auto], 'FieldS': [Status], 'image':[image],'image2':[image2]}

                df1 = pd.DataFrame(data, columns=['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                                  'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
                df = df.append(df1)
            except:
                continue
        return render(request, 'search/searchcoords.html', {'df':df})
        cache.clear()

@csrf_exempt
def save(request):
    if request.method == "POST":
        value = request.POST.get("value")
        ID = str(value)
        FIELD = ID.split(sep='.')
        FIELD = FIELD[1]
        if '-' in FIELD:
            FIELD = FIELD.replace('-','_')

        Galaxy = create_model(FIELD).objects.values('ra', 'dec', 'id').filter(id = ID).first()
        post = Saved(id = Galaxy['id'], ra = Galaxy['ra'], dec = Galaxy['dec'], user = str(request.user.username))
        post.save()

        ID = Galaxy['id']
        return JsonResponse({"success": f'Saved {ID}'})

@csrf_exempt
def delete(request):
    if request.method == "POST":
        value = request.POST.get("value")
        ID = str(value)

        Galaxy = Saved.objects.filter(id = ID, user = request.user.username).first()
        Galaxy.delete()

        return JsonResponse({"success": f'Deleted!'})

@csrf_exempt
def searchfromprof(request, param):
    cache.clear()
    id = param
    if ' ' or '  ' in id:
        mylist = id.replace(' ', '')
    if ', ' in id:
        mylist = id.split(', ')
    else:
        mylist = id.split(',')

    df = pd.DataFrame(columns = ['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                              'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])

    for x in mylist:
        try:
            FIELD = x.split(sep='.')
            FIELD = FIELD[1]
            Fieldx = FIELD
            if '-' in FIELD:
                FIELD = FIELD.replace('-','_')
            Galaxy = create_model(FIELD).objects.filter(id = x).first()
            Field = Ref.objects.filter(name = str(FIELD)).first()
            Status = Field.status

            #Legacy survey image link
            image = f"http://legacysurvey.org/viewer/cutout.jpg?ra={Galaxy.ra}&dec={Galaxy.dec}&layer=dr8&pixscale=0.50"
            #SPLUS image link
            image2 = f"https://datalab.noao.edu/svc/cutout?col=splus_dr1&siaRef={Fieldx}_R_swp.fz&extn=1&POS={Galaxy.ra},{Galaxy.dec}&SIZE=0.04,0.04&preview=true"

            ## Plotting the 12 filters
            plot = Graph(Galaxy)
            figfile = BytesIO()
            fig = plot.autoplot().savefig(figfile, format='png')
            figfile.seek(0)
            figdata_png = base64.b64encode(figfile.getvalue())
            result = str(figdata_png)[2:-1]
            petro = BytesIO()
            fig2 = plot.petroplot().savefig(petro, format='png')
            petro.seek(0)
            petro_png = base64.b64encode(petro.getvalue())
            result2 = str(petro_png)[2:-1]

            ## APPENDING RESULT TO DATAFRAME ##
            data = {'result':[result],'result2':[result2],'SFRA':[None], 'SFDec':[None], 'ID':[Galaxy.id],'RA':[Galaxy.ra],'Dec':[Galaxy.dec],'PhotoFlag':[Galaxy.photoflag],'FWHM':[Galaxy.fwhm],
                    'uJAVA_auto':[Galaxy.ujava_auto], 'F378_auto':[Galaxy.f378_auto], 'F395_auto':[Galaxy.f395_auto],'F410_auto':[Galaxy.f410_auto], 'F430_auto':[Galaxy.f430_auto],
                    'g_auto':[Galaxy.g_auto],'F515_auto':[Galaxy.f515_auto] , 'r_auto':[Galaxy.r_auto], 'F660_auto':[Galaxy.f660_auto],
                    'i_auto':[Galaxy.i_auto], 'F861_auto':[Galaxy.f861_auto], 'z_auto':[Galaxy.z_auto], 'FieldS': [Status], 'image':[image],'image2':[image2]}

            df1 = pd.DataFrame(data, columns=['result','result2','SFRA','SFDec','ID','RA','Dec','PhotoFlag','FWHM','uJAVA_auto', 'F378_auto', 'F395_auto', 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto',
                                              'r_auto', 'i_auto', 'F660_auto', 'F861_auto', 'z_auto', 'FieldS', 'image','image2'])
            df = df.append(df1)
        except:
            continue
    return render(request, 'search/searchcoords.html', {'df':df})
