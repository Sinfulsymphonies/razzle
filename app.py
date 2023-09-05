from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/request-form', methods=['POST'])
def request_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        request_text = request.form['request']

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'request': request_text
        }

        with open('requests.json', 'a') as f:
            json.dump(data, f)
            f.write("\n")

        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
