import sys
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


def create_batches(posts, max_size_mb=12):
    # Calculate the max size in bytes
    max_size_bytes = max_size_mb * 1024 * 1024

    batches = []
    batch = []
    current_size = 0

    for post in posts:
        # Calculate the size of the current string in bytes
        string_size = sys.getsizeof(post)

        # Check if adding this string would exceed the max batch size
        if current_size + string_size > max_size_bytes:
            # Start a new batch
            batches.append(batch)
            batch = [post]
            current_size = string_size
        else:
            # Add the string to the current batch
            batch.append(post)
            current_size += string_size

    # Add the last batch to the list if not empty
    if batch:
        batches.append(batch)

    return batches


def save_batches_to_files(batches, output_prefix="posts"):
    file_count = 1
    for batch in batches:
        file_name = f"{output_prefix}_{file_count}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            for string in batch:
                file.write(string + '\n')  # Each string on a new line
        print(f"Batch {file_count} saved to {file_name}")
        file_count += 1


batches = create_batches(all_posts)

save_batches_to_files(batches)

