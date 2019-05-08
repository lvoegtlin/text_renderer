import argparse
import os
import shutil

from sklearn.model_selection import train_test_split


def split_dataset(dataset_path, copy=False):
    print("Creating folders for the split...")
    output_images, output_root = create_folders(dataset_path)

    print("Fetching gt...")
    gt = get_gt_and_move_files(dataset_path, output_images, copy)

    # split the dataset
    print("Split gt...")
    train, val = train_test_split(gt)

    print("Writing files...")
    write_files(output_root, train, val)

    print("Finished splitting!")


def write_files(output_root, train, val):
    with open(os.path.join(output_root, 'train.txt'), 'w') as f:
        [f.write(' '.join(line)) for line in train]
    with open(os.path.join(output_root, 'dev.txt'), 'w') as f:
        [f.write(' '.join(line)) for line in val]


def get_gt_and_move_files(dataset_path, output_images, copy):
    # gt per line
    gt = []

    # get all files in folder
    for root, _, files in os.walk(dataset_path):
        # iterate over each file
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            # check if its a image
            if copy:
                if file_extension == '.jpg':
                    # move file to output folder
                    shutil.copy(os.path.join(root, file), os.path.join(output_images, file))
                continue
            if "ground_truth.txt" in file:
                with open(os.path.join(root, file), 'r+') as f:
                    # ground truth per line (tuple (filename, ints)) care, last int has a \n
                    gt = [tuple(line.split(' ')) for line in f.readlines()]
    return gt


def create_folders(dataset_path):
    # create output folder
    root_path = os.path.join(os.path.split(dataset_path)[0], "split")
    output_images = os.path.join(root_path, "images")
    if not os.path.exists(output_images):
        os.makedirs(output_images)
    return output_images, root_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split dataset')

    parser.add_argument("--dataset_path", required=True,
                        help="The path to the data set")

    args = parser.parse_args()
    split_dataset(args.dataset_path)
