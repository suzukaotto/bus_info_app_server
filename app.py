import json
from flask import Flask
from api.main import main_bp
import utils

# load setting
with open('./config.json', 'r') as f:
    CONFIG = json.load(f)

# create app
app = Flask(__name__)
app.register_blueprint(main_bp)

# 404 error handling
@app.errorhandler(404)
def page_not_found(e):
    return utils.get_response(15), 404

# start app
if __name__ == '__main__':
    app.run(CONFIG['HOST'], CONFIG['PORT'], debug=True)