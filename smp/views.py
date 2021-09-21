from django.shortcuts import render
import numpy as np
import joblib


model = joblib.load("student_marks_predictor"+".pkl")


# Create your views here.

def home(request):
    predicted_mark = 0
    study_hour = 0
    if request.method == 'POST':
        study_hour = request.POST['s_hour']
        val = np.array([study_hour])
        predicted_mark = model.predict([val])[0][0].round(2)
    return render(request,'home.html',{'predicted_mark':predicted_mark,'studyhour':study_hour})