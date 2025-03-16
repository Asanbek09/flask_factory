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
    
class Customer(db.Model):
    __tablename__ = 'customer'
    id = id.Column(db.Integer, db.ForeignKey('login.id'), primary_key = True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    middlename = db.Column(db.String(45))
    email = db.Column(db.String(45))
    mobile = db.Column(db.String(20))
    address = db.Column(db.String(100))
    status = db.Column(db.String(45))

    login = db.relationship('Login', back_populates="customer")
    orders = db.relationship('Orders', back_populates="customer")
    shippings = db.relationship('Shipping', back_populates="customer")

    def __init__(self, id, firstname, lastname, middlename, email, mobile, address, status):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.email = email
        self.mobile = mobile
        self.address = address
        self.status = status

    def __repr__(self):
        return f"<Customer {self.id} {self.firstname} {self.lastname} {self.middlename}>"