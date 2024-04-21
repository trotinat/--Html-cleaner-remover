from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        html_content = request.form['html_content']
        processed_content = process_html_content(html_content)
        return render_template('result.html', processed_html=processed_content)
    return render_template('index.html')

def process_html_content(html_content):
    content = html.unescape(html_content)
    soup = BeautifulSoup(content, 'html.parser')
    return str(soup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
