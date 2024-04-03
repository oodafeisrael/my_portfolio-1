from flask import Blueprint

auth = Blueprint('auth', __name__)

#@auth.route('/form_view')
#def form_view():
   # return render_template('public/forms/form_view.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('public/forms/login.html')

@auth.route('/logout')
def logout():
    return "<p>bye</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template('public/forms/sign_up.html')