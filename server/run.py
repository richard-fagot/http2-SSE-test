#! /usr/bin/env python
from dsapp import app

if __name__ == "__main__":
    app.debug=True
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Mandatory for the SSE (Server Sent Event) to allow Flask 
    # not to block connection in development server : 
    # https://stackoverflow.com/questions/12232304/how-to-implement-server-push-in-flask-framework
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    app.run(threaded=True)