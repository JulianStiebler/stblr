from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Test User 1',
        'title': 'Test Title 1',
        'content': 'Test Content 1',
        'date_posted': 'Test Date 1',
    },
    {
        'author': 'Test User 2',
        'title': 'Test Title 2',
        'content': 'Test Content 2',
        'date_posted': 'Test Date 2',
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About", posts=posts)



if __name__ == '__main__':
    app.run(debug=True)