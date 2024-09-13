# Virtual memoery
- Total addressable memory as provided by CPU
- When a process load, it creates the virtual address space. 
- When a process requet physical mem access, the kernel maps pysical address to virtual address
- /proc/cpuinfo.

# Cache
- Disk cache is important.
- Page cache / Dentires / inode

# Active / Inactive memory
- Linux keep track of active/inactive memory
- When memory shortage occurs, the kernel will drop inactive file memory.
- Inactive memory stored in swap file
- Swap should contain twice the amount of RAM
- free and top give overview of current swap usage.

# Huge pages
- Default memory page is 4K
- Huge pages - 2Mb
- /proc/meminfo

# Dirty cache
