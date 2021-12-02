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

The following fps information should appear in console or in ```logfile.txt``` . 

```
2021-12-02 16:12:01,067 [INFO] Press q or esc to exit program.
2021-12-02 16:12:01,068 [INFO] Frame size , width 640 ,height 480.
2021-12-02 16:12:09,017 [INFO] running frame per sec 10.516485489831366
2021-12-02 16:12:13,018 [INFO] running frame per sec 12.49434756648364
2021-12-02 16:12:17,019 [INFO] running frame per sec 12.499466561194788
2021-12-02 16:12:21,019 [INFO] running frame per sec 12.49800579777237
```

Note that typing q or esc on opencv's windows will terminal program.

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

