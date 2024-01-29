# Computer Vision

Major applications : 

1. Snapchat and Instagram filters
2. Optical Character Recognition
    - License Plate Reading
4. Self driving cars
5. Sporting Analysis
6. Facial Recognition

Major applications within CV at the time has been with : 

1. Image Recognition
2. Object Detection
3. Segementation
4. AI Art
5. Image Similarity
6. Deep Fakes
7. Body Pose Detection
8. Image Generation

Libraries : 

1. OpenCV
2. TensorFlow
3. Keras
4. Theano
5. Caffe
6. CUDA

CV with Deep Learning vs Classical : 

| Deep Learning                                               | Classical                                           |
| ----------------------------------------------------------- | --------------------------------------------------- |
| Adapts to new images well(assuming trained on similar data) | Small changes can have big negative impacts         |
| Requires Models to be trained                               | Doesn't require training and can be used once coded |
| Model weights learn to adapt to varying image conditions    | Relies on hardcoded features and parameters         |
| Requires GPU hardware(most times)                           | Can be run on CPU                                   |

Image types : 
1. Raster Images
2. Vector Images

CV2 operations : 

1. Rotations
    - `cv2.getRotationMatrix2D(center=center, angle=45, scale=1)`
    - `cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))`
    - `transpose`
2. Scaling
3. Resizing
4. Cropping
5. Arithematic and Bitwise operations
6. Convolutions(function overlapping another, to produce a function similar to 1 of them)
7. Blurring
    - Gaussian Blur - `cv2.GaussianBlur(image, kernel, offset)`
    - Median Blur - `cv2.medianBlur(image, blurKernelSize)`
    - Normalized Blur - `cv2.blur(src, ksize[, dst[, anchor[, borderType]]])`
9. Sharpening(occurs using negative kernel values in the filter matrix)
10. Thresholding(uses `cv2.threshold(image, lower_value, upper_value, threshold_type)`)
    1.  Binary threshold `cv2.THRESH_BINARY`
    2.  Inverse Binary `cv2.THRESH_BINARY_INV`
    3.  Truncate `cv2.THRESH_TRUNC`
    4.  To Zero `cv2.THRESH_TOZERO`
    5.  To Zero Inverse `cv2.THRESH_TOZERO_INV`
11. Adaptive Thresholding(uses `cv2.adaptiveThreshold(src, dst, maxVal, adaptiveMethod, thresholdType, blockSize, constant)`)
    1.  Adaptive Thresholding using Means and C `cv2.ADAPTIVE_THRESH_MEAN_C`
    2.  Adaptive Thresholding using Gaussian `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`
    3.  Otsu's Binarization(Determines threshold value automatically) `cv2.THRESH_OTSU`
12. Edge detection
    1.  Canny Edge detection(uses first order derivative)
13. Contours(continuous lines nad curves) `cv2.findContours()`. It has retrieval modes
    1. RETR_LIST
    2. RETR_EXTERNAL
    3. RETR_CCOMP
    4. RETR_TREE 
14. Moments(center points of shapes found) `cv2.moments(countours)`
15. Sorting
16. Approximating

`printText`, `drawContours` for debugging.

SKImage operations : 

1. Thresholding `skimage.filters.threshold_local(image, block_size, offset=10, method='gaussian')`
2. 