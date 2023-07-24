from django.shortcuts import render,redirect
import requests
import json
from django.http import HttpResponse
from  viewapp.client import get_token
from json import dumps
from django.http.response import JsonResponse
from django.views.generic import View
from viewapp.froms import loginfrom,createForm, updateForm
from viewapp.models import client
import six



# Create your views here.
# def index (request):
#      r=requests.get('https://api.covid19api.com/countries')
#      t= r.json()
#      return render (request,'viewapp/index.html',{'res': t})


class LoginView(View):
    def get(self, request, *args, **kwargs):       
        form = loginfrom()
        return render(request, 'login_from.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = loginfrom(request.POST)
        if form.is_valid():
            post_data= {'email': form.cleaned_data['email'],'password': form.cleaned_data['password']}
            headers = {'content-type': "application/json",
                        'Authorization': "" }

            response = requests.post("http://192.168.0.41:3000/api/users/login", data=dumps(post_data), headers=headers)
            
            json_data1=json.dumps(response.json())
            json_data = json.loads( json_data1)
            # token_string = json_data["token"]

            request.session['token_string']=json_data["token"]
            header = { 'Authorization':'Bearer %s'%request.session['token_string']}
            response = requests.get("http://192.168.0.41:3000/api/sliders/all",headers=header)

            data=response.json()

            list_data=[]
            for i in range(len(data['data'])):
                list_data.append(data['data'][i])
            context ={'list_data': list_data}

            return render(request, 'list_data.html', context)




class create(View):
    def get(self, request, *args, **kwargs):       
        form = createForm()
        return render(request, 'create.html', {'form': form}) 

    def post(self, request, *args, **kwargs):
        form =createForm(request.POST)
        if form.is_valid():
            post_data= {'title': form.cleaned_data['title'],'description': form.cleaned_data['description'],'priority': form.cleaned_data['priority'],'created_by': form.cleaned_data['created_by']}
            headers = {'content-type': "application/json",
                        'Authorization': 'Bearer %s'%request.session['token_string'] }
      
            response = requests.post("http://192.168.0.41:3000/api/sliders/create", data=dumps(post_data), headers=headers)     
            return render(request, 'success.html')


def view(request,id):  
        headers = {'content-type': "application/json",
                        'Authorization': 'Bearer %s'%request.session['token_string'] }
        response = requests.get("http://192.168.0.41:3000/api/sliders/slider/"+id, headers=headers)
        data=response.json()
        # request.session['info']=data
        list_data=[]
        list_data.append(data['data'])
        context ={'list_data': list_data}
        return render(request, 'editdata.html', context)
# class update(View):
#     def get(self, request,id, *args, **kwargs): 
def Update(request,id): 
    if request.method == 'GET':
        headers = {'content-type': "application/json",
                        'Authorization': 'Bearer %s'%request.session['token_string'] }

        response = requests.get("http://192.168.0.41:3000/api/sliders/slider/"+id, headers=headers)
        data=response.json() 
        data1=json.dumps(data)
        data2 = json.loads(data1)
        make_data= data2["data"]
        form = updateForm(request.GET or None, initial=make_data)
    
        return render(request, 'update.html', {'form': form}) 
        
    else: 
        form = updateForm(request.POST or None) 
        if form.is_valid():
            post_data= {'id': form.cleaned_data['id'],'title': form.cleaned_data['title'],'description': form.cleaned_data['description'],'priority': form.cleaned_data['priority'],'created_by': form.cleaned_data['created_by'] }
            print(post_data)
            headers = {'content-type': "application/json",
                            'Authorization': 'Bearer %s'%request.session['token_string'] }
    
            response = requests.patch("http://192.168.0.41:3000/api/sliders/update",data=dumps(post_data), headers=headers) 
            print(response.text)  
            list_data=post_data
            
            context ={'list_data': list_data}
            return render(request, 'singledata.html', context)

# def SuccessView(request):
#     return render(request, 'success.html')



def delete(request,id):
        headers = {'content-type': "application/json",
                        'Authorization': 'Bearer %s'%request.session['token_string'] }
        response = requests.delete("http://192.168.0.41:3000/api/sliders/delete/"+id,headers=headers)
     
        lists=[]
        context={'delete_message' : "Delete Done"}
        return render(request,'delete.html', context)
  
   
