from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Approvals
from . serializers import ApprovalsSerializer
import json
import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from joblib import load, dump
from sklearn import svm

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = ApprovalsSerializer

def ohe_value(df):
    ohe_col = load("col.joblib")
    cat_columns = ['gender', 'married', 'education', 'self_employed', 'property_area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    new_dict={}
    for i in ohe_col:
        if i in df_processed.columns:
            new_dict[i] = df_processed[i].values
        else:
            new_dict[i] = 0
    df1 = pd.DataFrame(new_dict)
    return df1


#@api_view(["POST"])
def approve_reject(unit):
    try:
        mdl = load("clf.joblib")
        #my_data=request.data
        #unit = np.array(list(my_data.values()))
        #unit = unit.reshape(1,-1)
        #scalers = load()
        #X = scalers.tranform(unit)
        sc = MinMaxScaler()
        X = sc.fit_transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred>0.52)
        new_df = pd.DataFrame(y_pred, columns=['Status'])
        new_df = new_df.replace({True: 'Approved', False: 'Rejected'})
        return "Your status is {}".format(new_df)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):

    if request.method =='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dependents = form.cleaned_data['dependents']
            applicant_income = form.cleaned_data['applicant_income']
            co_applicant_income = form.cleaned_data['co_applicant_income']
            loan_amt = form.cleaned_data['loan_amt']
            loan_term = form.cleaned_data['loan_term']
            credit_history = form.cleaned_data['credit_history']
            gender = form.cleaned_data['gender']
            married = form.cleaned_data['married']
            education =form.cleaned_data['education']
            self_employed = form.cleaned_data['self_employed']
            property_area = form.cleaned_data['property_area']
            my_dict = request.POST.dict()
            df = pd.DataFrame(my_dict, index=[0])
            # test we toga ve le data dummiser print(ohe_value(df))
            print(approve_reject(ohe_value(df)))

    form = ApprovalForm()

    return render(request, 'myform/csform.html', {'form':form})