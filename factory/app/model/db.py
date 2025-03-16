from app import db

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, db.Sequence('login_id_seq', increment=1), primary_key = True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    user_type = db.Column(db.Integer)

    admins = db.relationship('Admin', back_populates="login", uselist=False)
    customer = db.relationship('Customer', back_populates="login", uselist=False)

    def __init__(self, username, password, user_type, id = None):
        self.id = id
        self.username = username
        self.password = password
        self.user_type = user_type

def __repr__(self):
    return f"<Login {self.id} {self.username} {self.password} {self.user_type}>"