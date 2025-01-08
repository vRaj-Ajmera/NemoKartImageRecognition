import os
import shutil
import random

def split_train_val_files(base_path, train_ratio=0.8):
    """
    Splits images and labels into train and val folders.

    Args:
        base_path (str): The path to the dataset directory containing 'images/' and 'labels/' folders.
        train_ratio (float): The ratio of images to use for training (default is 0.8).
    """
    # Paths to images and labels folders
    images_path = os.path.join(base_path, "images")
    labels_path = os.path.join(base_path, "labels")

    # Create train/ and val/ subfolders in images/ and labels/
    train_images_path = os.path.join(images_path, "train")
    val_images_path = os.path.join(images_path, "val")
    train_labels_path = os.path.join(labels_path, "train")
    val_labels_path = os.path.join(labels_path, "val")

    os.makedirs(train_images_path, exist_ok=True)
    os.makedirs(val_images_path, exist_ok=True)
    os.makedirs(train_labels_path, exist_ok=True)
    os.makedirs(val_labels_path, exist_ok=True)

    # Get list of all image files
    all_images = [f for f in os.listdir(images_path) if f.endswith(".png")]
    total_images = len(all_images)
    print(f"Found {total_images} images in {images_path}.")

    # Shuffle and split the images into train and val sets
    random.shuffle(all_images)
    train_count = int(train_ratio * total_images)
    train_images = all_images[:train_count]
    val_images = all_images[train_count:]

    print(f"Splitting {train_count} images into train/ and {total_images - train_count} into val/.")

    # Move images and corresponding labels to train and val folders
    for image_file in train_images:
        # Move image to train/ folder
        shutil.move(os.path.join(images_path, image_file), os.path.join(train_images_path, image_file))

        # Move corresponding label to train/ folder
        label_file = image_file.replace(".png", ".txt")
        if os.path.exists(os.path.join(labels_path, label_file)):
            shutil.move(os.path.join(labels_path, label_file), os.path.join(train_labels_path, label_file))

    for image_file in val_images:
        # Move image to val/ folder
        shutil.move(os.path.join(images_path, image_file), os.path.join(val_images_path, image_file))

        # Move corresponding label to val/ folder
        label_file = image_file.replace(".png", ".txt")
        if os.path.exists(os.path.join(labels_path, label_file)):
            shutil.move(os.path.join(labels_path, label_file), os.path.join(val_labels_path, label_file))

    print("Data split complete. New folder structure:")
    print(f"  - {train_images_path}")
    print(f"  - {val_images_path}")
    print(f"  - {train_labels_path}")
    print(f"  - {val_labels_path}")

if __name__ == "__main__":
    path_to_dataset = "exported_yolo_labels/"
    split_train_val_files(path_to_dataset)
