from flask import Flask, request, jsonify, render_template
import pandas as pd

df = pd.read_csv('/Users/chawadesharvari17gmail.com/Desktop/chatbot/clean_merged.csv')

app = Flask(__name__)

dbs = [
    {'title':"and", "description":"lots of lorem ipsum","link":"#"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # get the message from the user
    user_message = request.json['message']
    
    # your code to process the user message and generate a response
    bot_response = generate_bot_response(user_message)
    
    # return the bot response to the user
    return jsonify({'response': bot_response})

@app.route('/insights')
def insights():
    return render_template('insights.html',dbs = dbs)

# your function to generate a response to the user message
def generate_bot_response(user_message):
    # your code to generate the bot response
    if 'columns in data' in user_message.lower():
        col = ""
        for i in df.columns:
            col = col+i+", "
        return col
    if 'describe' in user_message.lower():
        df1 = df.describe()
        return df1.to_json()
    if 'beverages' in user_message.lower():
        a = df['food type'].value_counts()
        # print(a)
        # print(type(a))
        # print(a['beverage'])
        b = df['Veg/nonveg/alcoholic/nonalcoholic'].value_counts()
        al = int(b['a']*100/a['beverage'])
        return f"Number of beverage items are {a['beverage']}, out of them alcoholic drinks are {al}% and non-alcoholic drinks are {100-al}%"
    if 'maincourse' in user_message.lower():
        a = df['food type'].value_counts()
        b = df['Veg/nonveg/alcoholic/nonalcoholic'].value_counts()
        veg = int(b['v']*100/a['maincourse'])
        return f"Number of maincourse dishes are {a['maincourse']}, out of them veg dishes are {100-(veg-100)}% and non-veg dishes are {veg-100}%"
    if 'most ordered food' or 'most ordered dish'in user_message.lower():
        a = df['food item'].value_counts()
        # max(a)
        return f"Most ordered dish is {a[[0]]}"

    else:
        return "Please add valid question"

if __name__ == '__main__':
    app.run(debug=True,port=5001)
