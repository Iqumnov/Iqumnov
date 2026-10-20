#!/usr/bin/env python3
"""Backward-compatibility wrapper for build_iqumnov_stats_svg.py"""
import os
import runpy

if __name__ == "__main__":
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_iqumnov_stats_svg.py")
    runpy.run_path(target, run_name="__main__")
