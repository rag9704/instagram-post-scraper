# Instagram Post Scraper
This Python script utilizes the Instaloader library to scrape likes and comments from Instagram posts. The script takes Instagram credentials and a list of post links as command-line arguments, then outputs the data to a CSV file.

## Requirements
Python 3.x
Instaloader library (pip install instaloader)
Pandas library (pip install pandas)
Usage
Clone the repository:

```{r, engine='bash', count_lines}
git clone https://github.com/yourusername/instagram-post-scraper.git
cd instagram-post-scraper
Install the required libraries:
```
Copy code
```{r, engine='bash', count_lines}
pip install -r requirements.txt
```
Run the script with the following command:

bash
Copy code
```{r, engine='bash', count_lines}
python scraper.py <username> <password> <post_link1> <post_link2> ...
Replace <username> and <password> with your Instagram credentials, and <post_link1>, <post_link2>, etc., with the Instagram post links you want to scrape.
```
The script will output the results to a file named instagram.csv.

Command Line Arguments
username: Your Instagram username.
password: Your Instagram password.
links: List of Instagram post links to scrape.
Output
The script will generate a CSV file (instagram.csv) containing the following columns:

Platform: The social media platform (always "instagram" in this case).
Post: The URL of the Instagram post.
user: List of users who liked or commented on the post.
useraction: The type of user action ("like" or "comment").
Important Note
Please be aware of Instagram's rate limits when using this script. The script incorporates a basic rate-limiting mechanism to avoid exceeding the allowed number of requests per hour. If the rate limit is reached, the script will pause execution to comply with Instagram's policies.

## Disclaimer
This script is intended for educational purposes and personal use only. Make sure you comply with Instagram's terms of service and data usage policies when using this script. The developers are not responsible for any misuse or violations.
