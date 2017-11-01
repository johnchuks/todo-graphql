from .api.schema import schema
from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.route('/', methods=['GET'])
def hello():
    return "I am here for real"


if __name__ == '__main__':
    app.run()

