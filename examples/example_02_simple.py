# Basic example - create base config for you app with dataclass.
# same as example_01_simple.py but parser created at parse_cfg function.
from pydantic import BaseModel
from argparse_pydantic.core import parse_args


# Create config for App as dataclass
class AppCfg(BaseModel):
    arg_1: int = 0
    arg_2: float = 0.1
    arg_3: str = "string"


if __name__ == "__main__":
    # parse arguments.
    # parse_args return object from config Class (based on BaseModel) sent to it as argument.
    # if you want some config to parser, you can send it as argument to parse_args
    cfg: AppCfg = parse_args(AppCfg)
    # now we got object with autocompletion at ide.
    # if you want to play with config at jupyter notebook: import AppCfg.
    print(cfg)
    assert cfg == AppCfg()
