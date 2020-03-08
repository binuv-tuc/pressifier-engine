from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule(rule='/', view_func=views.index)
app.add_url_rule(rule='/api/articles', view_func=views.get_articles, methods=['POST'])
app.add_url_rule(rule='/api/articles/classify', view_func=views.classify_articles, methods=['POST'])
app.add_url_rule(rule='/api/articles/rate', view_func=views.rate_articles, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
