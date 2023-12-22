#!/usr/bin/env python

import os
import pathlib
from configparser import ConfigParser


def get_account_info():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    return (
        config["keys"]["orderly_key"],
        config["keys"]["orderly_secret"],
        config["keys"]["orderly_account_id"],
        config["keys"]["wallet_secret"],
        config["keys"]["orderly_testnet"],
        config["keys"]["wss_id"],
    )
