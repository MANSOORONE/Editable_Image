import svgwrite
import cv2
import numpy as np

def generate_svg_from_masks(masks, image_path):
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    dwg = svgwrite.Drawing("output.svg", size=(w, h))

    # Sort masks (big → small)
    masks = sorted(masks, key=lambda x: x['area'], reverse=True)

    for i, mask in enumerate(masks):

        # Remove noise
        if mask['area'] < 500:
            continue

        binary = mask['segmentation'].astype(np.uint8) * 255

        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        pixels = img[mask['segmentation']]
        if len(pixels) == 0:
            continue

        avg_color = pixels.mean(axis=0)

        color = "#{:02x}{:02x}{:02x}".format(
            int(avg_color[2]), int(avg_color[1]), int(avg_color[0])
        )

        group = dwg.g(id=f"layer_{i}")

        for cnt in contours:
            if len(cnt) < 5:
                continue

            path = "M "
            for point in cnt:
                x, y = point[0]
                path += f"{x},{y} "
            path += "Z"

            group.add(dwg.path(d=path, fill=color))

        dwg.add(group)

    dwg.save()
    return "output.svg"