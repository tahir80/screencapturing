from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def screen_capture():
    return render_template('screensharing-test.html')



if __name__ == '__main__':
    app.run(debug=True)

