# Django-Projects

A collection of Django projects build with the approach of TDD. 

### 1.Inventory Management Web Application [Devlopment Status: Active]

A web application to manage inventory of a list of products in respective warehouses.

#### Database Tables:

    Product (product_id)
    Location (location_id)
    ProductMovement (movement_id, timestamp, from_location, to_location, product_id, qty)

Any one, or both of from_location and to_location can be filled. If you want to move things into a location, from_location will be blank, if you want to move things out, then to_location will be blank.

#### Views:

    Add/Edit/View Product
    Add/Edit/View Location
    Add/Edit/View ProductMovement

#### Report:

    Balance quantity in each location



### 1. BankAPI [Devlopment Status: Beta]

Create a REST service that can:

1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

#### Database Tables: 

	Bank(name,bankid)
	Branch(ifsc,bank_name,address,city,district,state,bank_deatils)

#### Views:
	Search Bank or branch details or by criteria of IFSC,name or city 

