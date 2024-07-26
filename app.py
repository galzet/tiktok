from flask import Flask, render_template, request
import tiktok

app = Flask(__name__)

@app.route("/")
def index():
    if request.url.endswith('/'):
        return render_template('index.html')
    else:
        if request.args.get('url'):
            return tiktok.get_embed_video(request.args.get('url'))
        else:
            return render_template('index.html')

@app.route("/<path:path>")
def tiktok_page(path):
    return tiktok.get_embed_video(path)


if __name__ == '__main__':
    app.run()