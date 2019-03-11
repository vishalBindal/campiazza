# campiazza
Campiazza: 'Campus Piazza' : A market portal for IITD students
This website is hosted at https://campiazza.herokuapp.com/shop/

## Note
__Yet to update technical details__<br>
__In process of updating images ( after having set up amazon s3 service) (Temporarliy added item images to admin page)__

## Features
* Login - for existing users, and sign up - for new users 
* Admin - admin portal
* Search bar & category links - to search existing products
* Sell - Link to sell your products. However, if you are not logged in you will be redirected to login page


### Login
* As per requirements, 4 users have been already created with username user_i and password pass_i (eg user_1 and pass_1)
* You are free to access these or create a new account.
* After logging in, access your profile page to view and edit your profile. You may also change your profile picture.
* Your profile page also shows items you have uploaded and your orders

### Search
* You can use the search bar to search products by name.
* You can also search by category via the navbar above

### Sell
* To sell, you need to be logged in
* Fill the details form consisting of 2 steps
* You can add as many images as you want. To add an image, choose file and click upload. While adding the final image, choose file and click continue.
* If you click continue without selecting any image, then a default 'Unknown' image will be assigned to the product.
* After clicking continue you will be redirected to the details page of the product.

### Buy
* Click on a product to view its details page. If you are logged in, you will see a 'Buy now' button.
* Upon clicking the button, you will be redirected to a confirmation page, displaying details of item and seller. If your address is not yet filled in, you will be prompted to update your address in your profile. Else, click confirm.
* You can now check the product in 'Your orders' section on your profile page. It will contain info about delivery address, date/time of purchase and link to buyer's profile.

## Someone buys your product
* When you log in, you will receive an alert indicating the no of your products (if any) which have been bought since your last login. For this the app checks the buy time of user's items with the last login time of user.
* Visit 'Your items' in your profile page to view your products and their buyer information (link to buyer profile, date/time of purchase, delivery address)

## Admin
* To login to the admin portal , use username='admin' and password='admin'
* In Users section, you can view a list of all users and their details. 
* In Items section, you can view details of all transactions, and item information.

