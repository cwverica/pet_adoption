from models import *
from app import app

connect_db(app)

# Create all tables
db.drop_all()
db.create_all()

# Empty table if not empty
Pet.query.delete()

watson = Pet(name="Watson", 
            species="Dog", 
            photo_url="https://www.thesprucepets.com/thmb/6-aH0A-UljMzAsLm4evRUHnS1gQ=/1920x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dog-3684791_1920-eb357f61749c4e83bdfccb9d12d65913.jpg", 
            age=5, 
            notes="The best dog in the whole world",  
            available=False)

db.session.add(watson)
db.session.commit()