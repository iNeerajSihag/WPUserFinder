import requests
import json
from urllib.parse import urlparse

def get_user_info(session, website_url, user_id):
    response = session.get(f"{website_url}/wp-json/wp/v2/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_authors(session, website_url):
    response = session.get(f"{website_url}/wp-json/wp/v2/users")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def validate_url(website_url):
    try:
        result = urlparse(website_url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def validate_num_users(num_users):
    try:
        num = int(num_users)
        return num > 0
    except ValueError:
        return False

def print_and_write(file, message, end='\n'):
    print(message, end=end)
    if file:
        file.write(message + end)

def main():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    })

    print_and_write(None, f"+---+---+---+---+---+---+---+---+---+---+")
    print_and_write(None, "WPUserFinder - WordPress Open-Source Intelligence (OSINT) Tool")
    print_and_write(None, "Author - Neeraj Sihag")
    print_and_write(None, "GitHub - https://github.com/iNeerajSihag")
    print_and_write(None, f"+---+---+---+---+---+---+---+---+---+---+")

    while True:
        website_url = input("Enter URL of WordPress site (include http:// or https://). Eg - https://website.com : ")
        if validate_url(website_url):
            break
        else:
            print("Invalid URL. Please enter a valid URL including http:// or https://")

    while True:
        num_users = input("Enter the number of users you want to check: ")
        if validate_num_users(num_users):
            num_users = int(num_users)
            break
        else:
            print("Invalid input. Please enter value greater than 0.")

    save_to_file = False
    while True:
        save_to_file_input = input("Do you want to save the results to a text file? (y/n): ").lower()
        if save_to_file_input in ['y', 'n']:
            save_to_file = save_to_file_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    file = None
    if save_to_file:
        filename = input("Enter the filename (without .txt): ").strip()
        filename = filename.split('.')[0]  # Removes any file extension, if provided by user.
        filename += '.txt'  # Add .txt extension to saved file.
        file = open(filename, 'w')

    print_and_write(file, f"+---+---+---+---+---+---+---+---+---+---+")
    print_and_write(file, "Author - Neeraj Sihag")
    print_and_write(file, "GitHub - https://github.com/iNeerajSihag")
    print_and_write(file, f"+---+---+---+---+---+---+---+---+---+---+")
    print_and_write(file, f"\nChecking for {num_users} registered users on {website_url}.\n")
    total_users_found = 0
    user_ids_found = []
    print_and_write(file, f"+---+---+---+---+---+---+---+---+---+---+")

    for user_id in range(1, num_users + 1):
        print_and_write(file, f"Checking for user : {user_id} --> ", end="")
        user_info = get_user_info(session, website_url, user_id)
        if user_info is not None:
            total_users_found += 1
            user_ids_found.append(user_id)
            print_and_write(file, "User found")
            print_and_write(file, f"\tID - {user_info['id']}")
            print_and_write(file, f"\tName - {user_info['name']}")
            print_and_write(file, f"\tUsername - {user_info['slug']}")
            print_and_write(file, f"\tUrl - {user_info['link']}")
            print_and_write(file, f"\tDescription - {user_info['description']}")
            print_and_write(file, f"\tSlug - {user_info['slug']}")
            print_and_write(file, f"\tAvatar - {user_info.get('avatar_urls', {}).get('96', 'Not available')}")
            print_and_write(file, f"\tFull Information - {json.dumps(user_info, indent=4)}")
        else:
            print_and_write(file, "User not found")

        print_and_write(file, f"-------------------------------------")

    print_and_write(file, f"\nTotal Users found - {total_users_found}")
    if total_users_found > 0:
        print_and_write(file, f"User ID found - {', '.join(map(str, user_ids_found))}")
    else:
        print_and_write(file, "No user Found")
    print_and_write(file, f"-------------------------------------")

    print_and_write(file, "\nChecking for authors...\n")
    authors = get_authors(session, website_url)
    if authors is not None and len(authors) > 0:
        print_and_write(file, f"Total authors found: {len(authors)}")
        for author in authors:
            print_and_write(file, f"-------------------------------------")
            print_and_write(file, f"Author ID: {author['id']}")
            print_and_write(file, f"Author Name: {author['name']}")
            print_and_write(file, f"Author URL: {author['link']}")
            print_and_write(file, f"Author Description: {author['description']}")
            print_and_write(file, f"-------------------------------------")
    else:
        print_and_write(file, "No authors found.")

    if save_to_file:
        file.close()
        print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    main()
