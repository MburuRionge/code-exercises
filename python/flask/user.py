from flask import Flask, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'mburu' #required to ise session in flask

@app.before_request
def check_user_logged_in():
    #define routes that don't require login
    public_routes = ['login', 'register']

    # if the requested route isn't public and the user is not logged in, redirect to login
    if request.endpoint not in public_routes and 'user_id' not in session:
        return redirect(url_for('login'))
    
@app.route('/login')
def login():
    return "Login Page"

@app.route('/register')
def register():
    return "Register Page"

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)