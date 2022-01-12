# Mass Image Optimization Script
Script based on https://tinyjpg.com/developers/reference/python API.

Optimized all images in "unoptimized_images" folder and saves optimized images in "optimized_images" folder. All images with unsupported type (all except png, jpg/jpeg and webp) will be moved to "unsupported_images" folder.

# Usage
To use it install all requirements, rename '.env.example' file to '.env' and add your API key (that you can get here https://tinyjpg.com/developers, first 500 images/month are free as of January 2022), paste all images that you want to process in "unoptimized_images" folder and run script.