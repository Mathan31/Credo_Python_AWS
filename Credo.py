from flask import Flask

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return "<h1>WelCome to Credo World, Deploying in AWS EB!!!</h1>"

if __name__ == '__main__':
    app.run()
