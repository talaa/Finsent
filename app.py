from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route('/ai-financialnews-sentiment-analysis', methods=['POST'])
def process():
    text_input = request.form.get('stock_name')
    slider_input = request.form.get('days_input')

    # Use the values as needed
    print(f'Text Input: {text_input}')
    print(f'Slider Input: {slider_input}')

    # Perform other operations or return a response if needed

    return 'Form submitted!'

    