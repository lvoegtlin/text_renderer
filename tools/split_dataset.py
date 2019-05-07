import argparse
import os
import shutil

import numpy as np
from sklearn.model_selection import train_test_split

def main(dataset_path):
    # create output folder
    output_root = args.output_path
    output_images = os.path.join(output_root, "images")
    if not os.path.exists(output_root):
        os.makedirs(output_images)

    # get all files in folder
    for root, _, files in os.walk(dataset_path.dataset_path):
        # iterate over each file
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            # check if its a image
            if file_extension == '.jpg':
                # move file to output folder
                shutil.copy(os.path.join(root, file), os.path.join(output_images, file))
            if "ground_truth.txt" in file:
                with open(os.path.join(root, file), 'r+') as f:
                    # ground truth per line (tuple (filename, ints)) care, last int has a \n
                    gt = [tuple(line.split(' ')) for line in f.readlines()]

    train, val = train_test_split(gt)

    with open(os.path.join(output_root, 'train.txt'), 'w') as f:
        [f.write(' '.join(line)) for line in train]
    with open(os.path.join(output_root, 'dev.txt'), 'w') as f:
        [f.write(' '.join(line)) for line in val]

# all images into a images folder
# create two files
# train
# dev (val set)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split dataset')

    parser.add_argument("--dataset_path", required=True,
                        help="The path to the data set")
    parser.add_argument("--output_path", required=True,
                        help="The output path")

    args = parser.parse_args()
    main(args)
