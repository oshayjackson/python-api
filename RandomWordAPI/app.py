from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/randomword', methods=['GET'])
def get_random_word():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    api_key = request.headers.get('X-Api-Key')

    if not api_key:
        return "X-Api-Key header is missing", 400

    headers = {'X-Api-Key': api_key}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        random_word = data.get('word')
        print("Random word:", random_word)
        return "Random word printed in terminal"
    else:
        return f"Error: {response.status_code}, {response.text}", response.status_code

if __name__ == '__main__':
    app.run(debug=True)
