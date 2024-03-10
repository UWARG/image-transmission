"""
For encoding images returned by the camera device.
"""
import cv2
import numpy as np

def encode_image_as_bytes(ext: str, image: "np.ndarray") -> "tuple[bool, bytes | None]" :
    """
    Encodes an image (np.ndarray as an RGB matrix) and returns its byte sequence.

    Parameters
    ----------
    ext: Desired image encoding format (e.g., ".png").
    image: Input image.

    Returns
    -------
    tuple[bool, bytes]
        The first parameter represents if the image encoding is successful.
        - If it is not successful, the second parameter will be None.
        - If it is successful, the second parameter will be the byte representation
          of the encoded image.
    """
    result, encoded_image = cv2.imencode(ext, image)
    if not result:
        return False, None

    encoded_image_bytes = encoded_image.tobytes()

    return True, encoded_image_bytes
