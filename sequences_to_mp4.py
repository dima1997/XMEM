import cv2
import os

def create_video_from_images(folder_path, seq, output_path, fps=30):
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if ((seq in f) and (f.endswith('.bmp')))]
    
    # Sort the image files based on their frame number
    image_files.sort(key=lambda x: int(x.split('-')[-1].split('.')[0]))

    # Get the dimensions of the first image
    first_image = cv2.imread(os.path.join(folder_path, image_files[0]))
    height, width, _ = first_image.shape

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write images to video
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        frame = cv2.imread(image_path)
        out.write(frame)

    # Release video writer
    out.release()

# Example usage (change the name to the sequence to convert):
name = 'swan'
folder_path = 'sequences-train'
output_path = f'{name}.mp4'
create_video_from_images(folder_path, name ,output_path)

