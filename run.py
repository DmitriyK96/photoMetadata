from flask import Flask, request, render_template
from PIL import Image

app = Flask(__name__)

ALLOWED = ('png', 'jpg', 'jpeg')

def is_allowed(file):
    if file.filename.split('.',1)[1] in ALLOWED:
        return True
    else:
        return False

def is_empty(file):
    if file:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if is_empty(file) and is_allowed(file):
        im = Image.open(file)
        (width, height) = im.size
        pix = im.load()
        rgb = [0, 0, 0]
        for i in range(width):
            for j in range(height):
                rgb[0] += pix[i, j][0]
                rgb[1] += pix[i, j][1]
                rgb[2] += pix[i, j][2]
        rgb = list(map(lambda x: int(x/(width*height)), rgb))
        hex = '{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        return render_template('result.html', width=width, height=height, color=hex)
    else:
        return render_template('wrong.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)