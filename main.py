#!venv/bin/python3.9
from flask import (
    Flask,
    Response,
    make_response,
    request
)

# Variables declaration.
application = Flask(__name__)
get_counter = 0
post_counter = 0


@application.route(
    rule="/",
    methods=[
        "POST",
        "GET"
    ]
)
def index() -> Response:
    global get_counter
    global post_counter
    if request.method == "GET":
        get_counter += 1
        return make_response(
            f"Hmm, our GET counter is: {get_counter}",
            200
        )
    if request.method == "POST":
        post_counter += 1
        return make_response(
            f"Hmm, our POST counter is: {post_counter}",
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
