'''Main file'''
from flask import render_template_string
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def index():
    '''Index method'''
    return render_template_string("GOOD")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
