import os
import nemo
import pytorch_lightning as pl
import nemo.collections.asr as nemo_asr

from ruamel.yaml import YAML
from torch.utils.data import DataLoader
from helper.parser import parse_arguments
from data.commonvoice_dataset import CommonVoiceDataset


def main():
    args = parse_arguments()

    yaml = YAML(typ='safe')
    with open(args.config) as f:
        params = yaml.load(f)

    
    train_dataset = CommonVoiceDataset('train', args.config['data']['cv_loc'], n_rows=(500 if args.debug else None))
    train_dataloader = DataLoader(train_dataset, batch_size=args.config['training']['bs'], num_workers=args.config['training']['nw'])

    val_dataset = CommonVoiceDataset('dev', args.config['data']['cv_loc'], n_rows=(100 if args.debug else None))
    val_dataloader = DataLoader(val_dataset, batch_size=args.config['training']['bs'], num_workers=args.config['training']['nw'])

    trainer = pl.Trainer(devices=1, accelerator='gpu', max_epochs=50)
    



if __name__ == '__main__':
    main()