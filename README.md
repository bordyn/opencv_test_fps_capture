# opencv_test_fps_capture
This repository aims for testing opencv's video capture capability on camera device.

## Setup

1. Create venv on this directory

```bash
python3 -m virtualenv venv
```

2. Activate virtual environments

```bash
# Linux    
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Install requirements

```bash
(venv)python -m pip install -r requirements.txt
```

## Running
Running on video device 0 

```bash
# Linux    
(venv)python capture.py --video=/dev/video0

# Windows
(venv)python capture.py --video=0
```

## PyInstalling (Windows)

```bash
(venv)python pyinstalling.py
```

The executable should be in __gen/dist folder with run.bat file.
Run run.bat file or type the following command in dist folder to test the pyinstalling executable result.

```bash
bin\capture --video=0
```

Note that you can edit ```--video```  argument to suite your camera index (e,g 0,1,2).

