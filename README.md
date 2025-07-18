# License Plate Detection
<p align="center">
    <img src="https://i.ytimg.com/vi/ZeLg5rxLGLg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDMiHxm_6Tdby6DNjyr-vZRRLZ8lQ">
    <img src="https://i.postimg.cc/3Rc9Kf3W/Whats-App-Image-2023-09-09-at-13-38-57.jpg" alt="Image 1" width="40%" style="margin: 10px;">
    <img src="https://i.postimg.cc/mDs17QVV/Whats-App-Image-2023-09-09-at-13-34-31.jpg" alt="Image 2" width="40%" style="margin: 10px;">
    
</p>



## Introduction

Welcome to the License Plate Detection Software, meticulously crafted by **Abdullah Alshateri**, **Ahmed Assagaf** and **Ahmed Balfiqah**, all third-year Electrical Engineering students at UTM, during their internship in Smart Navigation System in the UAE.

Our software leverages the formidable capabilities of the Ultralytics **YOLOv8 model** to deliver lightning-fast license plate detection using the ESP32-CAM. But we don't stop at mere detection! With advanced **machine learning algorithms**, the software delves deep into each detection, deciphering even the tiniest nuances of a license plate. Moreover, it seamlessly integrates these detections into an Excel database, ensuring that data archival is not just efficient but also organized.

Whether you're an enthusiast looking for a reliable license plate recognition solution or a professional seeking robust software for larger systems, our tool is designed to impress and deliver. Dive in and discover our license plate detector!

> **License Plate Detection Model Update (2023-09-06):**
> 
> - **Stability:** The system is now in a stable state.
> 
> - **Accuracy:** Its detection accuracy is outstanding, exceeding 90%. Failures are rare.
> 
> - **Output Details:** The model can discern and provide:
>    - Plate category ✅
>    - Plate number ✅
>    - Plate state ✅
> 
> The model’s detection ability is parallel to human eyesight:
>   - If it recognizes a plate, it captures it with high precision.
>   - When the model cannot detect a plate, it will clearly mention that no plate could be detected.

## Table of Contents
- [System Flow](#system-flow)
- [Dependencies](#dependencies)
- [User Guide](#user-guide)
- [Updating the Repository](#updating-the-repository)



> **Tips to avoid problems:**
> 1. Ensure all dependencies are installed.
> 2. Clone the repository.
> 3. Run the `plate-detector.py` Python script.
> 4. Input image URLs when prompted.
> 5. View the detected license plates and their details.
> 6. All detected details will be saved in an Excel file.


## Dependencies
**Before running this project, make sure to install the following Python dependencies:**

> - ### `os`: For OS-level operations.
>   ```
>   pip install os
>   ```

> - ### `ultralytics`: Used for YOLO model integrations.
>   ```
>   pip install ultralytics
>   ```

> - ### `cv2`: Image and video processing tasks.
>   ```
>   pip install opencv-python
>   ```

> - ### `requests`: To fetch images from URLs.
>   ```
>   pip install requests
>   ```

> - ### `numpy`: Numerical operations.
>   ```
>   pip install numpy
>   ```

> - ### `io`: Core I/O functionalities.
>   ```
>   pip install io
>   ```

> - ### `matplotlib`: Display images.
>   ```
>   pip install matplotlib
>   ```

> - ### `pandas`: Manage Excel operations effectively.
>   ```
>   pip install pandas
>   ```

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


#Feture updates for the project:

- **Updating the AI model**: Using yolov11 for better results.
- **Creating a smaller model**: Using tiny model instead of nano for more enhanced results when raspberry pi is used.  








