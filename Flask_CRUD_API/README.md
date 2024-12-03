
# Flask Laptop API - Testing with Postman
# Author
- [Khadijah Seidu](https://github.com/kadijaseidu)

This API provides endpoints to manage laptops. It allows the user to add a laptop, get access to all laptops, get access to a laptop by name, get access to a laptop by a laptop number, update a laptop by a laptop number, and also delelte a laptop by a laptop number. Below are the instructions for testing the API endpoints using Postman.

You can find the project repository [here](https://github.com/kadijaseidu/Tech4girls_Backend).
## Start the Flask Application
You need to run the Flask app first so that the server is up and running, allowing you to send requests to it.

## Set Up Postman
Once your Flask app is running, open Postman and perform the following steps to test the API endpoints.

# Example 1: Testing POST /laptops/add (Add a Laptop)
- Open Postman.
- Set the request method to POST.
- In the URL field, enter the following URL: 'http://localhost:5000/laptops/add'
- Go to the Body tab in Postman.
- Select raw and choose JSON by clicking on text.
- Enter the JSON data for the new laptop, 
- for example:

{
  "name": "Dell",
  "laptop_number": "2023",
  "student_id": "8"
}
- Click on Send.

- Expected Response:
If the laptop is added successfully, you should see a response with a 201 Created status code and a message like:

'{
  "message": "Laptop added successfully"
}'

If there’s an error or if you forget a required field or the laptop number already exists, the server will respond with an error message in JSON format.

# Example 2: Testing GET /laptops (Get All Laptops)
- Set the request method to GET.
- Enter the following URL: 'http://localhost:5000/laptops/'
- Click on Send.

- Expected Response:
- You should see a list of all laptops in the database. For instance;

'[
  {
    "name": "Dell",
    "laptop_number": "2023",
    "student_id": "8"
  }
]'


# Example 3: Testing GET /laptops/name/<name> (Get Laptop by Name)
- Set the request method to GET.
- Enter the following URL: 'http://localhost:5000/laptops/name/Dell'
- Expected Response:
The server should return the details of the Dell laptop:

'{
  "name": "Dell",
  "laptop_number": "2023",
  "student_id": "8"
}'

- If the laptop is not found or if you query for a laptop that doesn't exist, the server will return an error response like this:

'{
  "error": "Laptop not found."
}'

# Example 4: Testing PUT /laptops/update/<laptop_number> (Update Laptop by Number)
- Set the request method to PUT.
- Enter the following URL: 'http://localhost:5000/laptops/update/2023'
- Go to the Body tab in Postman.
- Choose raw and set the format to JSON.
- Enter the updated details for the laptop:

'{
  "name": "Dell XPS 18 Updated",
  "student_id": "8"
}'

- Click on Send.
- Expected Response:
- You should receive a 200 OK response with a message like:

'{
  "message": "Laptop updated successfully"
}'

- If the laptop is not found, the server will return an error response like this:

'{
  'error': Laptop number not found
}, 404'

# Example 5: Testing DELETE /laptops/delete/<laptop_number> (Delete Laptop by Number)
- Set the request method to DELETE.
- Enter the following URL: 'http://localhost:5000/laptops/delete/2023'
-Click on Send.

- Expected Response:
- If the laptop is deleted successfully, the response will be:

'{
  "message": "Laptop with 2023 deleted successfully."
}'


# Conclusion

This API provides an easy way to manage laptops in your system with endpoints for adding, retrieving, updating, and deleting a laptop. It handles common errors such as missing fields or laptop not found scenarios with appropriate HTTP status codes and messages. 

Using Postman, you can easily test the functionality of each endpoint. Ensure that you send the correct JSON payloads for `POST` and `PUT` requests and use the appropriate URLs for `GET`, `PUT`, and `DELETE` operations.

By following this documentation, you should be able to manage your laptop records efficiently through the API.
