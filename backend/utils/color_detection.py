import cv2
from sklearn.cluster import KMeans

def extract_colors(image_path, k=5):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixels = img.reshape(-1, 3)

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_

    hex_colors = []
    for color in colors:
        hex_colors.append(
            "#{:02x}{:02x}{:02x}".format(
                int(color[0]), int(color[1]), int(color[2])
            )
        )

    return hex_colors