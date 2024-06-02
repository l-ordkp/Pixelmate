from PIL import Image
import os

def resize_image():
    # Ask user for the path to the image
    input_path = input("Enter the path to the image: ")
    
    # Verify that the file exists
    if not os.path.isfile(input_path):
        print("The specified file does not exist.")
        return

    # Get and print the original dimensions of the image
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        print(f"Original dimensions: {original_width}x{original_height}")
    
    # Ask user for the desired dimensions
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))
    
    # Ask user for the output path
    output_path = input("Enter the output path (including file name without extension): ")
    
    # Open the image file and resize it
    with Image.open(input_path) as img:
        resized_img = img.resize((new_width, new_height))
        # Save the resized image
        resized_img.save(f"{output_path}.jpg")
        print(f"Image saved to {output_path}.jpg")

if __name__ == "__main__":
    resize_image()

    

  


