import requests

# Specify the URL of your Flask app
url = "http://localhost:5000"

# Sample data for the input fields
data = {
    "donor_age": 35,
    "donor_gender": 1,
    "donor_bmi": 28.9,
    "donor_cause_of_death": 0,
    "donor_diabetes": 0,
    "donor_hypertension": 1,
    "donor_alcohol_abuse": 0,
    "donor_smoking": 1,
    "donor_lymphocyte": 0,
    "donor_hepatitis_b": 0,
    "donor_hepatitis_c": 0,
    "recipient_etiology": 1,
    "recipient_meld_score": 20,
    "recipient_age": 50,
    "recipient_gender": 0,
    "recipient_bmi": 25.5,
    "recipient_diabetes": 1,
    "recipient_hypertension": 0,
    "recipient_alcohol_abuse": 0,
    "recipient_smoking": 0,
    "recipient_lymphocyte": 0.8,
    "recipient_hepatitis_b": 0,
    "recipient_hepatitis_c": 1,
    "recipient_albumin_level": 40,
    "recipient_alcoholic_cirrhosis": 5.0,
    "recipient_primary_biliary_cirrhosis": 0.9,
    "recipient_na": 140,
    "recipient_mg": 2.0,
    "recipient_wbc": 7000,
    "recipient_platelets": 250000,
    "recipient_cold_ischemia_time": 8.0,
    "recipient_warm_ischemia_time": 2.5,
    "recipient_blood_transfusion": 1.0,
    "recipient_immunosuppressant_medication": 2,
    "recipient_rejection_episodes": 1
}

# Send a POST request to your Flask app
response = requests.post(url, data=data)

# Print the response from the Flask app
print(response.text)
