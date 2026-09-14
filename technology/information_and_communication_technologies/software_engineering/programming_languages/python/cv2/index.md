# OpenCV (`cv2`)

## 1. Overview

**OpenCV (Open Source Computer Vision Library)** is an open-source computer-vision and machine-learning library exposed to Python through the `cv2` module.

It provides APIs for:

- Image and video I/O
- Image manipulation and geometric transformations
- Filtering, enhancement, thresholding, and segmentation
- Edge, corner, blob, and feature detection
- Feature descriptors and image matching
- Object detection
- Camera calibration and 3D reconstruction
- Video capture, processing, and tracking
- Computational photography
- Image stitching and panorama generation
- Deep-neural-network inference through `cv2.dnn`
- Classical machine-learning algorithms
- GUI/display utilities
- Hardware-accelerated computer vision on supported builds

OpenCV's current documentation organizes functionality into modules including `core`, `imgproc`, `imgcodecs`, `videoio`, `highgui`, `video`, `calib3d`, `features2d`, `objdetect`, `dnn`, `ml`, `flann`, `photo`, `stitching`, and `gapi`.

---

## 2. Installation

For a normal Python environment:

```bash
python -m pip install opencv-python
```

For OpenCV's additional/contrib modules:

```bash
python -m pip install opencv-contrib-python
```

Verify the installation:

```python
import cv2

print(cv2.__version__)
```

### `opencv-python` vs `opencv-contrib-python`

Use:

- `opencv-python` for the standard OpenCV distribution.
- `opencv-contrib-python` when you need functionality shipped in the extra/contrib modules.

Avoid installing multiple OpenCV wheel variants into the same environment unless you have a specific reason. They can conflict because they expose the same `cv2` Python module.

---

## 3. The OpenCV Data Model

A fundamental concept for Python developers is that an OpenCV image is normally represented as a **NumPy array**.

```python
import cv2

image = cv2.imread("input.jpg")

print(type(image))
print(image.shape)
print(image.dtype)
```

Typical output:

```text
<class 'numpy.ndarray'>
(1080, 1920, 3)
uint8
```

For a color image, the three channels are normally:

```text
BGR
```

not RGB.

Therefore:

```python
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

is required when passing an OpenCV image to code that expects RGB ordering, such as many plotting or ML libraries.

---

## 4. Major Capabilities

### 4.1 Image I/O

OpenCV can read and write many common image formats.

```python
import cv2

image = cv2.imread("input.jpg")

if image is None:
    raise RuntimeError("Could not load image")

cv2.imwrite("output.png", image)
```

Useful functions:

| Function | Purpose |
|---|---|
| `cv2.imread()` | Read image |
| `cv2.imwrite()` | Write image |
| `cv2.imdecode()` | Decode image from memory |
| `cv2.imencode()` | Encode image into memory |

Memory-based encoding is particularly useful in APIs where files arrive as bytes rather than filesystem paths.

Example:

```python
import cv2
import numpy as np

data = open("input.jpg", "rb").read()

buffer = np.frombuffer(data, dtype=np.uint8)
image = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

if image is None:
    raise ValueError("Invalid image")

ok, encoded = cv2.imencode(".jpg", image)

if not ok:
    raise RuntimeError("Encoding failed")

jpeg_bytes = encoded.tobytes()
```

This is useful in FastAPI/Flask services because the image does not need to be written to disk.

---

## 5. Image Manipulation

### 5.1 Resize

```python
resized = cv2.resize(
    image,
    (1280, 720),
    interpolation=cv2.INTER_AREA,
)
```

For shrinking an image, `INTER_AREA` is commonly a good choice.

For enlarging:

```python
resized = cv2.resize(
    image,
    None,
    fx=2.0,
    fy=2.0,
    interpolation=cv2.INTER_CUBIC,
)
```

---

### 5.2 Crop

Because an OpenCV image is a NumPy array:

```python
crop = image[y1:y2, x1:x2]
```

Example:

```python
crop = image[100:500, 200:800]
```

The order is:

```text
image[y, x]
```

not:

```text
image[x, y]
```

---

### 5.3 Rotate

```python
rotated = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE,
)
```

For arbitrary angles, use an affine transformation matrix:

```python
height, width = image.shape[:2]

center = (width // 2, height // 2)

matrix = cv2.getRotationMatrix2D(
    center,
    30,
    1.0,
)

rotated = cv2.warpAffine(
    image,
    matrix,
    (width, height),
)
```

---

## 6. Drawing and Annotation

OpenCV can draw directly onto images.

```python
cv2.line(
    image,
    (10, 10),
    (300, 300),
    (255, 0, 0),
    3,
)

cv2.rectangle(
    image,
    (100, 100),
    (500, 400),
    (0, 255, 0),
    2,
)

cv2.circle(
    image,
    (300, 300),
    50,
    (0, 0, 255),
    3,
)

cv2.putText(
    image,
    "Detected object",
    (100, 90),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,
    (255, 255, 255),
    2,
)
```

This is useful for:

- Debugging computer-vision pipelines
- Drawing bounding boxes
- Displaying tracking information
- Producing annotated evidence images
- Visualizing detection results

---

## 7. Color-Space Conversion

OpenCV supports many color-space transformations.

Common examples:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

#### Why HSV is useful

HSV separates:

- Hue
- Saturation
- Value

This makes it useful for color-based segmentation.

Example: detect a range of colors.

```python
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([35, 80, 50])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(
    image,
    image,
    mask=mask,
)
```

---

## 8. Image Filtering

Filtering is commonly used for noise reduction and preprocessing.

### Gaussian blur

```python
blurred = cv2.GaussianBlur(
    image,
    (5, 5),
    0,
)
```

### Median filtering

```python
filtered = cv2.medianBlur(
    image,
    5,
)
```

Median filtering is particularly useful for salt-and-pepper noise.

### Bilateral filtering

```python
filtered = cv2.bilateralFilter(
    image,
    9,
    75,
    75,
)
```

Bilateral filtering attempts to smooth an image while preserving edges.

---

## 9. Thresholding and Segmentation

### Binary threshold

```python
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY,
)
```

### Adaptive threshold

```python
binary = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2,
)
```

Useful when lighting is not uniform.

---

## 10. Morphological Operations

Morphological operations operate primarily on binary masks.

Common operations:

- Erosion
- Dilation
- Opening
- Closing
- Morphological gradient

Example:

```python
kernel = np.ones((5, 5), np.uint8)

opened = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel,
)

closed = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel,
)
```

These are frequently used to remove small artifacts or close gaps in segmentation masks.

---

## 11. Edge Detection

OpenCV provides edge-detection algorithms including Canny.

```python
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

blurred = cv2.GaussianBlur(
    gray,
    (5, 5),
    0,
)

edges = cv2.Canny(
    blurred,
    50,
    150,
)
```

Typical pipeline:

```text
Image
  |
  v
Grayscale
  |
  v
Noise reduction
  |
  v
Canny
  |
  v
Edge map
```

Edges can then be processed with contours, Hough transforms, or geometric analysis.

---

## 12. Contour Detection

Contours are useful when analyzing shapes and connected regions.

```python
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE,
)

for contour in contours:
    area = cv2.contourArea(contour)

    if area < 500:
        continue

    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2,
    )
```

Applications include:

- Shape detection
- Document boundary detection
- Component inspection
- Blob analysis
- Object segmentation

---

## 13. Geometric Shape Analysis

OpenCV provides functions for calculating geometric properties.

Examples:

```python
area = cv2.contourArea(contour)

perimeter = cv2.arcLength(
    contour,
    True,
)

approx = cv2.approxPolyDP(
    contour,
    0.02 * perimeter,
    True,
)
```

A rectangle-like object can be detected by checking whether the approximated contour has four vertices.

---

## 14. Feature Detection

OpenCV provides a feature-detection framework with algorithms such as:

- Harris corners
- Shi-Tomasi
- FAST
- SIFT
- ORB
- AKAZE

These features can be used for:

- Image matching
- Object recognition
- Image registration
- Panorama generation
- Camera tracking
- Visual localization

---

### 14.1 ORB PoC

ORB is useful when you need a relatively fast feature detector/descriptor.

```python
import cv2

image = cv2.imread("image.jpg")

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

orb = cv2.ORB_create(
    nfeatures=1000,
)

keypoints, descriptors = orb.detectAndCompute(
    gray,
    None,
)

output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
)

cv2.imwrite(
    "orb_features.jpg",
    output,
)

print("Keypoints:", len(keypoints))

if descriptors is not None:
    print("Descriptor shape:", descriptors.shape)
```

---

### 14.2 SIFT PoC

SIFT provides scale- and rotation-invariant local features.

```python
import cv2

image = cv2.imread("image.jpg")

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(
    gray,
    None,
)

output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
)

cv2.imwrite(
    "sift_features.jpg",
    output,
)

print("Keypoints:", len(keypoints))
```

---

## 15. Feature Matching

Once descriptors are extracted from two images, OpenCV can match them.

For binary descriptors such as ORB:

```python
orb = cv2.ORB_create(nfeatures=1000)

kp1, des1 = orb.detectAndCompute(
    image1,
    None,
)

kp2, des2 = orb.detectAndCompute(
    image2,
    None,
)

matcher = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True,
)

matches = matcher.match(
    des1,
    des2,
)

matches = sorted(
    matches,
    key=lambda m: m.distance,
)

result = cv2.drawMatches(
    image1,
    kp1,
    image2,
    kp2,
    matches[:50],
    None,
)

cv2.imwrite(
    "matches.jpg",
    result,
)
```

For floating-point descriptors such as SIFT, a different distance metric such as `NORM_L2` is appropriate.

---

## 16. Homography and Image Alignment

Feature matching can be combined with homography estimation.

Typical workflow:

```text
Image A
   |
Feature detection
   |
Descriptors
   |
Feature matching
   |
Matched points
   |
Homography estimation
   |
Perspective transformation
   |
Aligned image
```

Example:

```python
import cv2
import numpy as np

## src_pts and dst_pts are matched point coordinates.
H, mask = cv2.findHomography(
    src_pts,
    dst_pts,
    cv2.RANSAC,
    5.0,
)

height, width = image2.shape[:2]

aligned = cv2.warpPerspective(
    image1,
    H,
    (width, height),
)
```

This is useful for:

- Document alignment
- Object localization
- Image registration
- Panorama construction
- AR-style overlays

---

## 17. Video Processing

OpenCV can capture frames from:

- USB/web cameras
- Video files
- Network streams, depending on the available backend/build

Basic camera loop:

```python
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open camera")

while True:
    ok, frame = cap.read()

    if not ok:
        break

    cv2.imshow(
        "Camera",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 18. Video Processing PoC — Edge Detector

A useful first real-time PoC is a live Canny edge detector.

```python
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open camera")

while True:
    ok, frame = cap.read()

    if not ok:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY,
    )

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0,
    )

    edges = cv2.Canny(
        blurred,
        50,
        150,
    )

    cv2.imshow(
        "Original",
        frame,
    )

    cv2.imshow(
        "Edges",
        edges,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

This demonstrates the basic OpenCV real-time processing model:

```text
Capture
   ↓
Decode frame
   ↓
Transform
   ↓
Process
   ↓
Display / store / transmit
   ↓
Next frame
```

---

## 19. Video Writing

Frames can be written to a video file.

```python
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Camera unavailable")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30.0

fourcc = cv2.VideoWriter_fourcc(
    *"mp4v"
)

writer = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (width, height),
)

try:
    while True:
        ok, frame = cap.read()

        if not ok:
            break

        writer.write(frame)

        cv2.imshow(
            "Recording",
            frame,
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    writer.release()
    cv2.destroyAllWindows()
```

Codec/container compatibility depends on the OpenCV build and the video backend installed on the system.

---

## 20. Object Tracking

OpenCV contains tracking functionality and can also be combined with detection algorithms.

Conceptually:

```text
Detector
   |
   v
Object bounding box
   |
   v
Tracker
   |
   +---- frame N+1
   |
   +---- frame N+2
   |
   +---- frame N+3
```

Tracking can reduce the need to run an expensive detector on every frame.

A production system might therefore use:

```text
Periodic detection
       +
Continuous tracking
```

rather than:

```text
Detection on every frame
```

---

## 21. Object Detection

OpenCV supports traditional object-detection approaches and modern neural-network inference.

The `objdetect` module contains object-detection functionality.

Examples of tasks:

- Face detection
- QR/barcode detection
- Object localization
- Cascade-based detection

For modern neural networks, `cv2.dnn` is generally the more flexible interface.

---

## 22. Deep Neural Networks with `cv2.dnn`

OpenCV's DNN module can perform inference using supported neural-network model formats.

A common workflow is:

```text
Pre-trained model
       |
       v
cv2.dnn.readNet(...)
       |
       v
cv2.dnn.blobFromImage(...)
       |
       v
net.setInput(...)
       |
       v
net.forward(...)
       |
       v
Post-processing
```

Example skeleton:

```python
import cv2

net = cv2.dnn.readNetFromONNX(
    "model.onnx"
)

image = cv2.imread(
    "input.jpg"
)

blob = cv2.dnn.blobFromImage(
    image,
    scalefactor=1 / 255.0,
    size=(640, 640),
    swapRB=True,
    crop=False,
)

net.setInput(blob)

output = net.forward()

print(output.shape)
```

The exact preprocessing and postprocessing are **model-specific**. A model cannot be used correctly merely by loading it into `cv2.dnn`; its expected input dimensions, channel order, normalization, output tensors, and decoding logic must be respected.

---

## 23. Camera Calibration

The `calib3d` module supports camera calibration and 3D reconstruction workflows.

Typical calibration pipeline:

```text
Calibration images
       |
       v
Detect calibration pattern
       |
       v
Image points
       +
Known 3D object points
       |
       v
cv2.calibrateCamera()
       |
       v
Camera matrix
Distortion coefficients
       |
       v
Undistortion / 3D geometry
```

Example skeleton:

```python
import cv2
import numpy as np

ret, camera_matrix, distortion, rvecs, tvecs = (
    cv2.calibrateCamera(
        object_points,
        image_points,
        image_size,
        None,
        None,
    )
)

print("Camera matrix:")
print(camera_matrix)

print("Distortion:")
print(distortion)
```

Calibration is important when image coordinates need to be related accurately to the physical camera and scene.

---

## 24. Stereo Vision and 3D Reconstruction

OpenCV can support stereo-vision pipelines.

Typical architecture:

```text
Left camera ─────┐
                 ├──> Calibration
Right camera ────┘
                      |
                      v
                 Rectification
                      |
                      v
                Stereo matching
                      |
                      v
                  Disparity
                      |
                      v
                Depth / 3D data
```

This enables applications such as:

- Depth estimation
- 3D reconstruction
- Robotics
- Measurement
- Spatial mapping

---

## 25. Image Stitching

OpenCV provides a stitching module for combining multiple images into panoramas.

Conceptually:

```text
Image 1 ─┐
Image 2 ─┼──> Feature matching
Image 3 ─┘          |
                    v
               Alignment
                    |
                    v
               Blending
                    |
                    v
                Panorama
```

For simple cases:

```python
import cv2

images = [
    cv2.imread("left.jpg"),
    cv2.imread("center.jpg"),
    cv2.imread("right.jpg"),
]

stitcher = cv2.Stitcher_create()

status, panorama = stitcher.stitch(
    images
)

if status != cv2.Stitcher_OK:
    raise RuntimeError(
        f"Stitching failed: {status}"
    )

cv2.imwrite(
    "panorama.jpg",
    panorama,
)
```

---

## 26. QR Codes and Barcodes

OpenCV includes QR-code detection functionality.

Example:

```python
import cv2

image = cv2.imread("qr.png")

detector = cv2.QRCodeDetector()

data, points, _ = detector.detectAndDecode(
    image
)

if points is not None:
    print("QR detected")
    print("Data:", data)
else:
    print("No QR code detected")
```

For production barcode/QR systems, compare OpenCV's capabilities with specialized barcode libraries depending on the required symbologies and reliability requirements.

---

## 27. Computational Photography

The `photo` module provides functionality useful for computational photography.

Areas include:

- Image denoising
- HDR-related workflows
- Tone mapping
- Inpainting
- Exposure fusion

Example: image inpainting.

```python
import cv2

image = cv2.imread("damaged.jpg")
mask = cv2.imread(
    "mask.png",
    cv2.IMREAD_GRAYSCALE,
)

restored = cv2.inpaint(
    image,
    mask,
    3,
    cv2.INPAINT_TELEA,
)

cv2.imwrite(
    "restored.jpg",
    restored,
)
```

---

## 28. Machine Learning

OpenCV also includes a classical ML module.

Depending on the version/build, algorithms include functionality for tasks such as:

- K-means clustering
- Decision trees
- Random trees
- Support vector machines
- K-nearest neighbors
- Naive Bayes
- Boosting

Example SVM skeleton:

```python
import cv2
import numpy as np

samples = np.array([
    [1, 2],
    [2, 3],
    [8, 9],
    [9, 10],
], dtype=np.float32)

labels = np.array([
    0,
    0,
    1,
    1,
], dtype=np.int32)

model = cv2.ml.SVM_create()

model.setType(cv2.ml.SVM_C_SVC)
model.setKernel(cv2.ml.SVM_LINEAR)
model.setC(1.0)

model.train(
    samples,
    cv2.ml.ROW_SAMPLE,
    labels,
)

_, prediction = model.predict(
    np.array([[3, 4]], dtype=np.float32)
)

print("Prediction:", prediction)
```

For deep learning, however, modern projects will often use PyTorch or TensorFlow for training and OpenCV primarily for preprocessing, inference integration, image/video handling, or deployment-oriented computer-vision operations.

---

## 29. GUI and Debugging

OpenCV provides simple GUI functionality.

```python
cv2.imshow(
    "Preview",
    image,
)

key = cv2.waitKey(0)

cv2.destroyAllWindows()
```

Trackbars can be useful for interactively tuning thresholds.

Example:

```python
def nothing(value):
    pass


cv2.namedWindow("Controls")

cv2.createTrackbar(
    "Threshold",
    "Controls",
    127,
    255,
    nothing,
)
```

For server-side applications, do not rely on OpenCV GUI functions. Headless/server environments commonly need a non-GUI workflow.

---

## 30. A Practical Computer-Vision Pipeline

A typical application can be decomposed as:

```text
                 ┌───────────────────┐
                 │ Image / Camera /  │
                 │ Video / Network   │
                 └─────────┬─────────┘
                           │
                           v
                 ┌───────────────────┐
                 │ Decode / Capture  │
                 └─────────┬─────────┘
                           │
                           v
                 ┌───────────────────┐
                 │ Pre-processing    │
                 │ resize / denoise  │
                 │ color conversion  │
                 └─────────┬─────────┘
                           │
                           v
                 ┌───────────────────┐
                 │ Computer Vision   │
                 │ detection /       │
                 │ segmentation /    │
                 │ features / etc.   │
                 └─────────┬─────────┘
                           │
                           v
                 ┌───────────────────┐
                 │ Post-processing   │
                 │ filtering /       │
                 │ tracking /        │
                 │ geometry          │
                 └─────────┬─────────┘
                           │
                           v
                 ┌───────────────────┐
                 │ Application       │
                 │ decision / API /  │
                 │ storage / UI      │
                 └───────────────────┘
```

---

## 31. Developer PoC: Image Processing Service

OpenCV works well as a processing component inside a Python API.

Example FastAPI endpoint:

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

import cv2
import numpy as np


app = FastAPI()


@app.post("/edges")
async def detect_edges(
    file: UploadFile = File(...)
):
    data = await file.read()

    buffer = np.frombuffer(
        data,
        dtype=np.uint8,
    )

    image = cv2.imdecode(
        buffer,
        cv2.IMREAD_COLOR,
    )

    if image is None:
        return {
            "error": "Invalid image"
        }

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )

    edges = cv2.Canny(
        gray,
        50,
        150,
    )

    ok, encoded = cv2.imencode(
        ".png",
        edges,
    )

    if not ok:
        return {
            "error": "Encoding failed"
        }

    return Response(
        content=encoded.tobytes(),
        media_type="image/png",
    )
```

Run:

```bash
uvicorn app:app --reload
```

This gives a basic architecture:

```text
HTTP client
    |
    v
FastAPI
    |
    v
OpenCV
    |
    v
NumPy
    |
    v
Encoded image response
```

No intermediate image file is required.

---

## 32. Developer PoC: Real-Time Object Processing

For a real-time video application, keep the processing loop separate from the application/API layer.

Recommended architecture:

```text
Camera / RTSP / Video
          |
          v
     Frame Capture
          |
          v
     Frame Queue
          |
          v
  OpenCV Processing
          |
     ┌────┴────┐
     v         v
 Detection   Tracking
     |         |
     └────┬────┘
          v
   Application Logic
          |
     ┌────┴─────┐
     v          v
  Storage     Client
```

This allows the capture rate, processing rate, and output rate to be managed independently.

For higher-throughput systems, use bounded queues and explicit backpressure/drop policies rather than allowing unbounded frame accumulation.

---

## 33. Performance Considerations

### Avoid unnecessary copies

NumPy/OpenCV operations can become expensive when large frames are repeatedly copied.

Prefer operations that reuse buffers where practical.

### Resize early

If the source is 4K but the algorithm only needs 640×640 input:

```text
4K frame
   |
resize
   |
640x640
   |
processing
```

is often substantially cheaper than processing the full-resolution image.

### Avoid processing every frame when unnecessary

For video:

```text
30 FPS input
```

does not necessarily mean:

```text
30 expensive neural-network inferences/sec
```

Possible strategies:

- Run detection every N frames.
- Track between detections.
- Downsample frames.
- Crop to regions of interest.
- Batch frames when latency permits.
- Use hardware acceleration when available.

### Profile the complete pipeline

Measure:

```text
capture time
decode time
preprocessing
inference
postprocessing
encoding
I/O
```

rather than optimizing only the OpenCV call that appears expensive.

---

## 34. Threading and Multiprocessing

Python applications using OpenCV often combine:

- Threaded capture
- Processing workers
- Queue-based pipelines
- Multiprocessing for CPU-heavy Python workloads

A basic queue architecture:

```python
from queue import Queue
from threading import Thread

frame_queue = Queue(maxsize=5)
```

The queue should generally be bounded for real-time applications. If processing falls behind capture, retaining every historical frame can increase latency dramatically.

For real-time vision, **freshness is often more important than completeness**.

A useful policy can be:

```text
If queue is full:
    drop an old frame
    process the newest frame
```

rather than processing stale frames seconds after capture.

---

## 35. Hardware Acceleration

OpenCV can use optimized CPU implementations and, depending on how it was built, hardware acceleration facilities.

Relevant areas include:

- SIMD CPU optimizations
- OpenCL
- CUDA-related functionality
- Hardware-specific inference backends

Check the actual build configuration:

```python
import cv2

print(cv2.getBuildInformation())
```

Do not assume that installing an OpenCV Python package automatically means CUDA acceleration is available.

The actual build configuration determines what backends and accelerators are usable.

---

## 36. Common Pitfalls

### 36.1 BGR vs RGB

OpenCV normally uses BGR:

```python
image = cv2.imread("image.jpg")
```

Many Python ML/visualization libraries expect RGB.

Convert explicitly:

```python
rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB,
)
```

---

### 36.2 `VideoCapture.read()` can fail

Always check:

```python
ok, frame = cap.read()

if not ok:
    ## Handle camera disconnect,
    ## end-of-file, backend failure, etc.
    ...
```

---

### 36.3 FPS metadata may be unreliable

For some cameras or video streams:

```python
fps = cap.get(cv2.CAP_PROP_FPS)
```

may return zero or an inaccurate value.

Do not blindly trust it for timing-sensitive applications.

---

### 36.4 Codec support depends on the environment

A script working on one machine may fail to encode/decode a particular video format on another because OpenCV's video I/O backend and codec availability differ.

Inspect:

```python
print(cv2.getBuildInformation())
```

when diagnosing video I/O problems.

---

### 36.5 GUI calls fail in headless environments

This:

```python
cv2.imshow(...)
```

is not appropriate for many:

- Docker containers
- cloud servers
- CI environments
- backend services

For those environments, process frames and write/return them instead.

---

## 37. Recommended Project Structure

For a medium-sized computer-vision service:

```text
vision_app/
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── capture.py
│   ├── preprocessing.py
│   ├── detection.py
│   ├── tracking.py
│   ├── postprocessing.py
│   ├── models.py
│   └── config.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_detection.py
│   └── test_api.py
│
├── models/
│   └── model.onnx
│
├── scripts/
│   └── camera_test.py
│
├── requirements.txt
└── README.md
```

Keep model-specific code separate from generic image-processing utilities.

---

## 38. Capability Map

| Area | Representative APIs | Typical Use |
|---|---|---|
| Image I/O | `imread`, `imwrite`, `imdecode`, `imencode` | Image services |
| Array operations | NumPy + OpenCV | Pixel manipulation |
| Color conversion | `cvtColor` | Preprocessing |
| Resize/warp | `resize`, `warpAffine`, `warpPerspective` | Geometric normalization |
| Filtering | `GaussianBlur`, `medianBlur`, `bilateralFilter` | Noise reduction |
| Thresholding | `threshold`, `adaptiveThreshold` | Segmentation |
| Morphology | `morphologyEx` | Mask cleanup |
| Edges | `Canny` | Edge extraction |
| Contours | `findContours` | Shape analysis |
| Features | SIFT, ORB, AKAZE | Matching/local features |
| Matching | BFMatcher, FLANN | Image correspondence |
| Video | `VideoCapture`, `VideoWriter` | Camera/video processing |
| Detection | `objdetect` | Traditional detection |
| DNN | `cv2.dnn` | Neural-network inference |
| Calibration | `calib3d` | Camera geometry |
| Stereo | `calib3d` | Depth/3D |
| Stitching | `stitching` | Panoramas |
| Photography | `photo` | HDR/denoise/inpainting |
| Classical ML | `ml` | Traditional ML |
| GUI | `highgui` | Local visualization |
| Acceleration | CUDA/OpenCL/backends | Performance |

---

## 39. Where OpenCV Fits in a Modern Python Stack

OpenCV is best viewed as a **computer-vision and image/video processing engine**, not necessarily as the complete AI stack.

A practical modern architecture might be:

```text
                  Python Application
                         |
             ┌───────────┴───────────┐
             |                       |
          FastAPI                 Worker
             |                       |
             └───────────┬───────────┘
                         |
                       OpenCV
                         |
          ┌──────────────┼──────────────┐
          |              |              |
        NumPy          cv2.dnn       Video I/O
          |              |              |
          |           ONNX model        |
          |                             |
          └──────────────┬──────────────┘
                         |
                    Application
                     decision
```

Common complementary technologies:

- **NumPy** — numerical/image-array operations
- **PyTorch** — model development and training
- **ONNX** — model interchange/deployment
- **FastAPI** — serving computer-vision functionality
- **FFmpeg/GStreamer** — advanced media pipelines
- **Pillow** — general-purpose image manipulation
- **scikit-image** — additional scientific image processing

---

## 40. Suggested PoC Progression

For a developer learning OpenCV, the following sequence gives a useful progression.

#### PoC 1 — Image manipulation

Implement:

```text
load → resize → grayscale → save
```

#### PoC 2 — Segmentation

Implement:

```text
load → HSV → threshold → morphology → contours
```

#### PoC 3 — Real-time processing

Implement:

```text
camera → grayscale → blur → Canny → display
```

#### PoC 4 — Object/feature matching

Implement:

```text
two images → ORB/SIFT → descriptors → matcher → visualization
```

#### PoC 5 — Camera geometry

Implement:

```text
checkerboard → calibration → distortion correction
```

#### PoC 6 — Neural-network inference

Implement:

```text
image → blob → cv2.dnn → ONNX model → detections
```

#### PoC 7 — Production API

Implement:

```text
FastAPI
   ↓
Upload/stream
   ↓
OpenCV preprocessing
   ↓
DNN inference
   ↓
postprocessing
   ↓
JSON / image / video result
```

---

## 41. Quick Reference

```python
import cv2
import numpy as np

## Read
image = cv2.imread("image.jpg")

## Color conversion
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

## Resize
small = cv2.resize(
    image,
    (640, 480),
)

## Blur
blurred = cv2.GaussianBlur(
    image,
    (5, 5),
    0,
)

## Threshold
_, mask = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY,
)

## Edges
edges = cv2.Canny(
    gray,
    50,
    150,
)

## Contours
contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE,
)

## Camera
cap = cv2.VideoCapture(0)

## DNN
net = cv2.dnn.readNetFromONNX(
    "model.onnx"
)

## Save
cv2.imwrite(
    "output.png",
    image,
)
```

---

## 42. Key Takeaways

1. `cv2` is the Python interface to OpenCV.
2. OpenCV images are normally NumPy arrays.
3. OpenCV uses **BGR** channel ordering by default for color images.
4. OpenCV covers both low-level image processing and higher-level computer-vision workflows.
5. `VideoCapture` and `VideoWriter` provide the foundation for camera/video processing.
6. `imgproc` contains many of the fundamental preprocessing and segmentation operations.
7. `features2d` provides feature detection, description, and matching.
8. `calib3d` supports camera calibration, stereo, and 3D reconstruction workflows.
9. `cv2.dnn` can perform neural-network inference without requiring the entire model-development stack.
10. For production systems, treat capture, preprocessing, inference, postprocessing, and output as separate pipeline stages.
11. Profile the entire pipeline rather than individual OpenCV functions in isolation.
12. Verify the actual OpenCV build when relying on video backends or hardware acceleration.

---

## 43. Official References

- OpenCV Tutorials: https://docs.opencv.org/4.12.0/d9/df8/tutorial_root.html
- OpenCV-Python Tutorials: https://docs.opencv.org/trunk/d6/d00/tutorial_py_root.html
- OpenCV modules: https://docs.opencv.org/4.10.0/
- OpenCV feature detection documentation: https://opencv-opencv.mintlify.app/tutorials/feature-detection
- OpenCV video-processing documentation: https://opencv-opencv.mintlify.app/tutorials/video-processing
- OpenCV DNN documentation/wiki: https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV