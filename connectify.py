"""
connectify application launcher. Opens in default browser.
"""

from flask import Flask, render_template, request

app = Flask(__name__)
app.config["STATIC_FOLDER"] = 'static'  # set location of static folder

@app.route('/')
def index() -> str:
    """
    Log in/sign up page.
    """
    return render_template('sign_up.html')

@app.route('/profile.html/<username>')
def user_profile(username: str) -> str:
    """
    Profile of specified username.
    """
    # fetch user info
    user_data = None

    return render_template('profile.html', data=user_data)

@app.route('/login')
def login() -> str:
    """
    Log in page
    """
    return render_template('login.html')

@app.route('/attempt_create_account', methods=["post"])
def create_account() -> str:
    """
    Create the account with emaio, username, and password from sign_up.html

    Precondition: username is not taken by an existing account
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    print(f"username: {username}\npassword: {password}\nemail: {email}")
    #return render_template(f'profile.html/{username}')
    return "Profile page not implemented yet."

if __name__ == '__main__':
    app.run(debug=True)