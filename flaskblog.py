from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author':"Muhammad",
        "title":"Blog Post 1",
        "content":"First Blog Posted",
        "posted_date":"April 20, 2020"
    },
    {
        'author':"Abdullah",
        "title":"Blog Post 2",
        "content":"second Blog Posted",
        "posted_date":"April 25, 2020"
    }
]

@app.route('/')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == "__main":
    app.run(
        debug=True
    )