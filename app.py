from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Event Registration</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #667eea, #764ba2);
                text-align: center;
                color: white;
                margin-top: 80px;
            }
            .box {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
            }
            input {
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
                border: none;
                width: 200px;
            }
            button {
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                background: white;
                color: #333;
                font-weight: bold;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <div class="box">
            <h2>Event Registration</h2>
            <form method="POST" action="/submit">
                <input type="text" name="name" placeholder="Enter Name"><br>
                <input type="email" name="email" placeholder="Enter Email"><br>
                <button type="submit">Register</button>
            </form>
        </div>

    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return "<h3>❌ Registration Failed: All fields required</h3>"

    return f"<h3>✅ Registration Successful for {name}</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)