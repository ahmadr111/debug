import fitz
import cv2
import numpy
import io
import numpy as np

# Infinitive loop
while True:
    # Empty document for this example
    with fitz.open() as doc:
        # Let's also instert 100 empty pages
        for i in range(100):
            doc.insertPage(i)
            page = doc[i]

            # Create image rectangle
            image_rectangle = fitz.Rect(0, 0, 10, 10)

            # Example image - 1000x1000 px zaved as png into byte stream
            image = np.zeros((100, 100, 3))
            _, image_numpy_bytes = cv2.imencode(".png", image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            image_bytes = io.BytesIO(image_numpy_bytes)

     
            #page.insertImage(image_rectangle, stream=image_bytes)
