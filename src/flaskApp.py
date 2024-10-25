from flask import Flask, request, render_template
from sports_injury_info import get_injury_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""
    if request.method == 'POST':
        injury_name = request.form['injury_name']
        result = get_injury_info(injury_name)
        if isinstance(result, dict):
            result_text = (
                f"Description: {result['Description']}<br>"
                f"Common Sports: {', '.join(result['Common Sports'])}<br>"
                f"Treatment: {result['Treatment']}<br>"
                f"Recovery Exercises: {', '.join(result['Recovery Exercises'])}"
            )
        else:
            result_text = result

    return render_template('index.html', result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
