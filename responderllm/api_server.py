# Setup endpoint that can be used to update the prompt
from threading import Thread
from flask import Flask, request
from uuid import uuid4
from dataclasses import dataclass
from time import time, sleep
import logging


@dataclass
class APIMessage:
    type: str
    data: str
    id: int


class FlaskServer:
    """A Flask server implementation for handling API requests.

    Attributes:
        cmd_q: Queue for command processing
        resp_d: Dictionary for storing responses
        port: Port number for the server
    """
    def __init__(self, cmd_q, resp_d, port=5432):
        """Initialize the Flask server.

        Args:
            cmd_q: Queue for command processing
            resp_d: Dictionary for storing responses
            port: Port number for the server (default: 5432)
        """
        self.flask_thread = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        self.cmd_q = cmd_q
        self.resp_d = resp_d

        self.app = Flask(__name__)

        self.app.add_url_rule("/query", "query", self.query)
        self.port = port

    def get_command_response(self, uuid_str, timeout=10):
        start_time = time()

        # wait for response or timeout
        while True:
            if time() - start_time >= timeout:
                return None

            if uuid_str in self.resp_d:
                return self.resp_d.pop(uuid_str)
            else:
                sleep(0.1)

    def query(self):
        print(request.args)
        query_type = "alert" if request.args.get("alert", False) == "True" else "query"
        print(query_type)
        queue_message = APIMessage(
            type=query_type,
            data=request.args.get("query", "Describe the scene."),
            id=int(uuid4()),
        )
        self.cmd_q.put(queue_message)
        response = self.get_command_response(queue_message.id)
        if response:
            return response
        else:
            return "Server timed out processing the request"

    def _start_flask(self):
        self.app.run(use_reloader=False, host="0.0.0.0", port=self.port)

    def start_flask(self):
        self.flask_thread = Thread(target=self._start_flask, daemon=True)
        self.flask_thread.start()
