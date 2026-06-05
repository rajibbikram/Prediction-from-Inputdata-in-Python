from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        #These names MUST match your HTML input name=""
        gender = request.form.get("gender")
        race = request.form.get("race")
        parental = request.form.get("parental")
        lunch = request.form.get("lunch")
        test = request.form.get("test")

        math = float(request.form.get("math", 0))
        reading = float(request.form.get("reading", 0))
        writing = float(request.form.get("writing", 0))

        #This converts form data into ML format
        input_data = pd.DataFrame([{
            "gender": gender,
            "race/ethnicity": race,
            "parental level of education": parental,
            "lunch": lunch,
            "test preparation course": test,
            "math score": math,
            "reading score": reading,
            "writing score": writing
        }])

        #First data is encoded/scaled
        #Then model predicts result
        transformed = preprocessor.transform(input_data)
        prediction = model.predict(transformed)[0]

        #Show result on webpag
        return render_template("index.html", result=prediction)

    except Exception as e:
        return render_template("index.html", result=str(e))


if __name__ == "__main__":
    app.run(debug=True)