from flask import Flask, request, jsonify, render_template
import pandas as pd

df = pd.read_csv('/Users/chawadesharvari17gmail.com/Desktop/datahack website/clean_merged.csv')

app = Flask(__name__)

powerbidata = [
    {"title":"Overall sales of products over the years and by price", "description":"The visualization on the home page shows which product has highest amount of sales, for eg: beverage is the highest moneymaker followed by maincourse then starters and so on. Another line graph is shown wherein eranings of restaurant over years is demonstrated." , "link":"https://app.powerbi.com/view?r=eyJrIjoiZDRhYzE5M2YtNDU5NS00YWRlLThiYTQtYWNmMzAxNjFlNjZlIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D"}
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
    return render_template('insights.html',database = powerbidata)

# your function to generate a response to the user message
def generate_bot_response(user_message):

    # your code to generate the bot response
    if 'columns in data' in user_message.lower():
        col = ""
        for i in df.columns:
            col = col+i+", "
        return "All the columns in data are " + col

    elif 'describe' in user_message.lower():
        df1 = df.describe()
        return df1.to_json()

    elif 'beverages' in user_message.lower():
        a = df['food type'].value_counts()
        b = df['Veg/nonveg/alcoholic/nonalcoholic'].value_counts()
        al = int(b['a']*100/a['beverage'])
        return f"Number of beverage items are {a['beverage']}, out of them alcoholic drinks are {al}% and non-alcoholic drinks are {100-al}%"
    
    elif 'maincourse' in user_message.lower():
        a = df['food type'].value_counts()
        b = df['Veg/nonveg/alcoholic/nonalcoholic'].value_counts()
        veg = int(b['v']*100/a['maincourse'])
        return f"Number of maincourse dishes are {a['maincourse']}, out of them veg dishes are {100-(veg-100)}% and non-veg dishes are {veg-100}%"
    
    elif 'most ordered' in user_message.lower():
        a = df['food item'].value_counts()
        d = a[[0]].to_string().split("   ")
        return f"Most ordered dish is {d[0]}"
    
    elif 'least ordered' in user_message.lower():
        a = df['food item'].value_counts()
        d = a[[-1]].to_string().split("   ")
        return f"Least ordered dish is {d[0]}"
    
    else:
        return "Please add valid question"

if __name__ == '__main__':
    app.run(debug=True,port=5001)
