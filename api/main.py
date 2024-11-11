from flask import Blueprint
from api.businfo.main import businfo_bp

main_bp = Blueprint('main', __name__, url_prefix='/api')
main_bp.register_blueprint(businfo_bp)

@main_bp.route('/', methods=['GET'])
def home():
    return "/api"