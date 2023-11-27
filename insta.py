import instaloader
import pandas as pd
import re
import argparse
import time

parser = argparse.ArgumentParser(description='Running Instagram Post Scrawler')

parser.add_argument('username', type=str, help='username')
parser.add_argument('password', type=str, help='password')
parser.add_argument('links', nargs='+', type=str, help='list of links')

args = parser.parse_args()

def extract_end_id(link):
    # Define a regular expression pattern to match the end ID
    pattern = r'https://www\.instagram\.com/p/([a-zA-Z0-9_-]+)'
    
    # Use re.search to find the match in the link
    match = re.search(pattern, link)
    
    # Check if a match is found
    if match:
        # Extract and return the end ID
        return match.group(1)
    else:
        # Return None if no match is found
        return None


Posts = [extract_end_id(link) for link in args.links]
print(Posts)


df = pd.DataFrame(columns=['Platform', 'Post', 'user','useraction'])
L = instaloader.Instaloader()
L.login(args.username,args.password)
#L.login('testing1232260', 'Durga@123')
requests_made = 0
rate_limit = 200
start_time = time.time()

for post_id in Posts:
    Post = instaloader.Post.from_shortcode(L.context, post_id)
    user=[]
    for like in Post.get_likes():
        user.append(like.username)
        requests_made += 1
        
        if requests_made >= rate_limit:
            # Calculate the time elapsed
            elapsed_time = time.time() - start_time
            print(len(user))

            # If the time elapsed is less than an hour, sleep to stay within the rate limit
            if elapsed_time < 3600:
                sleep_time = 3600 - elapsed_time
                print(f"Rate limit reached. Sleeping for {sleep_time} seconds.")
                time.sleep(sleep_time)

            # Reset the variables for the next hour
            start_time = time.time()
            requests_made = 0
        
    new_row = {'Platform': 'instagram', 'Post': f'https://www.instagram.com/p/{post_id}','user':user,'useraction':'like'}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

requests_made = 0
rate_limit = 200
start_time = time.time()   
for post_id in Posts:
    Post = instaloader.Post.from_shortcode(L.context, post_id)
    
    post_comments = Post.get_comments()
    for comment in post_comments:
        user_comments.append(comment.owner.username)
        requests_made += 1
        if requests_made >= rate_limit:
            # Calculate the time elapsed
            elapsed_time = time.time() - start_time

            # If the time elapsed is less than an hour, sleep to stay within the rate limit
            if elapsed_time < 3600:
                sleep_time = 3600 - elapsed_time
                print(f"Rate limit reached. Sleeping for {sleep_time} seconds.")
                time.sleep(sleep_time)

            # Reset the variables for the next hour
            start_time = time.time()
            requests_made = 0
    new_row = {'Platform': 'instagram', 'Post': f'https://www.instagram.com/p/{post_id}','user':user_comments,'useraction':'comment'}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


df.to_csv('instagram.csv')
