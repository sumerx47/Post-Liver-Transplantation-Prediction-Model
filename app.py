import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

pickle_in = open("model.pkl", "rb")
best_model = pickle.load(pickle_in)

def liver_prediction(donor_age, donor_gender, donor_bmi, donor_cause_of_death, donor_diabetes, donor_hypertension, donor_alcohol_abuse, donor_smoking, donor_lymphocyte, donor_hepatitis_b, donor_hepatitis_c, recipient_etiology, recipient_meld_score, recipient_age, recipient_gender, recipient_bmi, recipient_diabetes, recipient_hypertension, recipient_alcohol_abuse, recipient_smoking, recipient_lymphocyte, recipient_hepatitis_b, recipient_hepatitis_c, recipient_albumin_level, recipient_alcoholic_cirrhosis, recipient_primary_biliary_cirrhosis, recipient_na, recipient_mg, recipient_wbc, recipient_platelets, recipient_cold_ischemia_time, recipient_warm_ischemia_time, recipient_blood_transfusion, recipient_immunosuppressant_medication, recipient_rejection_episodes):

    prediction = best_model.predict([[donor_age, donor_gender, donor_bmi, donor_cause_of_death, donor_diabetes, donor_hypertension, donor_alcohol_abuse, donor_smoking, donor_lymphocyte, donor_hepatitis_b, donor_hepatitis_c, recipient_etiology, recipient_meld_score, recipient_age, recipient_gender, recipient_bmi, recipient_diabetes, recipient_hypertension, recipient_alcohol_abuse, recipient_smoking, recipient_lymphocyte, recipient_hepatitis_b, recipient_hepatitis_c, recipient_albumin_level, recipient_alcoholic_cirrhosis, recipient_primary_biliary_cirrhosis, recipient_na, recipient_mg, recipient_wbc, recipient_platelets, recipient_cold_ischemia_time, recipient_warm_ischemia_time, recipient_blood_transfusion, recipient_immunosuppressant_medication, recipient_rejection_episodes]])
    return prediction

@app.route("/", methods=["GET", "POST"])
def main():
    complication = ""
    if request.method == "POST":
        donor_age = int(request.form["donor_age"])
        donor_gender_male = int(request.form["donor_gender_male"])
        donor_gender_female = int(request.form["donor_gender_female"])
        donor_bmi = float(request.form["donor_bmi"])
        donor_cause_of_death = int(request.form["donor_cause_of_death"])
        donor_diabetes = int(request.form["donor_diabetes"])
        donor_hypertension = int(request.form["donor_hypertension"])
        donor_alcohol_abuse = int(request.form["donor_alcohol_abuse"])
        donor_smoking = int(request.form["donor_smoking"])
        donor_lymphocyte = int(request.form["donor_lymphocyte"])
        donor_hepatitis_b = int(request.form["donor_hepatitis_b"])
        donor_hepatitis_c = int(request.form["donor_hepatitis_c"])
        recipient_etiology = int(request.form["recipient_etiology"])
        recipient_meld_score = float(request.form["recipient_meld_score"])
        recipient_age = int(request.form["recipient_age"])
        recipient_gender = int(request.form["recipient_gender"])
        recipient_bmi = float(request.form["recipient_bmi"])
        recipient_diabetes = int(request.form["recipient_diabetes"])
        recipient_hypertension = int(request.form["recipient_hypertension"])
        recipient_alcohol_abuse = int(request.form["recipient_alcohol_abuse"])
        recipient_smoking = int(request.form["recipient_smoking"])
        recipient_lymphocyte = float(request.form["recipient_lymphocyte"])
        recipient_hepatitis_b = int(request.form["recipient_hepatitis_b"])
        recipient_hepatitis_c = int(request.form["recipient_hepatitis_c"])
        recipient_albumin_level = float(request.form["recipient_albumin_level"])
        recipient_alcoholic_cirrhosis = float(request.form["recipient_alcoholic_cirrhosis"])
        recipient_primary_biliary_cirrhosis = float(request.form["recipient_primary_biliary_cirrhosis"])
        recipient_na = float(request.form["recipient_na"])
        recipient_mg = float(request.form["recipient_mg"])
        recipient_wbc = int(request.form["recipient_wbc"])
        recipient_platelets = int(request.form["recipient_platelets"])
        recipient_cold_ischemia_time = float(request.form["recipient_cold_ischemia_time"])
        recipient_warm_ischemia_time = float(request.form["recipient_warm_ischemia_time"])
        recipient_blood_transfusion = float(request.form["recipient_blood_transfusion"])
        recipient_immunosuppressant_medication = int(request.form["recipient_immunosuppressant_medication"])
        recipient_rejection_episodes = int(request.form["recipient_rejection_episodes"])

        complication_index = liver_prediction(donor_age,donor_gender_male, donor_gender_female, donor_bmi, donor_cause_of_death, donor_diabetes, donor_hypertension, donor_alcohol_abuse, donor_smoking, donor_lymphocyte, donor_hepatitis_b, donor_hepatitis_c, recipient_etiology, recipient_meld_score, recipient_age, recipient_gender, recipient_bmi, recipient_diabetes, recipient_hypertension, recipient_alcohol_abuse, recipient_smoking, recipient_lymphocyte, recipient_hepatitis_b, recipient_hepatitis_c, recipient_albumin_level, recipient_alcoholic_cirrhosis, recipient_primary_biliary_cirrhosis, recipient_na, recipient_mg, recipient_wbc, recipient_platelets, recipient_cold_ischemia_time, recipient_warm_ischemia_time, recipient_blood_transfusion, recipient_immunosuppressant_medication, recipient_rejection_episodes)

        if complication_index.size > 0:
                # ...
            if complication_index[0] == 0:
                complication = '" Artery Thrombosis "'
            elif complication_index[0] == 1:
                complication = '" Biliary Complications "'
            elif complication_index[0] == 2:
                complication = '" Cardiovascular Complications "'
            elif complication_index[0] == 3:
                complication = '" Infection "'
            elif complication_index[0] == 4:
                complication = '" Metabolic Complications "'
            elif complication_index[0] == 5:
                complication = '" No Complication "'
            elif complication_index[0] == 6:
                complication = '" Portal Vein Thrombosis "'
            elif complication_index[0] == 7:
                complication = '" Post-transplant Diabetes "'
            elif complication_index[0] == 8:
                complication = '" Primary Graft Non-function "'
            elif complication_index[0] == 9:
                complication = '" Rejection "'
            elif complication_index[0] == 10:
                complication = '" Renal Dysfunction "'
            else:
                complication = 'Invalid prediction'


    return render_template("index.html", complication=complication)

if __name__ == "__main__":
    app.run(debug=True)
