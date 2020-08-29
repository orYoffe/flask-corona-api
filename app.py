from flask import Flask
app = Flask(__name__)

a = 'a'

print(type(a) == <class 'str'>)

@app.route('/')
def index():
    return 'Index Page'
# TODO add overall stats
# TODO add country stats
# TODO add search sountry
@app.route('/hello')
def hello():
    return 'Hello, World'