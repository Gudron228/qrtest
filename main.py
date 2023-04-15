import qrcode
from flask import Flask, render_template, request, redirect, url_for

from forms import QrTextForm, ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljvndkgjns2kj4b23k4jb23k5bj235bj'

menu = [{"name": "Главная", "url": "index"},
        {"name": "Закодировать техт", "url": "qr_text"},
        {"name": "Закодировать контакт", "url": "qr_contact"}]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=menu)


@app.route('/qr_text', methods=['POST', 'GET'])
def qr_text():
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
        return redirect(url_for('qr_text'))

    return render_template('qr_text.html', title='Закодировать текст', menu=menu, form=form)


@app.route('/qr_contact', methods=['POST', 'GET'])
def qr_contact():
    form = ContactForm()
    if request.method == 'POST':
        if len(request.form['first_name']) + len(request.form['last_name']) + len(request.form['phone']) > 600:
            return redirect(url_for('index'))
        text = request.form['first_name'] + "\n" + request.form['last_name'] + "\n" + request.form['phone']
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=1,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('image2.png')
        return redirect(url_for('qr_contact'))

    return render_template('qr_contact.html', title='Закодировать контакт', menu=menu, form=form)


if __name__ == "__main__":
    app.run(debug=True)
