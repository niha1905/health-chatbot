from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "greetings": ["hello", "hey!", "what can I do for you?"],
    "goodbye": ["have a nice day", "goodbye"],
    "age": ["I get reborn after every compilation", "hey!", "my owners are averagely 20 years!"],
    "name": ["you can call me Medbot!", "I am Medbot!", "I am Medbot, your medical assistant"],
    "common cold symptoms": ["It seems that you are suffering from common cold"],
    "fever symptoms": ["It seems that you are suffering from fever"],
    "Diabetes symptoms": ["It seems that you are suffering from Diabetes"],
    "Depression symptoms": ["It seems that you are suffering from depression"],
    "Asthma symptoms": ["It seems that you are suffering from Asthma"],
    "common cold prevention": [
        "Medicines: Dextromethorphan, Decongestant, Diphenhydramine, Crocin Cold & Flu Max. Preventions: Wash your hands, Avoid touching your face, Clean frequently used surfaces, Use hand sanitizers."
    ],
    "fever prevention": [
        "Medicines: acetaminophen, ibuprofen, aspirin, Crocin Cold & Flu Max. Preventions: Wash your hands, Cover your mouth when you cough and your nose when you sneeze."
    ],
    "diabetes prevention": [
        "Medicines: Insulin, Amylinomimetic drug, DPP-4 inhibitor. Preventions: Cut Sugar and Refined Carbs, Work Out Regularly, Drink Water, Lose Weight."
    ],
    "depression prevention": [
        "Medicines: brexpiprazole, quetiapine, olanzapine. Preventions: Exercise regularly, Cut back on social media, Drink Water, Build strong relationships."
    ],
    "asthma prevention": [
        "Medicines: epinephrine, anticholinergic, Proair HFA. Preventions: Identify Asthma Triggers, Stay Away From Allergens, Avoid Smoke."
    ],
    "Consultation": [
        "You can consult doctors here: 1. https://www.1mg.com, 2. https://www.tatahealth.com, 3. https://www.doconline.com"
    ],
    "default": ["Sorry, I don't understand. Can you ask something else?"]
}

@app.route('/')
def index():
    return render_template('cha.html')

@app.route("/ask", methods=['POST'])
def ask():
    user_message = request.json.get('user_message', '').lower()
    response = responses.get(user_message, responses["default"])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
