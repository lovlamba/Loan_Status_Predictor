from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Create your views here.
def index(request) :
    if request.GET :
        dict = request.GET
        data = list(dict.values())
        try:
            test = [np.array(data, dtype='float64')]

            df = pd.read_csv('predictor/loan.csv')
            x=df[['Married','Education','ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']].values
            y=df['Loan_Status'].values

            model = LogisticRegression()
            model.fit(x, y)
            LogisticRegression()

            prediction = model.predict(test)
            approval = int(prediction[0])

            if approval == 0 :
                text = 'Sorry!! But your loan will not be approved'
            elif approval == 1 :
                text = 'Congrats!! your loan will be approved'

            context = {
                'variable':text
            }
            return render(request, 'index.html', context)
        except:
            context = {
                'variable':"Please fill all entries"
            }
            return render(request, 'index.html', context)
    else :
        return render(request, 'index.html')

