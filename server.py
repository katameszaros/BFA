from flask import Flask, render_template
from cinema import Cinema

app = Flask('3rd_assessment')


cinema1 = Cinema("Budapest", 200)
cinema2 = Cinema("Szeged", 350)
cinema3 = Cinema("Győr", 100)



@app.route("/")
def index():
    return render_template('index.html', cinemas = Cinema.cinemas)

@app.route("/<cinema_id>")
def show_cinema_website(cinema_id):
    seats = Cinema.get_cinema_by_id(int(cinema_id)).seats
    print(seats)
    return str(seats)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9999)
