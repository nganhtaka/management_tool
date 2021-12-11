import os

from flask import Flask
from flask_cors import CORS

# Initialize Flask app
from elements.authentication import simple_auth
from elements.criticalities import simple_criticality
from elements.dailies import simple_daily
from elements.levels import simple_level
from elements.tasks import simple_task
from elements.users import simple_user

app = Flask(__name__)
# deactivate CORS
CORS(app)

app.register_blueprint(simple_daily, url_prefix='/daily')
app.register_blueprint(simple_task, url_prefix='/task')
app.register_blueprint(simple_user, url_prefix='/user')
app.register_blueprint(simple_criticality, url_prefix='/criticality')
app.register_blueprint(simple_level, url_prefix='/level')
app.register_blueprint(simple_auth, url_prefix='/auth')

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
