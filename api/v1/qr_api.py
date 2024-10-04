from flask import Blueprint, jsonify, request
from api.utils import create_response
from PIL import Image, ImageEnhance, ImageOps
import cv2
import numpy as np

qr_bp = Blueprint("qr_bp", __name__)


def preprocess_image(image):
    # Convert to grayscale
    gray_image = ImageOps.grayscale(image)
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)
    # Convert to numpy array
    image_array = np.array(enhanced_image)
    return image_array


@qr_bp.route("/qrcode/info", methods=["POST"])
def get_qrcode_info():
    try:
        if "image" not in request.files:
            return create_response(
                success=False, errors="No image part in the request", status_code=400
            )

        file = request.files["image"]
        if file.filename == "":
            return create_response(
                success=False, errors="No selected file", status_code=400
            )

        image = Image.open(file.stream)
        processed_image = preprocess_image(image)

        # Use OpenCV to detect QR codes
        detector = cv2.QRCodeDetector()
        retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(
            processed_image
        )

        qrcodes = []
        for i, data in enumerate(decoded_info):
            if data:
                qrcodes.append(
                    {
                        "type": "QRCODE",
                        "data": data,
                        "position": {
                            "points": points[i].tolist() if points is not None else []
                        },
                    }
                )

        return create_response(success=True, data={"qrcodes": qrcodes})

    except Exception as e:
        return create_response(success=False, errors=str(e), status_code=500)
