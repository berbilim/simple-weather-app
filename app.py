from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_openweather_api_key'

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter required'}), 400
    url = f'<http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric>'
    res = requests.get(url)
    if res.status_code != 200:
        return jsonify({'error': 'Failed to retrieve data'}), res.status_code
    data = res.json()
    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
