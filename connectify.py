"""
connectify application launcher. Opens in default browser.
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config["STATIC_FOLDER"] = 'static'  # set location of static folder

@app.route('/')
def index():
    return render_template('begin.html')

if __name__ == '__main__':
    app.run(debug=True)