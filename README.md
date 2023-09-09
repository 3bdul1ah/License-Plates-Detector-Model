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

### Initialization

1. **Program Initialization (Lines 1-3):**
   - The program starts by importing essential libraries and initializing two crucial components: the Excel Database and the License Plate Detector.

2. **Database Initialization (Lines 143-144):**
   - An instance of the ExcelDatabase class is created to handle data storage. This database will store information extracted from license plates.

3. **License Plate Detector Initialization (Line 145):**
   - An instance of the LicensePlateDetector class is created, which loads a pre-trained YOLO model for object detection and sets a detection threshold.

4. **License Plate Categories and States (Lines 37-59):**
   - The program defines specific classes for license plate categories and state abbreviations, which will be used to interpret the detected objects.

### Image Processing Loop

5. **Image Processing Loop (Lines 146-152):**
   - The program enters a loop designed to process multiple image URLs provided by the user. This loop continues until the user enters "exit" to terminate the program.

   - For each image URL:

      - **Retrieve Image Data (Lines 106-110):**
        - The program retrieves image data from the given URL using HTTP requests.

      - **Image Retrieval Check (Lines 108-109):**
        - It checks whether the image retrieval was successful.

         - **Convert Image Format (Lines 110-111):**
           - If successful, the program converts the retrieved image data into the OpenCV format for further analysis.

         - **Get Image Dimensions (Line 112):**
           - The height and width dimensions of the image are extracted to help with subsequent processing.

        ### License Plate Detection

         - **Use YOLO Model (Line 113):**
           - The YOLO model is employed to identify objects within the image, which may include license plates.

         - **Filter and Sort Detected Objects (Lines 114-117):**
           - Detected objects are filtered based on a specified score threshold to focus on high-confidence predictions. They are then sorted by their x-axis position for sequential analysis.

         #### Process Each Detected Object

         - For each detected object:

           - **Check for License Plate (Lines 118-121):**
             - The program determines if the object corresponds to a license plate based on the score threshold and class names.

           - If it's a license plate:

             - **Draw Rectangle Around Plate (Line 122):**
               - A green rectangle is drawn around the detected license plate on the image to highlight it.

             - **Crop Plate Region (Line 123):**
               - The program crops the region containing the license plate from the image for detailed analysis.

             #### Extract Plate Information

             - **Plate Analysis (Lines 124-128):**
               - The program analyzes the license plate image to extract three key pieces of information:
                 - Plate category (e.g., private, commercial)
                 - Plate number (alphanumeric)
                 - State (e.g., Dubai, Abu Dhabi)

           - **Print Plate Information (Lines 125-127):**
             - Extracted plate category, plate number, and state are printed to the console for user visibility and verification.

           - **Save Plate Data (Line 129):**
             - The program saves the extracted plate data, including category, number, and state, to the Excel Database for future reference.

         - **Display Processed Image (Lines 131-140):**
           - The image with the drawn rectangle and extracted information is displayed to the user for visual confirmation.

        - If image retrieval is unsuccessful:
           - A message indicating image retrieval failure is printed (Lines 132-134).

### Program Cleanup and Exit

6. **Cleanup and Exit (Lines 141-142):**
   - After processing all images, the program proceeds with cleanup procedures. This includes releasing any resources acquired during image processing and closing the Excel Database to ensure data integrity.

7. **End Program (Lines 142-152)**
   - The program concludes, and the user can exit the application.



> **Tips to avoid problems:**
> 1. Ensure all dependencies are installed.
> 2. Clone the repository.
> 3. Run the `plate-detector.py` Python script.
> 4. Input image URLs when prompted.
> 5. View the detected license plates and their details.
> 6. All detected details will be saved in an Excel file.






