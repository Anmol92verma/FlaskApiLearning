from flask import Flask

from database import mysql
from routes.Users import userBlueprint
from routes.Posts import postBlueprint

flaskApp = Flask(__name__)
flaskApp.register_blueprint(userBlueprint)
flaskApp.register_blueprint(postBlueprint)


flaskApp.config['MYSQL_DATABASE_USER'] = "root"
flaskApp.config['MYSQL_DATABASE_PASSWORD'] = "helloworld"
flaskApp.config["MYSQL_DATABASE_DB"] = "db_fake"

mysql.init_app(flaskApp)

comments = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flaskApp.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
