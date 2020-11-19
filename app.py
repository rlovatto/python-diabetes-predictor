from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

def diabetes_prediction(form_values):
    input_data = form_values.reshape(1, 8)
    model_mlp = joblib.load("prediction_model.sav")
    output = model_mlp.predict(input_data)
    return output[0]

def initial_values():
    return {'gest': '3', 'glic': '148', 'diastolic_pre': '72', 'tri_st': '35', 'insu': '230', 'bmi': '28.7', 'ge_inh': '0.201', 'age': '43'}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        form_dict = initial_values()
        data = {"message": "", "css_class": "", "form": form_dict}
    else:
        form_dict = request.form.to_dict() #{'gest': '1', 'glic': '2', 'diastolic_pre': '3', 'tri_st': '4', 'insu': '5', 'bmi': '6', 'ge_inh': '7', 'age': '8'}  dict
        form_list = list(form_dict.values())   # ['1', '2', '3', '4', '5', '6', '7', '8'] list
        form_list = np.array(form_list, dtype='float64')

        result = diabetes_prediction(form_list)

        if int(result) == 1:
            data = {"message": "Sorry, you have diabetes", "css_class": "bad_result", "form": form_dict}
        else:
            data = {"message": "You don't have diabetes", "css_class": "good_result", "form": form_dict}

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)