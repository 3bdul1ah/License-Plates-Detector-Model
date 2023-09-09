# License Plate Detection
<p align="center">
    <img src="https://i.ytimg.com/vi/ZeLg5rxLGLg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDMiHxm_6Tdby6DNjyr-vZRRLZ8lQ">
    <img src="https://i.postimg.cc/3Rc9Kf3W/Whats-App-Image-2023-09-09-at-13-38-57.jpg" alt="Image 1" width="40%" style="margin: 10px;">
    <img src="https://i.postimg.cc/mDs17QVV/Whats-App-Image-2023-09-09-at-13-34-31.jpg" alt="Image 2" width="40%" style="margin: 10px;">
</p>




## Table of Contents
- [Introduction](#introduction)
- [Code Flowchart](#code-flowchart)
- [Dependencies](#dependencies)
- [Functional Overview](#functional-overview)
- [User Guide](#user-guide)
- [Updating the Repository](#updating-the-repository)
- [Future Enhancements](#future-enhancements) 


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

### START PROGRAM

#### 1. IMPORT Necessary Libraries

#### 2. DEFINE CLASS ExcelDatabase:
- **INIT(filename)**:
    - SET filename
- **METHOD save(plate_data)**:
    - IF filename does not exist:
        - CREATE new Excel file with columns
    - READ Excel file
    - APPEND new plate data to the Excel file
    - SAVE Excel file

#### 3. DEFINE CLASS LicensePlateDetector:
- **INIT(model_path, db)**:
    - LOAD YOLO model
    - SET confidence threshold
    - SET specific classes (characters for license plates)
    - SET state classes (to map class labels to actual state names)
- **METHOD detect_text(image)**:
    - INIT empty lists for plate number and category
    - SET default state_name to "couldn't be detected"
    - PARSE the image to detect state and characters
    - RETURN plate_category, plate_string, state_name
- **METHOD process_image(image_url)**:
    - FETCH the image using the provided URL
    - PROCESS the image through the YOLO model
    - LOOP through detected objects:
        - IF detected object is a plate:
            - EXTRACT plate details
            - PRINT plate details
            - SAVE plate details to Excel database
    - RETURN the processed image
- **METHOD display_image(processed_image)**:
    - DISPLAY the image using matplotlib

#### 4. MAIN EXECUTION:
- SET path for the YOLO model
- CREATE instance of ExcelDatabase
- CREATE instance of LicensePlateDetector
- LOOP continuously:
    - GET image_url from user
    - IF image_url is "exit":
        - BREAK
    - PROCESS the image through LicensePlateDetector
    - DISPLAY the processed image

### END PROGRAM

> **Tips to avoid problems:**
> 1. Ensure all dependencies are installed.
> 2. Clone the repository.
> 3. Run the `plate-detector.py` Python script.
> 4. Input image URLs when prompted.
> 5. View the detected license plates and their details.
> 6. All detected details will be saved in an Excel file.



##  Future Enhancements

As we envision the next chapters of our License Plate Detector journey, we are setting our sights on a more connected and seamless integration across platforms. Here's a glimpse of what's on our roadmap:

1. **Database Expansion**: With the influx of more user data and detections, it's imperative that our database becomes more robust, scalable, and efficient. We are exploring more advanced database systems that can handle large datasets without compromising speed.

2. **Cloud Integration**: Storing data on local servers has its limitations. To cater to a global audience and ensure accessibility from anywhere, we are keen on integrating cloud storage solutions. This would not only increase storage capacity but also offer better security features.

3. **WhatsApp Bot Integration**: In today's fast-paced world, instant communication is key. Our plan includes developing a WhatsApp bot that would instantly communicate the license plate detection data from the ESP32 camera to the user. This would mean real-time updates right at your fingertips.

4. **ESP32 Camera Enhancements**: The core of our system, the ESP32 camera, is due for some upgrades. We're looking at improving its detection capabilities, and its integration with the aforementioned WhatsApp bot for swift data dissemination.

5. **Secure Data Requests**: Safety is paramount. We're conceptualizing a system where users can securely request specific data captures from the camera, ensuring the privacy and integrity of the information are maintained.

6. **Distributed Data Processing**: By leveraging the power of the cloud, we intend to distribute data processing tasks. This ensures that no single server is overwhelmed, leading to quicker detections and updates.






