import os

# Specify the paths
text_file_path = 'data/allweather/allweather.txt'  # Path to your text file
images_folder_path = 'data/allweather/input'  # Path to your folder containing images

# Read image names from the text file and remove the prefix
with open(text_file_path, 'r') as file:
    image_names = [line.strip().replace('./allweather/input/', '') for line in file.readlines()]

print(len(image_names))
# Get the list of image files in the folder
existing_images = set(os.listdir(images_folder_path))
print(len(existing_images))

# Find missing images
missing_images = [image_name for image_name in image_names if image_name not in existing_images]

# Output missing images
if missing_images:
    print(f"Missing images ({len(missing_images)}):")
    for missing_image in missing_images:
        print(missing_image)
else:
    print("No images are missing.")

# Optionally, save the missing images to a file
with open('missing_images.txt', 'w') as output_file:
    output_file.write('\n'.join(missing_images))
