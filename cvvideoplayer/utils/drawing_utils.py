"""
This module contains an drawing routines based on OpenCV.
"""

from typing import Tuple, Optional

import cv2
import numpy as np


def draw_rectangle(
    image,
    x,
    y,
    w,
    h,
    color,
    thickness=2,
):
    """Draw a rectangle."""
    pt1 = int(x), int(y)
    pt2 = int(x + w), int(y + h)
    cv2.rectangle(image, pt1, pt2, color, thickness, lineType=cv2.LINE_AA)


def draw_polygon(
    image,
    points,
    color,
    thickness=2,
):
    """Draw a rectangle."""
    points = np.array(points).reshape((-1, 1, 2)).astype(np.int32)
    cv2.polylines(image, [points], isClosed=True, color=color, thickness=thickness, lineType=cv2.LINE_AA)


def draw_label(
    frame: np.ndarray,
    bbox_x1: int,
    bbox_y1: int,
    bbox_h: int,
    below_or_above: str,
    text: str,
    font_scale: float,
    thickness: int,
    text_color: Tuple[int, int, int],
    label_line_color: Optional[Tuple[int, int, int]] = None,
    filling_color: Optional[Tuple[int, int, int]] = None,
):
    assert below_or_above in {"below", "above"}

    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, fontScale=font_scale, thickness=thickness)

    if below_or_above == "above":
        label_pt1 = int(bbox_x1), int(bbox_y1 - 10 - text_size[0][1])
        label_pt2 = int(bbox_x1 + 10 + text_size[0][0]), int(bbox_y1)
        text_position = label_pt1[0] + 5, label_pt2[1] - 5
    else:
        label_pt1 = int(bbox_x1), int(bbox_y1 + bbox_h)
        label_pt2 = int(bbox_x1 + 10 + text_size[0][0]), int(bbox_y1 + bbox_h + 10 + text_size[0][1])
        text_position = label_pt1[0] + 5, label_pt2[1] - 5

    if filling_color is not None:
        cv2.rectangle(frame, label_pt1, label_pt2, color=filling_color, thickness=-1, lineType=cv2.LINE_AA)
    if label_line_color is not None:
        cv2.rectangle(frame, label_pt1, label_pt2, color=label_line_color, thickness=thickness, lineType=cv2.LINE_AA)

    cv2.putText(
        img=frame,
        text=text,
        org=text_position,
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=font_scale,
        color=text_color,
        thickness=thickness,
        lineType=cv2.LINE_AA,
    )
