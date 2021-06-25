# Pasting Threat Images 

## Resizing.py 
1. Read the given images from their directories.
2. Made a list of background and threat images respectively.
3. **Rotated** the images using ndimage.rotate function from **scipy** library.
4. **Resized** the images using cv2.resize while maintaining the aspect ratio. The calculation for maintaining aspect ratio is done by taking the width of the required backgroud image as a constant input. The width of the fourth threat image has been reduced to fit it exactly into the background image.
5. These threat images are then saved. 

## Pasting.py
1. Read the images ( threat and background ) from their respective directories.
2. Reshaped the threat images to match the background dimensions.
3. **Masked** the images to return the object while eliminating the white noise.
4. Changed the pixel values in the background image to 0 based on the mask values.
5. Added both cleaned threat image ( after removing noise ) and tweaked background image ( after editing pixels where there is threat based on the mask) to obtain the required image.
6. Finally saved the pasted images.
