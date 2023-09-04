from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer,Review

fake=Faker()

if __name__=='__main__':

    engine=create_engine('sqlite:///restaurant.db')
    Session=sessionmaker(bind=engine)
    session=Session()
    
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()
    session.commit()

    print("seeding.....")

    restaurants=[]
    for i in range(3):
        restaurant=Restaurant(
            name=fake.name(),
            price=fake.pyint()
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)
    
    customers=[]
    for i in range(5):
        customer=Customer(
            first_name=fake.name(),
            last_name=fake.name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

    reviews=[]
    for restaurant in restaurants:
        for i in range(random.randint(1,5)):
            customer=random.choice(customers)

            review=Review(
                comment=fake.sentence(),
                star_rating=random.randint(0,10),
                restaurant_id=restaurant.id,
                customer_id=customer.id
            )
            if restaurant not in customer.restaurants:
                customer.reviews.append(review)
                session.commit()
            
           
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()        