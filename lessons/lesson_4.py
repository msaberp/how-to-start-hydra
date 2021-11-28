"""
Argument management using hydra

First step:
    - loading a yaml file and printing it
    - using command line to change the parameters

link to the documentation:
https://hydra.cc/docs/intro/

link to blog post:
https://medium.com/pytorch/hydra-a-fresh-look-at-configuration-for-machine-learning-projects-50583186b710
"""

import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="configs", config_name="lesson_4")
def my_app(cfg: DictConfig) -> None:
    print("\n")
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    # also give some examples on command line overrides

