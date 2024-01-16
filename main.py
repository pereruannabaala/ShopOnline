from app import app, db
from app.models import User, Admin, Customer, ProductsForSale, PurchasedProducts


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Admin=Admin,
        Customer=Customer,
        ProductsForSale=ProductsForSale,
        PurchasedProducts=PurchasedProducts
    )
