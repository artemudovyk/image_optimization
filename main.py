import tinify
import os
from dotenv import dotenv_values # https://github.com/theskumar/python-dotenv
import shutil


# Load environment variables
config = dotenv_values(".env")  # dictionary with environment variables from './.env' file

supported_filetypes = [
    'jpeg',
    'jpg',
    'png',
    'webp'
]

# TODO: process only supported file types
# TODO: log process

# Your API token from https://tinify.com/dashboard/api
tinify.key = config['TINIFY_API_KEY']

unoptimized_path = './unoptimized_images'
optimized_path = './optimized_images'
unsupported_path = './unsupported_images'

images = os.listdir(unoptimized_path)
optimized_images = os.listdir(optimized_path)

for image in images:
    # Check if it's supported image filetype. If not supported, move to another folder
    image_extension = image.split('.')[-1].lower()
    if image_extension not in supported_filetypes:
        shutil.move(f'{unoptimized_path}/{image}', unsupported_path)
        print(f'{image_extension} is not supported by this API. {image} moved to an {unsupported_path} folder')
        continue
        
    # If wasn't process already, send via API to optimization
    if image not in optimized_images:
        source = tinify.from_file(f'{unoptimized_path}/{image}') # upload
        source.to_file(f'{optimized_path}/{image}') # download


