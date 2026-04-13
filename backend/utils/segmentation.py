import cv2
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

# Load model ONLY ONCE (important)
sam = sam_model_registry["vit_b"](checkpoint="sam_vit_b.pth")
mask_generator = SamAutomaticMaskGenerator(sam)

def get_masks(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masks = mask_generator.generate(image)

    return masks