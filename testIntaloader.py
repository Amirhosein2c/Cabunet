from datetime import datetime
import instaloader

L = instaloader.Instaloader()
# L.interactive_login("YOUR-USER-ID")

hashtag = "elevatorselfie"
#"selfieascensor"

posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

SINCE = datetime(2014, 8, 10)
UNTIL = datetime(2020, 8, 10)

counter = 0
post_list = []
file_object = open(hashtag + "_50000_URLs.txt", 'a+')

userID = None
for post in posts:
    postdate = post.date
    user = post.owner_id
    # if user != userID:
    #     userID = user
    if SINCE < postdate < UNTIL:
        counter += 1
        if counter >= 50000:
            break
        else:
            post_list.append(post.url)
            # L.download_post(post, hashtag)
            print("Post No: ", counter)
            print(post.url)
            print(post.owner_id)
            file_object.write(post.url + "\n\n")
file_object.close()