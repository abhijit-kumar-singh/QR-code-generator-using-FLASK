from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/', methods=['get','POST'])
def index():
  if request.method == 'POST':
    text = request.form['text']
    qrcode.make(text).save('qrcode.png')
    return send_file('qrcode.png', mimetype='images/png')
  return render_template('index.html')

if __name__ == "__main__":
      app.run(debug=True, host="0.0.0.0", port=80)