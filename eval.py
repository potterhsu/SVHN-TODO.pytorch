import argparse
import os

import torch


def _eval(path_to_checkpoint: str, path_to_data_dir: str, path_to_results_dir: str):
    os.makedirs(path_to_results_dir, exist_ok=True)

    # TODO: CODE BEGIN
    raise NotImplementedError
    # TODO: CODE END

    print('Start evaluating')

    with torch.no_grad():
        # TODO: CODE BEGIN
        raise NotImplementedError
        # TODO: CODE END

        accuracy = num_hits / len(dataset)
        print(f'Accuracy = {accuracy:.4f}')

    with open(os.path.join(path_to_results_dir, 'accuracy.txt'), 'w') as fp:
        fp.write(f'{accuracy:.4f}')

    print('Done')


if __name__ == '__main__':
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('checkpoint', type=str, help='path to evaluate checkpoint, e.g.: ./checkpoints/model-100.pth')
        parser.add_argument('-d', '--data_dir', default='./data', help='path to data directory')
        parser.add_argument('-r', '--results_dir', default='./results', help='path to results directory')
        args = parser.parse_args()

        path_to_checkpoint = args.checkpoint
        path_to_data_dir = args.data_dir
        path_to_results_dir = args.results_dir

        _eval(path_to_checkpoint, path_to_data_dir, path_to_results_dir)

    main()
