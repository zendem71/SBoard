import pyscreenshot
import flask
from io import BytesIO
from PIL import Image, ImageDraw

app = flask.Flask(__name__)


@app.route('/screen.png')
def serve_pil_image(x, y):
    print('x: {}, y: {}'.format(x, y))
    # img_buffer = BytesIO()
    # pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    #
    # BLUE = "#0000ff"
    # RED = "#ff0000"
    # MyImage = Image.open(img_buffer)
    # MyDraw = ImageDraw.Draw(MyImage)
    #
    # # Note: Odd line widths work better for this algorithm,
    # # even though the effect might not be noticeable at larger line widths
    #
    # LineWidth = 41
    #
    # MyDraw.line([100, 100, 150, 200], width=LineWidth, fill=BLUE)
    # MyDraw.line([150, 200, 300, 100], width=LineWidth, fill=BLUE)
    # MyDraw.line([300, 100, 500, 300], width=LineWidth, fill=BLUE)
    #
    # Offset = (LineWidth - 1) / 2
    #
    # # I have plotted the connecting circles in red, to show them better
    # # Even though they look smaller than they should be, they are not.
    # # Look at the diameter of the circle and the diameter of the lines -
    # # they are the same!
    #
    # MyDraw.ellipse((150 - Offset, 200 - Offset, 150 + Offset, 200 + Offset), fill=BLUE)
    # MyDraw.ellipse((300 - Offset, 100 - Offset, 300 + Offset, 100 + Offset), fill=BLUE)
    #
    #
    # # im = Image.open(img_buffer)
    # # draw = ImageDraw.Draw(im)
    # # draw.line((100, 150, 300, 500), fill=256)
    #
    # byte_io = BytesIO()
    # MyImage.save(byte_io, 'PNG')
    #
    # byte_io.seek(0)
    # return flask.send_file(byte_io, mimetype='image/png')
    return None

@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)


@app.route('/')
def serve_img():
    return flask.render_template('screen.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True
)