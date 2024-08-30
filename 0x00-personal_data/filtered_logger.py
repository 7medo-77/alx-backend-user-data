#!/usr/bin/env python3
"""
Module defining a function which obfuscates a log message
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Function to obfuscate passwords and dates of birth
    """
    return_list = []
    for field in fields:
        return_list.append(re.sub(r'{}=(.*)'.format(field, separator), redaction, message))
    return ''.join(return_list)
