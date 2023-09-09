# License Plate Detection
<p align="center">
    <img src="https://i.ytimg.com/vi/ZeLg5rxLGLg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDMiHxm_6Tdby6DNjyr-vZRRLZ8lQ">
    <img src="https://i.postimg.cc/3Rc9Kf3W/Whats-App-Image-2023-09-09-at-13-38-57.jpg" alt="Image 1" width="40%" style="margin: 10px;">
    <img src="https://i.postimg.cc/mDs17QVV/Whats-App-Image-2023-09-09-at-13-34-31.jpg" alt="Image 2" width="40%" style="margin: 10px;">
</p>




## Table of Contents
- [Introduction](#introduction)
- [System Flow](#system-flow)
- [Dependencies](#dependencies)
- [Functional Overview](#functional-overview)
- [User Guide](#user-guide)
- [Updating the Repository](#updating-the-repository)


## Introduction
Welcome to the License Plate Detection Software! Crafted by **Abdullah Alshateri** and **Ahmed Balfiqah**, a third-year Electronic-Telecom Engineering students from UTM.

Harnessing the raw power of the Ultralytics YOLO model, our software can detect license plates in split-second timing using the ESP32-CAM. But it doesn't stop there! With advanced machine learning algorithms, the software dives deep into each detection, deciphering even the tiniest nuances of a license plate. What’s more, it seamlessly integrates these detections into an Excel database, ensuring that data archival is not just efficient but also organized.

Whether you're an enthusiast looking for a reliable license plate recognition solution or a professional seeking robust software for larger systems, our tool is designed to impress and deliver. Dive in and discover our license plate detector!


## User Guide

1. **Clone the Repository**
   Use the following command to clone the repository to your local machine:
      ```bash
      git clone https://github.com/3bdul1ah/UAE-License-Plates-Detector.git

3. **Navigate to the directory**
   Change to the cloned directory using the command:
      ```bash
      cd UAE-License-Plate-Detector  

3. **Setting up in an IDE**
   After navigating to the project directory:
   - Open the folder using your preferred Integrated Development Environment (IDE) such as PyCharm, VSCode, etc.
   - Locate the `plate-detector.py`script within your IDE.
   - Execute this script to initiate the license plate detection process.

  > **Note:** Ensure you have all the necessary dependencies installed before running the script.
   

## Updating the Repository

If you're collaborating on the UAE-License-Plates-Detector project, please adhere to the following guidelines to update the code in the repository.

### 1. Navigate to the Project Directory

Open your terminal and ensure you're in the project's directory. You can use the following command:

```bash
cd path/to/UAE-License-Plates-Detector
```

> **Note:** Replace `path/to` with the actual path to your local copy of the repository.

### 2. Check the Status of Your Local Repository

To view which files have changed, use the command:

```bash
git status
```

### 3. Stage Your Changes

- To stage all changes, use:

    ```bash
    git add .
    ```

- To stage specific files, use:

    ```bash
    git add filename1 filename2
    ```

    > **Note:** Replace `filename1`, `filename2`, etc. with the actual names of the files you've changed.

### 4. Commit Your Changes

Commit your staged changes with a descriptive message using the following command:

```bash
git commit -m "Brief description of your changes"
```

### 5. Push Your Changes to GitHub

Push your committed changes to the main repository with:

```bash
git push origin master
```

> **Note:** If you're working on a branch other than `master`, replace `master` with your branch's name.

### 6. Stay Updated

Always make sure you have the latest changes from the main repository before beginning your work to avoid conflicts. Use the command:

```bash
git pull origin master
```

Thank you for contributing to **UAE-License-Plates-Detector**!

## Dependencies

- `os`: For OS-level operations.
- `ultralytics`: Used for YOLO model integrations.
- `cv2`: Image and video processing tasks.
- `requests`: To fetch images from URLs.
- `numpy`: Numerical operations.
- `io`: Core I/O functionalities.
- `matplotlib`: Display images.
- `pandas`: Manage Excel operations effectively.

## System Flow

###START PROGRAM
|
|---[Initialization]
|   |
|   |--- Load Essential Libraries: cv2, numpy, ultralytics, requests, io, matplotlib, pandas
|   |    |
|   |    |--- Import required Python libraries.
|   |    |
|   |    |--- Initialize OpenCV (cv2) for image processing.
|   |    |
|   |    |--- Import Ultralytics for YOLO model integration.
|   |    |
|   |    |--- Import numpy for numerical operations.
|   |    |
|   |    |--- Import requests for fetching images via HTTP.
|   |    |
|   |    |--- Import io for core I/O operations.
|   |    |
|   |    |--- Import matplotlib for plotting and visualization.
|   |    |
|   |    |--- Import pandas for Excel database operations.
|   |
|   |--- Set Global Variables: model_path, db, threshold, specific_classes, state_classes
|   |    |
|   |    |--- Set the path for the YOLO model weights (model_path).
|   |    |
|   |    |--- Create an instance of the ExcelDatabase class (db).
|   |    |
|   |    |--- Set a confidence threshold for object detection (threshold).
|   |    |
|   |    |--- Define specific_classes (characters for license plates).
|   |    |
|   |    |--- Define state_classes (mapping class labels to state names).
|   |
|   |--- Configure YOLO Model: Load YOLO model with model_path
|        |
|        |--- Load YOLO model using Ultralytics with the specified model_path.
|        |
|        |--- Initialize the YOLO model for object detection.
|
|---[Main Execution Loop]
|   |
|   |--- WHILE True  # Loop to get multiple image URLs
|   |    |
|   |    |--- Get image_url from the user.
|   |    |
|   |    |--- IF image_url is "exit" THEN BREAK the loop.
|   |    |
|   |    |--- Call process_image(image_url) to process the image.
|   |    |
|   |    |--- IF processed_image is not None
|   |    |    |
|   |    |    |--- Display the processed image using display_image(processed_image).
|   |
|   |--- [End of Main Loop]
|
|---[ExcelDatabase Class]
|   |
|   |--- INIT(filename='plates_data.xlsx'): Initialize ExcelDatabase instance with a filename.
|   |    |
|   |    |--- Set the filename for the Excel database (default is 'plates_data.xlsx').
|   |
|   |--- METHOD save(plate_data): Save plate data to Excel database.
|        |
|        |--- IF the Excel file does not exist
|        |    |
|        |    |--- Create a new Excel file with columns: "Plate Category", "Plate Number", "State", "Image URL".
|        |
|        |--- Read the existing Excel file.
|        |
|        |--- Create a new data frame (new_data) with the plate data.
|        |
|        |--- Concatenate the new data frame with the existing data frame.
|        |
|        |--- Save the updated data frame to the Excel file.
|
|---[LicensePlateDetector Class]
|   |
|   |--- INIT(model_path, db): Initialize LicensePlateDetector instance.
|   |    |
|   |    |--- Load YOLO model with the specified model_path.
|   |    |
|   |    |--- Set the confidence threshold for object detection.
|   |    |
|   |    |--- Initialize the ExcelDatabase instance (db).
|   |
|   |--- METHOD detect_text(image, plate_category=None): Detect text (plate details) in the image.
|   |    |
|   |    |--- IF plate_category is None, initialize empty lists for plate number and category.
|   |    |
|   |    |--- Set the default state_name to "couldn't be detected."
|   |    |
|   |    |--- Initialize plate_string and category lists.
|   |    |
|   |    |--- Get image dimensions (H, W).
|   |    |
|   |    |--- Perform object detection on the image using the YOLO model.
|   |    |
|   |    |--- Sort the detection results by the x-axis position.
|   |    |
|   |    |--- Iterate through sorted results:
|   |    |    |
|   |    |    |--- IF the class name is in state_classes:
|   |    |    |    |
|   |    |    |    |--- Update state_name with the corresponding state name.
|   |    |
|   |    |--- IF state_name is 'Sharjah' or 'Abu Dhabi'
|   |    |    |
|   |    |    |--- Iterate through sorted results:
|   |    |    |    |
|   |    |    |    |--- IF score > threshold and class name in specific_classes
|   |    |    |    |    |
|   |    |    |    |    |--- IF (y2 <= H // 2) or (x2 <= W // 5)
|   |    |    |    |    |    |
|   |    |    |    |    |    |--- Append class name to category.
|   |    |    |    |    |    |
|   |    |    |    |    |--- ELSE
|   |    |    |    |    |    |
|   |    |    |    |    |    |--- Append class name to plate_number.
|   |    |    |    |    |
|   |    |    |    |    |--- Concatenate category and plate_number to form plate_category.
|   |    |
|   |    |--- ELSE (state_name is not 'Sharjah' or 'Abu Dhabi')
|   |    |    |
|   |    |    |--- Iterate through sorted results:
|   |    |    |    |
|   |    |    |    |--- IF score > threshold and class name in specific_classes
|   |    |    |    |    |
|   |    |    |    |    |--- IF class name is alphabetic
|   |    |    |    |    |    |
|   |    |    |    |    |    |--- Append class name to category.
|   |    |    |    |    |    |
|   |    |    |    |    |--- ELSE IF class name is a digit
|   |    |    |    |    |    |
|   |    |    |    |    |    |--- Append class name to plate_number.
|   |    |    |    |    |
|   |    |    |    |    |--- Concatenate category and plate_number to form plate_category.
|   |    |
|   |    |--- RETURN plate_category, plate_number, state_name.
|   |
|   |--- METHOD process_image(image_url): Process an image from a URL.
|   |    |
|   |    |--- Fetch the image data from the provided URL using requests.
|   |    |
|   |    |--- IF the response status code is 200 (success)
|   |    |    |
|   |    |    |--- Decode the image data and create an OpenCV image.
|   |    |    |
|   |    |    |--- Get image dimensions (H, W).
|   |    |    |
|   |    |    |--- Perform object detection using the YOLO model.
|   |    |    |
|   |    |    |--- Sort the detection results by the x-axis position.
|   |    |    |
|   |    |    |--- Iterate through sorted results:
|   |    |    |    |
|   |    |    |    |--- IF score > threshold and class name is 'plate'
|   |    |    |    |    |
|   |    |    |    |    |--- Draw a green bounding box around the detected plate.
|   |    |    |    |    |
|   |    |    |    |    |--- Extract the plate image.
|   |    |    |    |    |
|   |    |    |    |    |--- Call detect_text() to extract plate details (plate_category, plate_number, state).
|   |    |    |    |    |
|   |    |    |    |    |--- PRINT plate details.
|   |    |    |    |    |
|   |    |    |    |    |--- Save plate details to the Excel database (db).
|   |    |    |
|   |    |--- ELSE (response status code is not 200)
|   |    |    |
|   |    |    |--- PRINT "Failed to retrieve image from URL: {image_url}".
|   |    |
|   |    |--- RETURN the processed image.
|   |
|   |--- METHOD display_image(processed_image): Display an image using Matplotlib.
|        |
|        |--- Create a Matplotlib figure.
|        |
|        |--- Display the processed image in the figure.
|        |
|        |--- SHOW the Matplotlib figure.


### END PROGRAM

> **Tips to avoid problems:**
> 1. Ensure all dependencies are installed.
> 2. Clone the repository.
> 3. Run the `plate-detector.py` Python script.
> 4. Input image URLs when prompted.
> 5. View the detected license plates and their details.
> 6. All detected details will be saved in an Excel file.






