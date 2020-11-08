from flask import Flask
from routes.Users import userBlueprint
from routes.Posts import postBlueprint

flaskApp = Flask(__name__)
flaskApp.register_blueprint(userBlueprint)
flaskApp.register_blueprint(postBlueprint)

comments = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flaskApp.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
