# IRAWS by Tiago Tamagusko
"""
Transfer Learning a with Deep Learning to train a model to detect unusual events (skids, vehicles off-street, and on
the wrong lane) in highways.

Models: https://github.com/tamagusko/nordicopendata/tree/main/models
Data: https://github.com/tamagusko/nordicopendata/tree/main/data

Usage:
    $ python path/to/train.py --basemodel MODEL --data "path/to/data" --cam COUNTRY_CAMERA --img SIZE

Example:
    $ python train.py --basemodel 'MobileNetV2' --data "data/" --cam 'FI_C0166000' --img 160
"""

import argparse


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Train a custom model to detect unusual road events",
    )
    parser.add_argument("-b", "--basemodel", type=str, default='MobileNetV2', required=True,
                        help="Base model for transfer learning: ['MobileNetV2', 'EfficientNetB1', 'EfficientNetB7']")
    parser.add_argument("-d", "--data", type=str, default='data/',
                        required=True, help="File path of data")
    parser.add_argument("-c", "--cam", type=str, required=True,
                        help="Camera to train the model")
    parser.add_argument("-i", "--img", type=int, default=160, required=True,
                        help="Size of images to train the model, recommendation: ['MobileNetV2': 160, 'EfficientNetB1': 240, 'EfficientNetB7': 600]")
    args = parser.parse_args()
    print(args.model)


if __name__ == "__main__":
    main()
