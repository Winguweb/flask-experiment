from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works'

@app.route('/hello')
def hello():
  return 'this is the hello endpoint'

@app.route('/user/<username>')
def show_user(username):
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return str(post_id)

