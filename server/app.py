# app.py

from flask import Flask
from server.routes.home       import home_bp
from server.routes.properties import properties_bp
from server.routes.api.bookings import bookings_bp
from server.routes.payments   import payments_bp   # ← new import

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

# register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(properties_bp)
app.register_blueprint(bookings_bp)
app.register_blueprint(payments_bp)                # ← register payments

if __name__ == '__main__':
    app.run(debug=True)
