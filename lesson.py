from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    param = {
        'title': 'Колонизация Марса'
    }
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
