# License Plate Detection
<p align="center">
  <img src="https://i.postimg.cc/3Rc9Kf3W/Whats-App-Image-2023-09-09-at-13-38-57.jpg" alt="Image 1" width="40%" style="margin: 10px;">
  <img src="https://i.postimg.cc/mDs17QVV/Whats-App-Image-2023-09-09-at-13-34-31.jpg" alt="Image 2" width="40%" style="margin: 10px;">
  <img src="https://i.postimg.cc/jjXvwd4W/ESP32-Cam-Thumbnail.jpg" alt="Image 3" width="40%" style="margin: 10px;">
  <img src=https://i.postimg.cc/mDs17QVV/Whats-App-Image-2023-09-09-at-13-34-31.jpg" alt="Image 4" width="40%" style="margin: 10px;">
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
1. **Clone the repo**
      ```bash
      git clone https://github.com/3bdul1ah/UAE-License-Plates-Detector.git

3. **Navigate to the directory**
      ```bash
      cd UAE-License-Plate-Detector  

3. **Setting up in an IDE**
    Once inside the project directory, open it with your preferred development environment, be it PyCharm, VSCode, or another editor. 
    File to Execute: Locate the `plate-detector.py` script in your editor. Execute this script to start the license plate detection process.

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

## Code Flowchart

### 1. Initialization
- **Load Essential Libraries**: This involves `cv2` for image processing, `numpy` for numerical operations, and more.
  
- **Set Global Variables**: These could be paths, default thresholds, etc.

- **Configure YOLO Model**: Load model weights and set model configurations.

### 2. Image Pre-processing
- **Load Image**: Utilize `cv2` or similar libraries to read the image.

- **Image Rescaling**: Ensure the image meets the size expectations of YOLO.

- **Image Normalization**: Transform pixel values for optimal model interpretation.

- **Image Augmentation**: Apply transformations, if needed, to enhance model accuracy.

### 3. License Plate Detection
- **Invoke YOLO Model**: Process the image through the YOLO neural network.

- **Post-process Outputs**: Filter out detections below a confidence threshold.

- **Draw Bounding Boxes**: Utilize the coordinates to illustrate detected regions.

### 4. License Plate Details Extraction
- **Crop License Plate**: Extract the specific region of interest.

- **Apply OCR**: Tools like Tesseract help in translating image to text.

- **Clean and Validate Text**: Ensure the extracted text matches license plate conventions.

### 5. Data Storage
- **Excel Initialization**: Set up Excel sheets or load existing ones.

- **Data Entry**: Input the detected data in rows/columns.

- **Auto-save Mechanism**: Periodically save data to prevent loss.

### 6. User Interface & Feedback
- **GUI Initialization**: If using a GUI, load up the interface.

- **Display Detected Image**: Provide a visual feedback on what's detected.

- **Interactive Features**: Allow users to manually adjust or confirm detections.

### 7. Cleanup & Finalization
- **Backup Data**: Periodically backup Excel data for safety.

- **Log Activities**: Maintain a log for traceability and debugging.

- **Close Operations**: Tidy up by closing files, releasing memory, and perhaps providing a summary report.

### 8. Exception Handling
- **Custom Error Messages**: For common issues, provide guidance.

- **Error Logging**: For unseen errors, log them for future debugging.

- **Graceful Exit**: Even in error states, ensure the program closes neatly without causing other disruptions.

### 9. Additional Features
- **Updates & Upgrades**: Regularly check for model upgrades or dataset updates.

- **User Customizations**: Allow users to set preferences, like confidence thresholds or specific regions to scan.

- **Extendable Modules**: Design the code such that future features or improvements can be plugged in without major overhauls.


## Dependencies
Ensure the following Python libraries are installed for optimal operation of the License Plate Detection tool:

- `os` Built-in module for OS-level operations.
- `ultralytics` Key for YOLO model integrations.
- `cv2` Utilized for image and video processing tasks.
- `requests` Enables making HTTP requests to fetch images.
- `numpy` Essential for numerical operations.
- `io` Supports core I/O functionalities.
- `matplotlib` For plotting and visualizations.
- `pandas` Handles Excel database operations effectively.

## Functional Overview 

### 1. **ExcelDatabase Class**: 
- **Purpose**: This class is responsible for managing the storage of license plate data in an Excel format. 
- **Database Creation**: It checks for the existence of the database file named 'plates_data.xlsx'. If not found, it intelligently initializes a new database with the required columns.
- **Data Entry**: Offers a `save` method that facilitates the addition of new license plate records to the database.

### 2. **LicensePlateDetector Class**: 
- **Core Operation**: At the heart of this tool, this class utilizes the power of the Ultralytics YOLO model to detect license plates in given images.
- **Data Extraction**: Post-detection, it not only identifies the license plate's region but also deciphers the textual details inscribed, such as the plate number and state.
- **Data Categorization**: Has an intrinsic capability to differentiate between various license plate formats, especially recognizing unique formats from states like 'Sharjah' and 'Abu Dhabi'.
- **Visualization**: An added functionality where the detected license plate on the image can be visualized with a bounding box.

### 3. **Main Workflow**: 
- **Interactive Input**: The script operates in an interactive mode, prompting users to input image URLs.
- **Processing Chain**: For each provided URL, the image undergoes a series of processes: fetching the image, detecting the license plate, deciphering its details, storing the data in the Excel database, and finally, visualizing the detection.
- **Exit Strategy**: The loop continues to process images until the user decides to terminate the session by inputting 'exit'.


##  Future Enhancements

As we envision the next chapters of our License Plate Detector journey, we are setting our sights on a more connected and seamless integration across platforms. Here's a glimpse of what's on our roadmap:

1. **Database Expansion**: With the influx of more user data and detections, it's imperative that our database becomes more robust, scalable, and efficient. We are exploring more advanced database systems that can handle large datasets without compromising speed.

2. **Cloud Integration**: Storing data on local servers has its limitations. To cater to a global audience and ensure accessibility from anywhere, we are keen on integrating cloud storage solutions. This would not only increase storage capacity but also offer better security features.

3. **WhatsApp Bot Integration**: In today's fast-paced world, instant communication is key. Our plan includes developing a WhatsApp bot that would instantly communicate the license plate detection data from the ESP32 camera to the user. This would mean real-time updates right at your fingertips.

4. **ESP32 Camera Enhancements**: The core of our system, the ESP32 camera, is due for some upgrades. We're looking at improving its detection capabilities, and its integration with the aforementioned WhatsApp bot for swift data dissemination.

5. **Secure Data Requests**: Safety is paramount. We're conceptualizing a system where users can securely request specific data captures from the camera, ensuring the privacy and integrity of the information are maintained.

6. **Distributed Data Processing**: By leveraging the power of the cloud, we intend to distribute data processing tasks. This ensures that no single server is overwhelmed, leading to quicker detections and updates.






