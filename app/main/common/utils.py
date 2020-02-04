from flask import jsonify


def generate_success_response(records=None):
    response = json_return()
    response.setSuccess(True)
    if records:
        response.addRecords(records)

    return jsonify(response.__dict__)


def generate_failure_response(message=None):
    response = json_return()
    response.setSuccess(False)
    if message:
        if isinstance(message, list):
            for m in message:
                response.addMessage(m)
        else:
            response.addMessage(message)

    return jsonify(response)


class json_return(object):
    def __init__(self):
        self.success = False
        self.records = []
        self.total = 0
        self.message = []

    def setSuccess(self, value):
        """setSuccess"""
        self.success = value

    def addRecords(self, recs):
        """addRecords to array of records, update total"""
        self.records += recs
        self.total = len(self.records)

    def addMessage(self, mess):
        """addMessage to array of messages"""
        self.message.append(mess)
