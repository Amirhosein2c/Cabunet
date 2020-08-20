from datetime import datetime
import instaloader

L = instaloader.Instaloader()
# L.interactive_login("YOUR-USER-ID")  # You can insert your IG user ID if you like, it will next ask for your password interactively

SINCE = datetime(2014, 8, 20) # From this date  (YYYY, M, D)
UNTIL = datetime(2020, 8, 20) # To this date
hashtag = "mirrorselfie"    # Hashtag to search for
num_posts = 50000             # Max number of links to be retrieved


posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
counter = 0
post_list = []
file_object = open(hashtag + "_" + str(num_posts) + "_URLs.txt", 'a+')

userID = None
for post in posts:
    postdate = post.date
    user = post.owner_id
    # if user != userID:
    #     userID = user
    if SINCE < postdate < UNTIL:
        counter += 1
        if counter >= num_posts:
            break
        else:
            post_list.append(post.url)
            # L.download_post(post, hashtag)
            print("Post No: ", counter)
            print(post.url)
            print(post.owner_id)
            file_object.write(post.url + "\n\n")
file_object.close()
