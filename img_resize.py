from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image file
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image saved to {output_path}")

def main():
    # Ask user for the path to the image
    input_path = input("Enter the path to the image: ")
    
    # Verify that the file exists
    if not os.path.isfile(input_path):
        print("The specified file does not exist.")
        return
    
    # Ask user for the desired dimensions
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))
    
    # Ask user for the output path
    output_path = input("Enter the output path (including file name and extension): ")
    
    # Resize the image
    resize_image(input_path, output_path, new_width, new_height)

if __name__ == "__main__":
    main()
