import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()

    # parser.add_argument('-config', type=str)
    # parser.add_argument('-debug', type=bool, default=False)

    # For building manifest
    parser.add_argument('-dir', type=str)
    parser.add_argument('-splits', type=str)

    return parser.parse_args()