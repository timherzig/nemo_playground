import os
import json
import librosa
import pandas as pd

from mutagen.mp3 import MP3

from helper.parser import parse_arguments

def build_manifest(root, split):
    dataset = pd.read_csv(os.path.join(root, split + '.csv'))

    manifest_path = os.path.join(root, split + '.json')
    with open(manifest_path, 'w') as f_out:
        for idx, row in dataset.iterrows():
            # print(row['path'])
            metadata = {
                'audio_filepath': os.path.join(root, 'clips', row['path']),
                'duration': MP3(os.path.join(root, 'clips', row['path'])).info.length, # librosa.core.get_duration(filename=os.path.join(root, 'clips', row['path']))
                'text': row['sentence']
            }

            json.dump(metadata, f_out)
            f_out.write('\n')

    return

# Not implemented/used
def main():
    args = parse_arguments()

    root_dir = args.dir
    splits = args.splits.split(' ')

    for split in splits:
        build_manifest(root_dir, split)


if __name__ == '__main__':
    main()