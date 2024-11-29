from flask import Flask, render_template, request

app = Flask(__name__)

# Simple meal prediction function
def predict_meal(age, gender, height, weight, activity_level, dietary_preference, meal_type):
    # Just a simple example prediction logic
    if dietary_preference == 'omnivore':
        if meal_type == 'breakfast':
            return "Omelette with whole grain toast"
        elif meal_type == 'lunch':
            return "Grilled chicken salad"
        elif meal_type == 'dinner':
            return "Steak with steamed vegetables"
        elif meal_type == 'snack':
            return "Greek yogurt with honey"
    elif dietary_preference == 'vegetarian':
        if meal_type == 'breakfast':
            return "Avocado toast with tomatoes"
        elif meal_type == 'lunch':
            return "Quinoa salad with mixed vegetables"
        elif meal_type == 'dinner':
            return "Vegetable stir-fry with tofu"
        elif meal_type == 'snack':
            return "Fruit salad"
    elif dietary_preference == 'vegan':
        if meal_type == 'breakfast':
            return "Smoothie with spinach and banana"
        elif meal_type == 'lunch':
            return "Lentil soup with a side of bread"
        elif meal_type == 'dinner':
            return "Chickpea curry with rice"
        elif meal_type == 'snack':
            return "Carrot sticks with hummus"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    gender = request.form['gender']
    height = request.form['height']
    weight = request.form['weight']
    activity_level = request.form['activity_level']
    dietary_preference = request.form['dietary_preference']

    # Get predictions for each meal type
    breakfast = predict_meal(age, gender, height, weight, activity_level, dietary_preference, 'breakfast')
    lunch = predict_meal(age, gender, height, weight, activity_level, dietary_preference, 'lunch')
    dinner = predict_meal(age, gender, height, weight, activity_level, dietary_preference, 'dinner')
    snack = predict_meal(age, gender, height, weight, activity_level, dietary_preference, 'snack')

    return render_template('predict.html', breakfast=breakfast, lunch=lunch, dinner=dinner, snack=snack)

if __name__ == '__main__':
    app.run(debug=True)