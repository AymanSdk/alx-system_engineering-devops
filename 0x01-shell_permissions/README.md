# 0x01. Shell Permissions

This repository contains a collection of scripts and resources related to shell scripting and permissions. This guide aims to provide an overview of shell scripting concepts and permissions in Unix-like systems.

## Table of Contents
1. Introduction to Shell Scripting
2. Permissions Overview
3. File Permissions
4. Directory Permissions
5. Changing Permissions
6. Special Permissions
7. Useful Shell Commands
8. Resources

## 1. Introduction to Shell Scripting
Shell scripting is the process of writing and executing scripts using a shell interpreter. A shell is a command-line interface that allows users to interact with the operating system by executing commands. Shell scripts are text files containing a series of commands that can be executed sequentially.

Shell scripting is powerful and allows for automation, repetitive tasks, and system administration. It provides various control structures, variables, functions, and file manipulation capabilities.

## 2. Permissions Overview
In Unix-like systems, file permissions are used to determine who can read, write, or execute files or directories. Each file and directory has three sets of permissions: one for the owner, one for the group, and one for others (everyone else). These permissions can be represented using numeric values or symbolic notation.

The three basic permissions are:
- Read (r): Allows reading or viewing the contents of a file or directory.
- Write (w): Allows modifying or deleting a file, as well as creating, deleting, or renaming files within a directory.
- Execute (x): Allows executing a file if it is a script or has executable permissions. For directories, execute permission enables navigating (accessing) the directory.

## 3. File Permissions
File permissions specify what actions can be performed on a file. To view the permissions of a file, you can use the `ls -l` command, which displays a detailed listing that includes permissions.

The permissions of a file are represented by ten characters:
- The first character indicates the file type ('-' for a regular file).
- The next three characters represent the owner's permissions.
- The following three characters represent the group's permissions.
- The last three characters represent permissions for others.

For example, `rw-r--r--` means the owner has read and write permissions, while the group and others have only read permissions.

## 4. Directory Permissions
Directory permissions determine what actions can be performed on a directory. The permissions are similar to file permissions, but they have a slightly different interpretation.

For directories, the `read` permission allows listing the directory's contents, the `write` permission allows creating, deleting, or renaming files within the directory, and the `execute` permission allows accessing the directory (i.e., using it as part of a path).

## 5. Changing Permissions
To change permissions, the `chmod` command is used. It allows modifying permissions in both symbolic and numeric notations.

The symbolic notation uses letters to specify the permissions. For example, `u+r` adds read permission for the owner, `g-w` removes write permission for the group, and `o=x` sets execute permission for others.

The numeric notation uses a three-digit value (0-7) to represent permissions. Each digit corresponds to the owner, group, or others. For example, 755 represents `rwxr-xr-x`, where the owner has all permissions, while the group and others have read and execute permissions.

