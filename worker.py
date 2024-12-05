from et import extract_tags

from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)


class ExtractTags(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("text", type=str, required=True, help="text is required")
        super(ExtractTags, self).__init__()

    def post(self):
        args = self.parser.parse_args()
        text = args["text"]
        keyword = extract_tags(text)
        return {"keyword": keyword}


api.add_resource(ExtractTags, "/v1/api/extract_tags")

# curl 测试
# curl -X POST -H "Content-Type: application/json" \
# -d '{"text":"温暖的氛围中总是带着一丝紧张   #机车女孩#一加ace2pro"}' http://127.0.0.1:5000/v1/api/extract_tags

if __name__ == "__main__":
    app.run(debug=False)
