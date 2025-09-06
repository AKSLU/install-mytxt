from flask import Flask, Response

app = Flask(__name__)

@app.route('/download')
def download():
    with open("my.txt", "r") as f:
        content = f.read()
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000)
