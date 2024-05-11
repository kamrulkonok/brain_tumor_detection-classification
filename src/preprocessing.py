import numpy as np
import cv2
import os


# Using adaptive thresholding and contour finding to crop the region of interest (ROI).
def find_roi(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cropped_img = img[y:y+h, x:x+w]
        return cropped_img
    else:
        return img
        
#Processes the images from a list of image paths by finding the ROI and resizing them.
def process_images(image_paths, save_path, img_size):

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    for image_path in image_paths:
        image = cv2.imread(image_path)
        if image is not None:
            roi = find_roi(image)
            resized_image = cv2.resize(roi, (img_size, img_size))
            image_name = os.path.basename(image_path)
            cv2.imwrite(os.path.join(save_path, image_name), resized_image)
            
#    Processes each image in the dataset directory.
def process_dataset(dataset_path, save_path, img_size):

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    image_files = [f for f in os.listdir(dataset_path) if os.path.isfile(os.path.join(dataset_path, f))]
    for image_file in image_files:
        image_path = os.path.join(dataset_path, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            roi = find_roi(image)
            resized_image = cv2.resize(roi, (img_size, img_size))
            cv2.imwrite(os.path.join(save_path, image_file), resized_image)

if __name__ == "__main__":
    dataset_path = r"C:\Users\Konok\Desktop\archive"
    img_size = 256
    categories = ["glioma", "meningioma", "notumor", "pituitary"]
    
    for category in categories:
        training_path = os.path.join(dataset_path, "Training", category)
        testing_path = os.path.join(dataset_path, "Testing", category)
        cleaned_training_path = os.path.join(dataset_path, "cleaned", "Training", category)
        cleaned_testing_path = os.path.join(dataset_path, "cleaned", "Testing", category)

        if os.path.isdir(training_path):
            process_dataset(training_path, cleaned_training_path, img_size)
        else:
            print(f"Directory does not exist: {training_path}")
        
        if os.path.isdir(testing_path):
            process_dataset(testing_path, cleaned_testing_path, img_size)
        else:
            print(f"Directory does not exist: {testing_path}")
