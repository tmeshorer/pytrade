# Kernel
    - control over everything
    - Provide access to hardware device
    - User with UID 0 has all capbilities
## Kernel modules
    - Hardware support is offered by drivers
    - Drivers are loaded on demand
    - Char device
    - Block device 
    - Network device - Ioctl()
## Glibc
    - GNU C library
    - provide the core linuc facilities - open/read/write/malloc

## Shell
    - Pass instruction to kernel from the user
    - bash is the unix shell

## File description
    - Everything is a file
    - File descriptors are the nubmer used to keep a list of open file.
    - All processes have at least 3 file descriptors
## Kernel generic interface
    - Virtual mem for memory
    - Virtual file system (VFS) for file systems
    - TCP/IP for networking
    - Process use system call to kernel
## /Proc 
- /proc is a pseudo file system to interfce kernel data structures
- Kernel use sysfs and debugfs
- Usefull file in /proc
  - cpuinfo
  - meminfo
  - cmdline
  - vmstat - stat about current mem usage
  - filesystems
  - mounts
- Each process has /proc/<pid>
- See by ps to top
- /etc/sysctl.conf.d/
- /proc/sysrq - perform advance operation on the kernel
- eBPF - VM in the kernel that allow programmer to run code in the kernel.
- 
## Hardware access
- /dev - access the device drivers
- device nodes are accessed with major/minor number
- devices are initlized via initamfs
- cat /sys/bus/cpu/devices/cpu1/online

## Linux storage device
- Linux store device on hard disk
- Structure disk by using partition
- Install fs on a patition
- Linux uses volumes for more dynamic approch.
- Use logical block addressing to address sector.
- Sector is 512 bytes in side.
- When creating parition, boundires are specified in sectors.
- MBR (Master boot record)
  - First 512 bytes on disk, 4 parition defined as primary partition.
  - One partition can be defined as extend parition.
  - GUID partition table (GPT) More space for managning partition, Max 128 parition
  - Store as second sector on disk
  - Next sector used to store partitions
 
 
## Logical volume manager
- Partition are static
- LVM - Multi device volume, raid
- LMV can take snapshot

## Device mapper
- support advance storage feature.
- map phsyical block device to virutal block device
- cache / encryption / raid

# VDO
- Thin provioning on top of LVM to use data deduplication and compression.
- LMV provides thin provisniong.

# Stratis
- Stratis volume use XFS

# LUKS
- Linux unified key setup - use for encrypted device.
- Encrypt and mount complete device - new device mapper device.

# VFS
- Generic interface used by several specific FS.
- Provide common system calls that are needed in all file systems

# POSIX FS
- posix complient FS
- Suport random reads, writes, fsync
- File access controlled by permissions.
- Features implemented in system calls.
- Support inodes for metadata
- Support directories and hard links

# File system
- Superblock contain FS metadata
- Directory map name -> inode
- Each file is an inode which contain a list of blocks

# Inode
- Reside in inode table
- Each file is one inode
- stat <filename> to see inode information. 

# Files
- Files stored on disk as blcoked
- Block size is a peoperty of the file system

# Sparse Files
- Block are written to disk when they information
- Empty blockes not commited

# Fuse file system
- Fuse is a file system in user space.

# Next generation FS
- XFS - 2014
- No convincing Next gen FS.

# BTRFS
- Btree file system
- Support copy on write.
- 