from flask import Blueprint

quiz_bp = Blueprint("quiz", __name__, url_prefix="/quiz", template_folder="templates")

from . import routes