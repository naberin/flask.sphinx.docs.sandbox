from flask import jsonify


class HealthController:

    @staticmethod
    def getHealth():
        return jsonify(status="OK"), 200
