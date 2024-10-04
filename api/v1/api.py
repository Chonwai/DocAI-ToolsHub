# v1/api.py
from flask import Blueprint
from api.v1.arxiv_api import arxiv_bp
from api.v1.qr_api import qr_bp  # 新增此行

api_bp = Blueprint("api_bp", __name__)

api_bp.register_blueprint(arxiv_bp, url_prefix="/arxiv")
api_bp.register_blueprint(qr_bp, url_prefix="/qrcode")  # 新增此行
