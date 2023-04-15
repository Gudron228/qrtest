from flask import Flask, render_template, request, redirect, url_for
from forms import QrTextForm
import qrcode
import cv2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljvndkgjns2kj4b23k4jb23k5bj235bj'


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = QrTextForm()
    if request.method == 'POST':
        text = request.form['text']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('image.png')
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
