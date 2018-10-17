from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '***** HAHAHA Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
