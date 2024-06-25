# Prerequisites
pip install ultralytics

# TODO
use roboflow to anotate a dataset. at least 1000 samples. ideally 2000+

# Results
## Basic yolov8x object detection
![Output video of yolov8x](images\README\20240519_WUL_SFatSD_left_24_clip.webp)

### Extra
Convert gif to webp format. With compression enabled, this cuts the filesize down by ~70%.
`gif2webp` comes from the [webp](https://developers.google.com/speed/webp/docs/gif2webp) package
```
gif2webp.exe -lossy input_clip.gif -o output_clip.webp
```