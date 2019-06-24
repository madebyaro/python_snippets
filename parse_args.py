#!/usr/bin/env python3

"""parse_args.py

cli structure for Agent Services

[options] are common options. Examples:
--debug: turn on debug logging
--url (string): connect to controller running at url
--output (string): text or json
--version: version of this tool
--help: this message
--read-timeout (int): maximum socket read time in seconds, 0 disables timeout
--connect-timeout(int): maximum socket connect time in seconds

"""

import os.path
import json
import argparse


class CommandLineInterface():

    def __init__(self):
        self.__logger = make_logger(self.__class__.__name__)
        self.__logger.debug('starting')

        self.__args = None

    def parse_args(self, args: List[str] = None) -> None:
        parser = argparse.ArgumentParser(
            description='Hyperion Agent Services CLI')
        parser.add_argument(
            'service',
            default=None,
            help='Service'
        )
        parser.add_argument(
            'command',
            default=None,
            help='Command'
        )
        parser.add_argument(
            'destination',
            default=None,
            help='Agent or Master ID, context specific'
        )
        parser.add_argument(
            'params',
            default=None,
            nargs='*',
            help='Command parameters'
        )
        parser.add_argument(
            '-r', '--registry-path',
            default='.',
            help='Path to registry files'
        )
        parser.add_argument('-u', '--rabbit-uri',
                            default='amqp://guest:guest@localhost')
        parser.add_argument(
            '-w', '--wait',
            type=int,
            default=10,
            metavar='SEC',
            help='Wait SEC seconds for notifications'
        )
        parser.add_argument(
            '-e', '--exec-cmd',
            default='dir',
            help='command to execute'
        )
        parser.add_argument("-s", "--server",
                            action="store_true",
                            help=("Run TAS in server mode. This must "
                                  "be passed for each call"))
        self.__args = parser.parse_args(args=args)


def main():
    cli = CommandLineInterface()
    cli.parse_args()
    

if __name__ == '__main__':
    main()
