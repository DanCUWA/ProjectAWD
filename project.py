from app import app,db,socketio
from app.models import User, Settings, GameRoom, Message

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Settings':Settings, 'GameRoom': GameRoom, 'Message':Message}

if __name__ == '__main__':
    socketio.run(app)

