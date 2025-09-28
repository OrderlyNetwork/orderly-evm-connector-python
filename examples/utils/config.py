#!/usr/bin/env python

import os
import pathlib
from configparser import ConfigParser


def get_account_info():
    config = ConfigParser()
    local_config_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config_local.ini"
    )
    default_config_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config_file_path = local_config_path if os.path.exists(local_config_path) else default_config_path
    config.read(config_file_path)
    return (
        config["keys"]["orderly_key"],
        config["keys"]["orderly_secret"],
        config["keys"]["orderly_account_id"],
        config["keys"]["wallet_secret"],
        str(config["keys"]["orderly_testnet"]).lower() == "true",
        config["keys"]["wss_id"],
    )
