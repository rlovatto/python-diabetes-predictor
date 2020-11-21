# Diabetes Predictor

Simple Flask application as a final challenge in the IGTI Python Developer Bootcamp. The goal was to determine among three machine learning algorithms the one with the best accuracy to predict whether a person has diabetes and show the result in a GUI.

### Tech:

  - Python
  - Flask
  - Scikit-learn: <br/>
      Algorithms: 
      - KNeighbors
      - Tree Decision
      - Multi-layer Perceptron (MLP) 
  - Google Colab (for the initial part where I chose among the three models)

### Files:
  - Machine Learning Model (Multi-layer Perceptron): prediction_model.sav  
  - Google Colab code: choosing_model.ipynb
  - Entry data: diabetes_data.csv

### Setup:
  - Open the terminal and create a folder (I used Power Shell in Windows)
  - Clone the repository
   ```  
git clone https://github.com/rlovatto/python-diabetes-predictor.git
```
  - Install virtual env and activate it
  ```
  python -m pip install --user virtualenv
  cd python-diabetes-predictor
  py -m venv diabetesenv
  .\diabetesenv\Scripts\activate
  ```
  If you are in the virtualenv your terminal should looks like this:
  ![](terminal_venv_activated.png)
  - Install dependencies
  ```  
pip install Flask
pip install numpy
pip install joblib
pip install scikit-learn
```
  - Run the project:
  ```
  python app.py
```

<br/><br/>
![](diabetes_predictor.gif)
