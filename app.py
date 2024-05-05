import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
channel = '@careerrevamp'

all_posts = []


with TelegramClient('foobar', api_id, api_hash) as client:
    for message in client.iter_messages(channel):
        post_text = f'{message.date.strftime("%Y-%m-%d %H:%M:%S")} - {message.text}\n'
        all_posts.append(post_text)


print(all_posts)


# Create a directory to store the text files
# os.makedirs('telegram_posts', exist_ok=True)


# # Process and save the retrieved posts
# with open(f'telegram_posts/{channel_username}_posts_{file_counter}.txt', 'w', encoding='utf-8') as file:
#    for post in all_posts:
#        file_size += len(post.encode('utf-8'))


#        if file_size > max_file_size:
#            file_counter += 1
#            file_size = len(post.encode('utf-8'))
#            file.close()
#            file = open(f'telegram_posts/{channel_username}_posts_{file_counter}.txt', 'w', encoding='utf-8')


#        file.write(post)




