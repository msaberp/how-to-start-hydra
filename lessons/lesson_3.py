"""
Argument management using yacs

link to the github page:
https://github.com/rbgirshick/yacs


"""

from yacs.config import CfgNode as CN
import argparse


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description="Train")
    parser.add_argument(
        "--cfg", dest="cfg_file", help="optional config file", default=None, type=str
    )
    parser.add_argument(
        "--set",
        dest="set_cfgs",
        help="set config keys",
        default=None,
        nargs=argparse.REMAINDER,
    )

    args = parser.parse_args()
    return args


def create_cfg():
    args = parse_args()
    cfg = get_cfg_defaults()
    if args.cfg_file is not None:
        cfg.merge_from_file(args.cfg_file)
    if args.set_cfgs is not None:
        cfg.merge_from_list(args.set_cfgs)
    cfg.freeze()
    return cfg

# -------------------------------------------------------------------------------

if __name__ == "__main__":
  cfg = get_cfg_defaults()
  cfg.merge_from_file("lessons/configs/lesson_3.yaml")
  cfg.freeze()
  print(cfg)
  
  # cfg = create_cfg()
  # print(cfg)

  # Example of using the cfg as global access to options
  if cfg.SYSTEM.NUM_GPUS > 0:
    # Do something regarding having multi-gpu support
    pass

  # model = my_project.create_model(cfg)