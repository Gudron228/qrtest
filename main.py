import qrcode
from flask import Flask, render_template, request, redirect, url_for

from forms import QrTextForm, ContactForm, ServiceForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljvndkgjns2kj4b23k4jb23k5bj235bj'
# меню для удобного перемещения по страницам
menu = [{"name": "Главная", "url": "index"},
        {"name": "Закодировать текст", "url": "qr_text"},
        {"name": "Закодировать контакт", "url": "qr_contact"},
        {"name": "Закодировать услугу", "url": "qr_service"}]


@app.route('/')
@app.route('/index')
# главная страница
def index():
    return render_template('index.html', menu=menu)


@app.route('/qr_text', methods=['POST', 'GET'])
# страница текстовым qr-кодом
def qr_text():
    form = QrTextForm()
    if request.method == 'POST':
        #проверка на колво символов
        if len(request.form['subject']) > 40 or len(request.form['text']) > 600:
            return redirect(url_for('index'))
        text = request.form['subject'] + "\n" + request.form['text']
        #генерация qr-кода
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        #сохранение изображения (пока что в директории проекта)
        img.save('image1.png')
        return redirect(url_for('qr_text'))

    return render_template('qr_text.html', menu=menu, form=form)


@app.route('/qr_contact', methods=['POST', 'GET'])
# страница с qr-кодом vCard
def qr_contact():
    form = ContactForm()
    if request.method == 'POST':
        # проверка на колво символов
        if len(request.form['first_name']) > 32 or len(request.form['last_name']) > 32 or \
                len(request.form['phone']) > 11 or len(request.form['org']) > 32 or \
                len(request.form['url']) > 64 or len(request.form['email']) > 32:
            return redirect(url_for('index'))
        #vCard для добавления в контакты
        s = f'''BEGIN:VCARD
VERSION:3.0
FN:{request.form['first_name']} {request.form['last_name']}
N:{request.form['first_name']};{request.form['last_name']}
EMAIL:{request.form['email']}
TEL;TYPE=WORK,VOICE:{request.form['phone']}
ORG:{request.form['org']}
URL:{request.form['url']}
END:VCARD'''
        # генерация qr-кода
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=1,
        )
        qr.add_data(s)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        # сохранение изображения (пока что в директории проекта)
        img.save('image2.png')
        return redirect(url_for('qr_contact'))

    return render_template('qr_contact.html', menu=menu, form=form)


@app.route('/qr_service', methods=['POST', 'GET'])
#страница с меню услуг
def qr_service():
    form = ServiceForm()
    if request.method == 'POST':
        # проверка на колво символов
        if (len(request.form['service']) > 32 or len(request.form['food']) > 32 or len(request.form['food']) > 11) and \
                request.form['price'] < 0:
            return redirect(url_for('index'))

        service = f'''Меню услуг\n {request.form['service']} "{request.form['food']}" {request.form['price']}р'''

        # генерация qr-кода
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=1,
        )
        qr.add_data(service)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        # сохранение изображения (пока что в директории проекта)
        img.save('image3.png')
        return redirect(url_for('qr_service'))

    return render_template('qr_service.html', menu=menu, form=form)


if __name__ == "__main__":
    app.run(debug=True)
