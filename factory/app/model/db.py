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
    
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key = True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    middlename = db.Column(db.String(45))
    email = db.Column(db.String(45))
    mobile = db.Column(db.String(45))

    login = db.relationship('Login', back_populates = "admins")

    def __init__(self, id, firstname, lastname, middlename, email, mobile):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.email = email
        self.mobile = mobile

    def __repr__(self):
        return f"<Admin {self.id} {self.firstname} {self.middlename} {self.lastname}>"
    
class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, db.Sequence('product_id_seq', increment=1), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    code = db.Column(db.String(45), nullable = False, unique = True)
    price = db.Column(db.Float, nullabel = False)

    orders = db.relationship('Orders', back_populates="product")

    def __init__(self, name, code, price, id = None):
        self.id = id
        self.name = name
        self.code = code
        self.price = price

    def __repr__(self):
        return f"<Products {self.id} {self.name} {self.code} {self.price}>"
    
class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, db.Sequence('orders_id_seq', increment=1), primary_key = True)
    pid = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
    order_no = db.Column(db.String, nullable = False, unique = True)
    cid = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    order_date = db.Column(db.Date, nullable = False)

    product = db.relationship('Products', back_populates="orders")
    customer = db.relationship('Customer', back_populates="orders")
    payment = db.relationship('Payment', back_populates="order", uselist=False)

    def __init__(self, pid, cid, order_no, order_date, id = None):
        self.id = id
        self.pid = pid
        self.cid = cid
        self.order_no = order_no
        self.order_date = order_date
    
    def __repr__(self):
        return f"<Orders {self.id} {self.pid} {self.cid} {self.order_no} {self.order_date}>"
    
class PaymentType(db.Model):
    __tablename__ = "payment_type"
    id = db.Column(db.Integer, db.Sequence('payment_type_id_seq', increment=1), primary_key = True)
    name = db.Column(db.String, nullable = False)

    payment = db.relationship('Payment', back_populates="payment_types")

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<PaymentType {self.id} {self.name}>"