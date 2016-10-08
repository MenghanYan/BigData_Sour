
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index_():
    return render_template('index.html')

@app.route('/documentary.html')
def documentary():
    return render_template('documentary.html')

@app.route('/article.html')
def article():
    return render_template('article.html')

@app.route('/article-single.html')
def aiticle_single():
    return render_template('article-single.html')

if __name__ == '__main__':
    app.run()
