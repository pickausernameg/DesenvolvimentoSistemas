from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChaveSecreta'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LczhpcUAAAAAMgiNQ7wP24hoS9CfyizglW2vRq3'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LczhpcUAAAAAGoRRJRS5U_HxIGerPJV3DbvQGDB'

class LoginForm(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')
	recaptcha = RecaptchaField()

@app.route('/form', methods=['GET', 'POST'])
def form():
	form = LoginForm()

	if form.validate_on_submit():
		return 'Formulário enviado'
	return render_template('form.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)