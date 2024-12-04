from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify

from werkzeug.utils import redirect

from pybo import db
from pybo.models import User

bp = Blueprint('my', __name__, url_prefix='/mypagE')


@bp.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    new_status = data.get('status', '').strip()  # 새 상태 메시지

    if not new_status:  # 상태 메시지가 비어 있으면 기본값 설정
        new_status = None

    # 사용자를 식별하기 위해 username을 사용 (로그인 시스템에서 대체 가능)
    username = "test_user"  # 예제 사용자 이름 (로그인 시스템으로 대체)
    user = User.query.filter_by(username=username).first()

    if user:
        user.status_message = new_status  # 상태 메시지 업데이트
        db.session.commit()  # 변경사항 저장
        return jsonify({"success": True, "message": "Status updated successfully"})
    else:
        return jsonify({"success": False, "message": "User not found"}), 404

