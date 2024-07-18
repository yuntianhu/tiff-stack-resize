from PIL import Image
import os

def compress_tiff_stack(input_folder, output_file, resize_factor=None, bit_depth_reduction=None):
    
    files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith('.tiff') or f.lower().endswith('.tif')]
    
  
    files.sort()

   
    first_image = Image.open(files[0])

   
    if resize_factor:
        first_image = first_image.resize((first_image.width // resize_factor, first_image.height // resize_factor),  Image.ANTIALIAS)
    
    
    if bit_depth_reduction:
        first_image = first_image.convert(bit_depth_reduction)

    tiff_images = []
    for file in files[1:]:
        img = Image.open(file)

      
        if resize_factor:
            img = img.resize(img.width // resize_factor, img.height // resize_factor)

       
        if bit_depth_reduction:
            img = img.convert(bit_depth_reduction)

        tiff_images.append(img)

   
    first_image.save(
        output_file,
        compression='tiff_deflate',
        save_all=True,
        append_images=tiff_images
    )
    print(f"Compressed TIFF stack saved to {output_file}")


input_folder = '/home/yuntian/tifzip' # replace it with your input path
output_file = 'output7.tiff'  # replace it with your output path


compress_tiff_stack(input_folder, output_file, resize_factor=2, bit_depth_reduction=None)
