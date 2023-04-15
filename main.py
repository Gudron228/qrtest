from flask import Flask, render_template, request, redirect, url_for
from forms import QrTextForm
import qrcode
import cv2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljvndkgjns2kj4b23k4jb23k5bj235bj'

menu = [{"name": "Главная", "url": "index"},
        {"name": "Закодировать техт", "url": "qrtext"},
        {"name": "Закодировать контакт", "url": "qrcontact"}]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=menu)


@app.route('/qrtext', methods=['POST', 'GET'])
def qrtext():
    form = QrTextForm()
    if request.method == 'POST':
        if len(request.form['subject']) + len(request.form['text']) > 600:
            return redirect(url_for('index'))
        text = request.form['subject'] + "\n" + request.form['text']
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=1,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('image1.png')
        return redirect(url_for('qrtext'))

    return render_template('qrtext.html', title='Закодировать текст', menu=menu, form=form)


@app.route('/qrcontact', methods=['POST', 'GET'])
def qrcontact():


if __name__ == "__main__":
    app.run(debug=True)
