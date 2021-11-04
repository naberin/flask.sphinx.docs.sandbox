import os
from flask import Flask
from config.constants import Constants
from controllers.healthController import HealthController

app = Flask(__name__)


@app.route('/api/health')
def health():
    return HealthController.getHealth()


if __name__ == '__main__':
    app.run(host=os.getenv("HOST", "0.0.0.0"),
            port=Constants.PORT)
