from app import app
from app import db
from app.models import User, Post


@app.shell_context_processor
def process_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
