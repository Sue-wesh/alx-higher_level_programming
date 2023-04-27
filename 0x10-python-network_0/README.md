0x10. Python - Network #0

Tasks
0. cURL body size
Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes, Use curl

1. cURL to the end
Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response, use curl

3. cURL only methods
Bash script that takes in a URL and displays all HTTP methods the server will accept., use curl

4. cURL headers
Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98

5. cURL POST parameters
Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD

6. Find a peak
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list

7. Only status code
Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

You are not allowed to use any pipe, redirection, etc.
You are not allowed to use ; and &&

8. cURL a JSON file
Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request

9. Catch me if you can!
Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

You have to use curl
You are not allow to use echo, cat, etc. to display the final result
Please test your script in the sandbox provided, using the web server running on port 5000
