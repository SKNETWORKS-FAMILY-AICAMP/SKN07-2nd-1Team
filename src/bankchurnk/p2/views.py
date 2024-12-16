from django.shortcuts import render
from p2.forms import *
from django.http import HttpResponse

import os
import pandas as pd
import numpy as np

from scipy.stats import uniform, randint

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import cross_validate
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import make_pipeline


from sklearn.metrics import f1_score, confusion_matrix, precision_score, recall_score
from sklearn.compose import make_column_transformer
import pickle

with open('rscv_gbc_model.pkl', 'rb') as f:
    gbc_model = pickle.load(f)

# RDF

# XGB


def gb_predict(request):
    result = "none"
    pred_message = ""
    if request.method == 'POST':
        form = BankCustomerForm(request.POST)
        if form.is_valid():
            creditscore = form['creditscore'].value()
            
            # geography_choice = form['geography_choice'].value
            geography_choices = (('France', 'France'), ('Spain', 'Spain'), ('Germany', 'Germany'))
            geography_choice = dict(geography_choices)[form.cleaned_data["geography_choice"]]

            # gender_choice = form['gender_choice'].value
            gender_choices = (('Female', 'Female'), ('Male', 'Male'))
            gender_choice = dict(gender_choices)[form.cleaned_data["gender_choice"]]

            card_type_choices = (('DIAMOND', 'DIAMOND'), ('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ('PLATINUM', 'PLATINUM'))
            card_type_choice = dict(card_type_choices)[form.cleaned_data["card_type_choice"]]

            age = form['age'].value()
            tenure = form['tenure'].value()
            balance = form['balance'].value()
            num_products = form['num_products'].value()
            has_card = form['has_card'].value()
            is_active_member = form['is_active_member'].value()
            estimated_salary = form['estimated_salary'].value()
            complain = form['complain'].value()
            satisfaction_score = form['satisfaction_score'].value()


            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]
            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]

            inner_data = [628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']
            inner_data[0] = creditscore
            inner_data[1] = age
            inner_data[2] = tenure
            inner_data[3] = balance
            inner_data[4] = num_products
            inner_data[5] = has_card
            inner_data[6] = is_active_member
            inner_data[7] = estimated_salary
            inner_data[8] = complain
            inner_data[9] = satisfaction_score
            inner_data[10] = geography_choice
            inner_data[11] = gender_choice
            inner_data[12] = card_type_choice
            data = [inner_data]
            
            pred = gbc_model.predict(data)
            if pred[0] == 0:
                pred_message = 'Stay'
            else:
                pred_message = 'Exit'
            return render(request, 'predict.html', { 'form':form , 'result': pred_message, 'test': 'gb_predict'})
    else:
        form = BankCustomerForm()
    
    return render(request, 'predict.html', { 'form':form})



def rdf_predict(request):
    result = "none"
    pred_message = ""
    if request.method == 'POST':
        form = BankCustomerForm(request.POST)
        if form.is_valid():
            creditscore = form['creditscore'].value()
            
            # geography_choice = form['geography_choice'].value
            geography_choices = (('France', 'France'), ('Spain', 'Spain'), ('Germany', 'Germany'))
            geography_choice = dict(geography_choices)[form.cleaned_data["geography_choice"]]

            # gender_choice = form['gender_choice'].value
            gender_choices = (('Female', 'Female'), ('Male', 'Male'))
            gender_choice = dict(gender_choices)[form.cleaned_data["gender_choice"]]

            card_type_choices = (('DIAMOND', 'DIAMOND'), ('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ('PLATINUM', 'PLATINUM'))
            card_type_choice = dict(card_type_choices)[form.cleaned_data["card_type_choice"]]

            age = form['age'].value()
            tenure = form['tenure'].value()
            balance = form['balance'].value()
            num_products = form['num_products'].value()
            has_card = form['has_card'].value()
            is_active_member = form['is_active_member'].value()
            estimated_salary = form['estimated_salary'].value()
            complain = form['complain'].value()
            satisfaction_score = form['satisfaction_score'].value()


            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]
            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]

            inner_data = [628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']
            inner_data[0] = creditscore
            inner_data[1] = age
            inner_data[2] = tenure
            inner_data[3] = balance
            inner_data[4] = num_products
            inner_data[5] = has_card
            inner_data[6] = is_active_member
            inner_data[7] = estimated_salary
            inner_data[8] = complain
            inner_data[9] = satisfaction_score
            inner_data[10] = geography_choice
            inner_data[11] = gender_choice
            inner_data[12] = card_type_choice
            data = [inner_data]
            
            pred = gbc_model.predict(data)
            if pred[0] == 0:
                pred_message = 'Stay'
            else:
                pred_message = 'Exit'
            return render(request, 'predict.html', { 'form':form , 'result': pred_message, 'test': 'rdf_predict'})
    else:
        form = BankCustomerForm()
    
    return render(request, 'predict.html', { 'form':form})


def xfb_predict(request):
    result = "none"
    pred_message = ""
    if request.method == 'POST':
        form = BankCustomerForm(request.POST)
        if form.is_valid():
            creditscore = form['creditscore'].value()
            
            # geography_choice = form['geography_choice'].value
            geography_choices = (('France', 'France'), ('Spain', 'Spain'), ('Germany', 'Germany'))
            geography_choice = dict(geography_choices)[form.cleaned_data["geography_choice"]]

            # gender_choice = form['gender_choice'].value
            gender_choices = (('Female', 'Female'), ('Male', 'Male'))
            gender_choice = dict(gender_choices)[form.cleaned_data["gender_choice"]]

            card_type_choices = (('DIAMOND', 'DIAMOND'), ('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ('PLATINUM', 'PLATINUM'))
            card_type_choice = dict(card_type_choices)[form.cleaned_data["card_type_choice"]]

            age = form['age'].value()
            tenure = form['tenure'].value()
            balance = form['balance'].value()
            num_products = form['num_products'].value()
            has_card = form['has_card'].value()
            is_active_member = form['is_active_member'].value()
            estimated_salary = form['estimated_salary'].value()
            complain = form['complain'].value()
            satisfaction_score = form['satisfaction_score'].value()


            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]
            # data = [[628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']]

            inner_data = [628, 39, 1, 115341.19, 1, 1, 1, 107674.3, 1, 4, 'Germany', 'Male', 'SILVER']
            inner_data[0] = creditscore
            inner_data[1] = age
            inner_data[2] = tenure
            inner_data[3] = balance
            inner_data[4] = num_products
            inner_data[5] = has_card
            inner_data[6] = is_active_member
            inner_data[7] = estimated_salary
            inner_data[8] = complain
            inner_data[9] = satisfaction_score
            inner_data[10] = geography_choice
            inner_data[11] = gender_choice
            inner_data[12] = card_type_choice
            data = [inner_data]
            
            pred = gbc_model.predict(data)
            if pred[0] == 0:
                pred_message = 'Stay'
            else:
                pred_message = 'Exit'
            return render(request, 'predict.html', { 'form':form , 'result': pred_message, 'test': 'xfb_predict'})
    else:
        form = BankCustomerForm()
    
    return render(request, 'predict.html', { 'form':form})