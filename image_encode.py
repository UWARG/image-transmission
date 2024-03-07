"""
For encoding images returned by the camera device
"""
import cv2
import numpy as np

def encode_image_as_bytes(ext: str, image: "np.ndarray") -> "tuple[bool, bytes]" :
    """
    Encodes an image (np.ndarray as an RGB matrix) and returns its byte sequence.

    Parameters
    ----------
    ext: str
    image: np.ndarray

    Returns
    -------
    tuple[bool, bytes]
    """
    result, encoded_image = cv2.imencode(ext, image)
    if not result:
        return False, None

    encoded_image_bytes = encoded_image.tobytes()

    return True, encoded_image_bytes
