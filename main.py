#!venv/bin/python3.9
from flask import (
    Flask,
    Response,
    make_response,
    request
)

# Variables declaration.
application = Flask(__name__)
counter = 0


@application.route(
    rule="/",
    methods=[
        "POST",
        "GET"
    ]
)
def index() -> Response:
    global counter
    if request.method == "POST":
        counter += 1
        return make_response(
            "Hmm, Plus 1 please ",
            200
        )
    else:
        return make_response(
            str(f"Our counter is: {counter} "),
            200
        )


@application.route(
    rule="/health",
    methods=[
        "GET"
    ]
)
def health() -> Response:
    return make_response(
        "",
        200
    )


if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
