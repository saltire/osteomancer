from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = '}\xf6\x92\xa8a\x82\xd9\x03aXL^/a}A\xd0zt1\x9c4\x81\x15'
app.jinja_options = dict(app.jinja_options, trim_blocks=True, lstrip_blocks=True)


@app.route('/')
def homepage():
    data = {}
    return render_template('home.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
