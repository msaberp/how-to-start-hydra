"""
Argument management using hydra

Second step:
    - loading a yaml file which uses a default attribute to load other yaml files
    - using command line to load different yaml file as a sub-config
    - overriding the config in the middle of code
    - sweeping between different configs [multi-run]

"""

import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="configs", config_name="lesson_5")
def my_app(cfg: DictConfig) -> None:
    print("\n")
    print(OmegaConf.to_yaml(cfg))
    
    # in case you want to change your dataset
    # print("changing the dataset to cifar10")

    # cfg = hydra.compose("lesson_5", overrides=['dataset=cifar10'])
    # print("\n")
    # print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    # also give some examples on command line overrides

