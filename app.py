# Assisted by watsonx Code Assistant 
from flask import Flask, request, jsonify
import requests
from requests.exceptions import RequestException

app = Flask(__name__)

API_KEY = 'your_openweather_api_key'

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter required'}), 400

    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(url)
        res.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = res.json()
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather)
    except RequestException as e:
        return jsonify({'error': 'Failed to retrieve data', 'details': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': 'Invalid response from API', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
