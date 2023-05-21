from app import create_app,db,socketio
from app.models import User, Settings, GameRoom, Message



if __name__ == '__main__':
    app = create_app()
    socketio.run(app)
    
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Settings':Settings, 'GameRoom': GameRoom, 'Message':Message}

