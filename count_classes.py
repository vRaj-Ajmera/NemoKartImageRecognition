import os
from collections import Counter

def count_classes(annotation_train_dir, annotation_val_dir, classes_file):
    """
    Count the occurrences of each class in YOLO annotation files for train and validation datasets.

    Args:
        annotation_train_dir (str): Path to the folder containing YOLO annotation .txt files for training.
        annotation_val_dir (str): Path to the folder containing YOLO annotation .txt files for validation.
        classes_file (str): Path to the `classes.txt` file with class names.

    Returns:
        tuple: Three dictionaries with class counts for train, val, and total.
    """
    # Load class names
    with open(classes_file, "r") as f:
        class_names = [line.strip() for line in f.readlines()]

    # Counters for class occurrences
    train_counts = Counter()
    val_counts = Counter()

    # Count occurrences in training annotations
    for filename in os.listdir(annotation_train_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(annotation_train_dir, filename)
            with open(filepath, "r") as file:
                for line in file:
                    class_id = int(line.split()[0])  # Extract class_id
                    train_counts[class_names[class_id]] += 1

    # Count occurrences in validation annotations
    for filename in os.listdir(annotation_val_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(annotation_val_dir, filename)
            with open(filepath, "r") as file:
                for line in file:
                    class_id = int(line.split()[0])  # Extract class_id
                    val_counts[class_names[class_id]] += 1

    # Combine train and validation counts for total
    total_counts = train_counts + val_counts

    return train_counts, val_counts, total_counts

# Paths to your files
annotation_train_dir = "dataset/labels/train"  # train annotations
dataset_val_dir = "dataset/labels/val"  # val annotations
classes_file = "dataset/classes.txt"  # classes.txt file

# Count classes
train_counts, val_counts, total_counts = count_classes(annotation_train_dir, dataset_val_dir, classes_file)

# Print the results
print("Train Counts:")
for class_name, count in train_counts.items():
    print(f"{class_name}: {count}")

print("=" * 50)  # Divider

print("Validation Counts:")
for class_name, count in val_counts.items():
    print(f"{class_name}: {count}")

print("=" * 50)  # Divider

print("Total Counts:")
for class_name, count in total_counts.items():
    print(f"{class_name}: {count}")
