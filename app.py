from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html',data=[{'description': 'Item 1'},{'description': 'Item 2'}])

if __name__ == '__main__':
  app.run()