# restaurant-code-challenge..
# code-.Restaurant

# Restaurant Reviews Project

The Restaurant Reviews Project is a Python application that uses SQLAlchemy to manage restaurant reviews. 
It allows users to create, read, update, and delete reviews for various restaurants.
This README provides instructions on setting up the project, using it, and understanding its components.

## Table of Contents

 [Features]z(#features)
 [Setup](#setup)
 [Usage](#usage)
 [Project Structure](#project-structure)
 [Contributing](#contributing)
 [License](#license)

## Features

Restaurant Management Create and manage restaurant records, including name, price, and reviews.
Customer Management Create and manage customer records, including first name, last name, and reviews.
Review Creation Add reviews for specific restaurants, including comments and star ratings.
Favorite Restaurants Find a customer's favorite restaurant based on their reviews.
 Review Deletion Delete reviews by customers for specific restaurants.

## Setup

1. **Clone the Repository:**

   ```shell
   git clone <repository_url>
   cd restaurant-reviews-project
   ```

2. **Install Dependencies:**

   Install the required dependencies using `pip`:

   
   
## Usage



### Restaurant Management

- Create a new restaurant:

  ```python
  new_restaurant = Restaurant(name="Restaurant Name", price=50)
  session.add(new_restaurant)
  session.commit()
  ```

- Get all reviews for a restaurant:

  ```python
  restaurant = session.query(Restaurant).first()
  reviews = restaurant.all_reviews()
  ```

  

### Customer Management

- Create a new customer:

  ```python
  new_customer = Customer(first_name="John", last_name="Doe")
  session.add(new_customer)
  session.commit()
  ```

- Add a review for a restaurant:

  ```python
  customer = session.query(Customer).first()
  restaurant = session.query(Restaurant).first()
  customer.add_review(restaurant, rating=5)


### Review Management

- Create a new review:

  ```python
  new_review = Review(comment="Great restaurant!", star_rating=4, restaurant=restaurant, customer=customer)
  session.add(new_review)
  session.commit()
  ```

- Get the customer and restaurant for a review:

  ```python
  review = session.query(Review).first()
  customer = review.customer
  restaurant = review.restaurant
  ```

## Project Structure

 `models.py` Defines the SQLAlchemy models for restaurants, customers, and reviews.
 `seeds.py` Seeds the database with initial data.
 `migrations/`Directory containing database migration scripts.
 `README.md`This README file.

## Contributing

If you'd like to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md]

## License

This project is licensed under the MIT License @mwanikititus@gmail.com# code-.Restaurant
