#!/usr/bin/python
import argparse
import sys
import os

args = sys.argv

if not args:
    print(
"""
Valid commands are:
1) simplify create_app
2) simplify create_view
3) simplify create_model
"""
    )
