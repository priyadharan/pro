from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def land():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    return f' {username} WELCOME TO PROJECT MANAGEMENT'
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    return f'{username} Succesfully Registered!'




if __name__ == '__main__':
    app.run(debug=True)