from quart import Quart

app = Quart(__name__)

@app.route('/')
async def index():
    return 'Hello World'

@app.cli.command('run')
def run():
    app.run(port=5000, certfile='cert.pem', keyfile='key.pem')