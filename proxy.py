from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        if response.status_code == 200:
            return render_template('index.html', content=response.content.decode('utf-8'))
        else:
            return "Failed to fetch URL"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
