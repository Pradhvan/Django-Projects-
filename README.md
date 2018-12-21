# Django-Projects

A collection of Django projects build with the approach of TDD. 

### 1.Inventory Management Web Application

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

