from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '759b7e7cc0dde1eaa7271006d27afad3'  # replace with your OpenWeatherMap API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = {'error': 'City not found!'}
    return render_template('index.html', weather=weather)
    
if __name__ == '__main__':
    app.run(debug=True)
