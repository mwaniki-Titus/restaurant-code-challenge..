from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

engine=create_engine('sqlite:///restaurant.db')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()
Base=declarative_base()
    

class Restaurant(Base):
    __tablename__ ='restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews=relationship('Review',back_populates='restaurant')
    customers=association_proxy('reviews','customer',creator=lambda us: Review(customer=us))
   

    def __repr__(self):
        return f'Restaurant Name: {self.name} Price: {self.price}'
    
    def restaurant_reviews(self):
        return self.reviews 

    def restaurant_customers(self):
         return[review.customer for review in self.reviews]
    
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(desc(cls.price)).first()
    
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]
        


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews=relationship('Review',back_populates='customer')
    restaurants=association_proxy('reviews','restaurant',creator=lambda gm: Review(restaurant=gm))


    def __repr__(self):
        return f'First Name: {self.first_name} Last Name {self.last_name}'

    def customer_reviews(self):
        return self.reviews
    
    def customer_restaurants(self):
        return [review.restaurant for review in self.reviews]
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def favorite_restaurant(self):
        return session.query(Restaurant).join(Review).filter(Review.customer_id==self.id).order_by(desc(Review.star_rating)).first()
    
    def add_reviews(self,restaurant,rating):
        new_review=Review(customer=self,restaurant=restaurant,star_rating=rating)
        session.add(new_review)
        session.commit()
    def delete_reviews(self,restaurant):
        session.query(Review).filter(Review.customer_id==self.id,Review.restaurant_id==restaurant.id).delete()
        session.commit()    

class Review(Base):
    __tablename__ ='reviews'

    id=Column(Integer(),primary_key=True)
    comment=Column(String())
    star_rating=Column(Integer())
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    customer_id=Column(Integer(),ForeignKey('customers.id'))
    restaurant=relationship('Restaurant',back_populates='reviews')
    customer=relationship('Customer',back_populates='reviews')

    def __repr__(self):
        return f'Review: {self.comment} star_rating {self.star_rating}'  
    
    def review_customer(self):
        return self.customer
    
    def Review_restaurant(self):
        return self.restaurant
    
    def full_review(self):
        return f'Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars'
    


