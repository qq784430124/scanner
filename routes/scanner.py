# coding=utf-8
from flask import (
    Blueprint,
    render_template,
)


scan = Blueprint('scan', __name__)


@scan.route('/')
def index():
    return render_template('scan.html', )

