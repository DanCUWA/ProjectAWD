from app import app,db,socketio
from app.models import User, Stats, Settings, GameRoom

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Stats': Stats, 'Settings':Settings, 'GameRoom': GameRoom}

if __name__ == '__main__':
    socketio.run(app)

