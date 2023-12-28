"""
connectify application launcher. Opens in default browser.
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config["STATIC_FOLDER"] = 'static'  # set location of static folder

@app.route('/')
def index() -> str:
    """
    Log in/sign up page.
    """
    return render_template('begin.html')

@app.route('/profile/<username>')
def user_profile(username: str) -> str:
    """
    Profile of specified username.
    """
    # fetch user info
    user_data = None

    return render_template('profile.html', data=user_data)


if __name__ == '__main__':
    app.run(debug=True)