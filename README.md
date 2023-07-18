# WPUserFinder - WordPress User Finder

WPUserFinder is an Open-Source Intelligence (OSINT) tool that helps you find registered users on a WordPress website. It uses the WordPress REST API to fetch user data and can also check for authors.

## Features

- Fetches user data from a WordPress website using the WordPress REST API.
- Checks for a specific number of users as specified by the user.
- Checks for authors on the WordPress website.
- Uses sessions, cookies, and a generic user agent to mimic a real user and bypass basic security checks.
- Option to save the results to a text file.

## How It Works

1. The tool first validates the URL and the number of users to check entered by the user.
2. It then creates a session using Python's `requests` library. This session is used for all subsequent requests to the website.
3. For each user ID from 1 to the specified number, the tool sends a GET request to the WordPress REST API endpoint (`/wp-json/wp/v2/users/{user_id}`).
4. If a user is found, the tool prints the user information and also writes it to a file if the user chose to save the results.
5. The tool also checks for authors on the website by sending a GET request to the `/wp-json/wp/v2/users` endpoint.
6. If any authors are found, their information is also printed and written to the file.

## Dependencies

This tool requires Python 3 and the `requests` library. You can install the `requests` library using pip:
`pip install requests`


## Usage

1. Clone the repository: `git clone https://github.com/iNeerajSihag/WPUserFinder.git`
2. Navigate to the cloned repository: `cd WPUserFinder`
3. Install dependencies : `pip install requests` or `pip install -r requirements.txt`
4. Run the tool: `python main.py` or `python3 main.py`
5. Follow the prompts to enter the URL of the WordPress website and the number of users to check.

## Author
Neeraj Sihag - ([github.com/iNeerajSihag](https://github.com/iNeerajSihag))
## Note

This tool is for educational purposes only. The author is not responsible for any misuse of this tool. Always get proper authorization before testing a website.
