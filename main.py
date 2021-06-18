from sanic import Sanic
from sanic.response import json

app = Sanic("Hello Pycon 2021")


@app.route('/')
async def test(request):
    name = request.args.get('iam') or 'Strange'
    name += '!'
    return json(dict(hello=name))


if __name__ == '__main__':
    app.run()
