import json


class Customers:
    customers = []
    users_id = []

    def add_customer(self,first_name,last_name,email,password):
        for user in self.customers:
            if user.firstname == first_name and user.lastname ==last_name:
                raise RuntimeError("You have already registered")
            new_customer =


class Customer:
    def __init__(self, firstname, lastname, email, password, user_id)
        self.firstName = firstname
        self.lastName = lastname
        self.email = email
        self.password = password
        self.user_id = user_id
