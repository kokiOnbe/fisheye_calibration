# Monocular Calibration

## Dependencies
- Python 3.x
- Open CV
- Boost

## Build
```
mkdir build
cd build
cmake ..
make -j
```

## Preparation
make calibration image list file
```
python imList_create.py <outputName> <path/to/image>
```
You create setting file like ``calib_setting.xml``.

## Run
```
./calibration <path/to/calib_setting.xml>
```
