# Processes
- created as child of the current process.
- current process create exact copy of iteslf and assign a new pid (fork)
- bash exec uses execcve

## Process vs Threads
- process is self contained execution env
- Each process has its own address space / file descriptor
- process can create threads
- Thread share the same memory space
- kernel scheduler manages thread and processes.
- process can be used for seperate memory. 
- `top` nTH to show number of threads
- `ps -T -p <pid>`
- `htop`

# Killing zombie
- Process exit using the exit() system call
- Process stop when they recieve a signal (other user, other process)
- Linux send  SIGCHLD to parent
- Parent execute `wait()`
- zombie - process that complete the execution but still have PID in the process table.
- ps aux
- orphan process , active process which parent is finished
- Upon termination of parent process, active child is adopted by `init` process

# Linux scheduler
- Process scheduler run process in realtime or normal
- I/O scheudler.
- complete fair scheduler
- Each process has nice values - range -20 to 19.

# Inter process communication
- Define how process communicate
- Shared data
- Shared file
- Sockets
- named pipe

# Linux commands

- comamnd need call system function
- create execution env
- load into memory
- request access to system resources like files
- fork() start the command process
- virtual mem is allocated to run the command
- command run in user space or system space
- linux create task_struct in kernel process table
- task_struct hold process metadata.
- in context switch the kernel save the CPU in task_struct

# System calls
- system calls are defined in the kernel source code
- glibc provide system wrapper around kernel system calls.
- `strace` to trace system call

# Virtual memory area
- when a process starts it allocates virtual memory.
- Within the allocated virtual memory, 
- Code segment
- Data segement
- Heap
- Memory mapped file
- Stack
- /proc/PID/status

# Why containers
- application need different version of the same depdency
- resource access is unlimited
- purly secured applcation allow access to system resources.
- namespaces:
  - cgroup - system resources
  - ipc - interprocess comm
  - network - netowrking
  - mount - directory access
  - pid -running processes
- use `lsns`
- 