from app import app


@app.route('')
@app.route('/index')
def index:
	form = EnterUserName()
	return render_template('index.html', form=form)
