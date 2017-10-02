
import requests as http
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/apply', methods=['GET', 'POST'])
def apply_page():
    if request.method == 'POST':
        apply_form = request.form
        http.post('http://lab.hi-arc.net/api/apply/new', data=apply_form)
        
    return render_template('apply.html')

if __name__ == '__main__':
    app.run()
