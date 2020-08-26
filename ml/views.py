from django.shortcuts import render
from django.http import HttpResponse
import pickle
from sklearn.model_selection import train_test_split

def home(request):
	return render(request,'ml/home.html')


def result(request):
	if(request.POST):
		pclass=int(request.POST.get('pclass'))
		age=int(request.POST.get('age'))
		sibsp=int(request.POST.get('sibsp'))
		parch=int(request.POST.get('parch'))
		fare=float(request.POST.get('fare'))
		sex=int(request.POST.get('sex'))
		q=int(request.POST.get('q'))
		s=int(request.POST.get('s'))
		x=[[1,pclass,age,sibsp,parch,fare,sex,q,s]]

		loaded_model=pickle.load(open('ml/finalized_model.sav','rb'))
		prediction=loaded_model.predict(x)



		context={'pclass':pclass,'age':age,'sibsp':sibsp,
		          'parch':parch,'fare':fare,'sex':sex,
		          's':s,'loaded_model':loaded_model,'prediction':prediction}
		return render(request,'ml/result.html',context)

	
