#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:11:59 2022

@author: siljegrue
"""

import glob
import os
import shutil

def file_pattern_search(root_dir, file_pattern, recursive = False):
    """ Find all files matching pattern inside a "root" directory
    # Usage:
    file_list = recursive_file_search(root_dir, file_pattern)
    # Required arguments:
    root_dir:       Path to root dir.
    file_pattern:   Search pattern for file.
                    Example: '*.png' (finds all png files)
    # Optional arguments:
    recursive:      Extend search into subdirectories.
    # Returns:
    file_list:  List with full path to all files found.
    # Notes:
    The function is a convenience wrapper for the glob.glob() function
    Both the root_dir and file_pattern can contain wildcard characters, such as
        '*' :   Match zero or more characters, any value allowed
        '?' :   Match exactly one character
        [2-5]:  Specify range for single digit (here between 2 and 5, inclusive)
    """

    # Use glob.glob() to search
    if recursive:
        glob_str = root_dir + os.path.sep + '**' + os.path.sep + file_pattern
        file_list = glob.glob(glob_str,recursive=True)
    else:
        glob_str = root_dir + os.path.sep + file_pattern
        file_list = glob.glob(glob_str,recursive=False)

    # Sort list and return
    file_list.sort()
    return file_list

def build_newdir_filepath(file_paths,new_dir,new_ext = None):
    """ Create new file paths, keeping file name but inserting new directory
    # Usage:
    new_file_paths = copy_filename_to_new_dir(file_paths,new_dir,...)
    # Required arguments:
    file_paths: List containing file name(s). The name can include a full or
                partial path.
    new_dir:    New file names will be placed inside this directory
    # Optional arguments:
    new_ext:    New file extension, including period(s). Example: '.png'
                If given, the old file name extension will be replaced with this.
    # Returns:
    new_file_paths:  New file path(s) (list).
    # Notes:
    """

    # Get list of file names only
    file_names = [os.path.basename(file) for file in file_paths]

    # Replace file extension (optional)
    if new_ext is not None:
        file_names = [name.split(sep='.')[0] + new_ext for name in file_names]

    # Add new path, remove any unneeded slashes
    new_file_paths = [os.path.normpath(new_dir + os.path.sep + name) for name in file_names]

    return new_file_paths


def copy_hyspec_aux_files(hdr_file,dest_dir,copy_lcf = True,copy_times=True):
    """ Copy auxillary files related to hyperspectral (ENVI) image files
    # Required arguments:
    hdr_file:   Path to header file (part of ENVI image)
    dest_dir:   Path to destination directory
    # Optional arguments:
    copy_lcf:   Do copy .lcf file (boolean)
    copy_times: Do copy .times file (boolean)
    # Notes:
    The function assumes the following naming convention:
    Binary data file:   <base name>.bip
    Header file:        <base name>.bip.hdr
    LCF file:           <base name>.lcf
    Times file:         <base name>.bip.times
    """

    base_name = os.path.join(os.path.dirname(hdr_file),
                    os.path.basename(hdr_file).split(sep='.')[0])

    lcf_path = base_name + '.lcf'
    if copy_lcf and os.path.exists(lcf_path):
        shutil.copy(lcf_path,dest_dir)

    times_path = base_name + '.bip.times'
    if copy_times and os.path.exists(times_path):
        shutil.copy(times_path,dest_dir)