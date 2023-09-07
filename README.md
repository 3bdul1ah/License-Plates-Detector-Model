# License Plate Detection
<!-- Image 1: Object Detection -->
<p align="center">
  <img src="https://mobisoftinfotech.com/resources/wp-content/uploads/2022/02/Number-Plate-Detection.png" alt="Object Detection" width="40%" style="margin: 10px;">
</p>

<!-- Image 2: ESP32 Camera View -->
<p align="center">
  <img src="https://wicard.net/wp-content/uploads/2023/02/spycam_00.jpg" alt="ESP32 Camera View" width="40%" style="margin: 10px;">
</p>

<!-- Image 3: ESP32 Machine Learning -->
<p align="center">
  <img src="https://i.ytimg.com/vi/WvqJDVjV5Mw/sddefault.jpg" alt="ESP32 Machine Learning" width="40%" style="margin: 10px;">
</p>

<!-- Image 4: Raspberry Pi and ESP32 Server -->
<p align="center">
  <img src="https://external-preview.redd.it/bJqPlZPMEXpe3I0j3n2ufhf1CzIIFTnmZM_OtmUgC0M.png?width=640&crop=smart&format=pjpg&auto=webp&s=ce70f47bda7e9ebc49ec7f5da29174cb07d4ef14" alt="Raspberry Pi and ESP32 Server" width="40%" style="margin: 10px;">
</p>





## Table of Contents
- [Introduction](#introduction)
- [Code Flowchart](#code-flowchart)
- [Dependencies](#dependencies)
- [Functional Overview](#functional-overview)
- [User Guide](#user-guide)
- [Future Enhancements](#future-enhancements)


## Introduction
Welcome to the License Plate Detection Software! Crafted with precision by **Abdullah Alshateri** and **Ahmed Balfiqah**, a third-year Electronic-Telecom Engineering students from UTM.

Harnessing the raw power of the Ultralytics YOLO model, our software can detect license plates in split-second timing using the ESP32-CAM. But it doesn't stop there! With advanced machine learning algorithms, the software dives deep into each detection, deciphering even the tiniest nuances of a license plate. What’s more, it seamlessly integrates these detections into an Excel database, ensuring that data archival is not just efficient but also organized.

Whether you're an enthusiast looking for a reliable license plate recognition solution or a professional seeking robust software for larger systems, our tool is designed to impress and deliver. Dive in and discover our license plate detector!

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


##  Future Enhancements

As we envision the next chapters of our License Plate Detector journey, we are setting our sights on a more connected and seamless integration across platforms. Here's a glimpse of what's on our roadmap:

1. **Database Expansion**: With the influx of more user data and detections, it's imperative that our database becomes more robust, scalable, and efficient. We are exploring more advanced database systems that can handle large datasets without compromising speed.

2. **Cloud Integration**: Storing data on local servers has its limitations. To cater to a global audience and ensure accessibility from anywhere, we are keen on integrating cloud storage solutions. This would not only increase storage capacity but also offer better security features.

3. **WhatsApp Bot Integration**: In today's fast-paced world, instant communication is key. Our plan includes developing a WhatsApp bot that would instantly communicate the license plate detection data from the ESP32 camera to the user. This would mean real-time updates right at your fingertips.

4. **ESP32 Camera Enhancements**: The core of our system, the ESP32 camera, is due for some upgrades. We're looking at improving its detection capabilities, and its integration with the aforementioned WhatsApp bot for swift data dissemination.

5. **Secure Data Requests**: Safety is paramount. We're conceptualizing a system where users can securely request specific data captures from the camera, ensuring the privacy and integrity of the information are maintained.

6. **Distributed Data Processing**: By leveraging the power of the cloud, we intend to distribute data processing tasks. This ensures that no single server is overwhelmed, leading to quicker detections and updates.






