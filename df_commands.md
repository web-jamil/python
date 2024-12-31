The `df` command in Linux (and other Unix-like operating systems) is used to report the amount of disk space used and available on file systems. The name "df" stands for **disk free**, and it's one of the most useful commands for system administrators and users to monitor storage usage.

Here’s a detailed breakdown of the `df` command and its options:

---

### **1. Basic Usage of `df`**

The basic syntax of the `df` command is:

```bash
df [options] [file or directory]
```

- **file or directory**: This is optional. If provided, `df` will display information for the file system that contains the given file or directory. If no argument is provided, `df` reports on all mounted file systems.

#### **Example**:

```bash
df
```

This will display the disk space usage for all mounted file systems.

---

### **2. Key Columns in `df` Output**

The output of `df` shows the following key columns (for each mounted file system):

1. **Filesystem**: The name of the file system.
2. **1K-blocks**: The total size of the file system in 1K blocks.
3. **Used**: The amount of space used on the file system.
4. **Available**: The amount of space available for use on the file system.
5. **Use%**: The percentage of space used on the file system.
6. **Mounted on**: The directory where the file system is mounted.

#### **Example Output**:

```bash
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       10240000 2048000  8192000  21% /
tmpfs            1024000    1024   1022976   1% /dev/shm
/dev/sdb1       51200000 30000000  15000000  60% /mnt/data
```

In this example:

- **/dev/sda1**: The root file system with a total size of 10 GB, of which 2 GB is used, and 8 GB is available.
- **/dev/sdb1**: A mounted data partition with a total size of 50 GB, of which 30 GB is used and 15 GB is available.
- **tmpfs**: A temporary file system (typically used for memory-based storage like `/dev/shm`), with only 1 MB used out of 1 GB.

---

### **3. Common `df` Options**

Here are some of the most commonly used options with the `df` command:

#### **3.1 Display Disk Space in Human-Readable Format**

- **`-h`**: Makes the output easier to read by showing sizes in human-readable format (e.g., KB, MB, GB).
  ```bash
  df -h
  ```
  Example output:
  ```bash
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sda1        10G  2.0G  8.0G  21% /
  tmpfs            1.0G  1.0M  1.0G   1% /dev/shm
  ```

#### **3.2 Display Inodes Usage**

- **`-i`**: Displays inode information instead of disk space usage. Inodes represent file metadata (not the data itself) such as filenames, permissions, and ownership.
  ```bash
  df -i
  ```
  Example output:
  ```bash
  Filesystem     Inodes  IUsed   IFree IUse% Mounted on
  /dev/sda1       262144  50000  212144   20% /
  tmpfs            25600     12   25588    1% /dev/shm
  ```

#### **3.3 Display File System Type**

- **`-T`**: Shows the type of the file system (e.g., ext4, ntfs, tmpfs).
  ```bash
  df -T
  ```
  Example output:
  ```bash
  Filesystem     Type  1K-blocks    Used Available Use% Mounted on
  /dev/sda1      ext4   10240000 2048000  8192000  21% /
  tmpfs           tmpfs  1024000    1024   1022976   1% /dev/shm
  ```

#### **3.4 Exclude Mounted File Systems**

- **`-x [type]`**: Excludes file systems of the specified type from the output. This is useful if you want to exclude temporary or pseudo file systems (like `tmpfs`).
  ```bash
  df -x tmpfs
  ```

#### **3.5 Display Information for a Specific File System or Directory**

- **[path]**: If you provide a specific file or directory, `df` will display the disk usage for the file system that contains the path.
  ```bash
  df /home
  ```
  This shows disk usage specifically for the file system where `/home` is mounted.

#### **3.6 Display the File System Space for All File Systems**

- **`-a`**: This option shows file systems that have zero blocks (e.g., virtual file systems like `/proc` or `/sys`).
  ```bash
  df -a
  ```

#### **3.7 Combine Multiple Options**

You can combine multiple options to tailor the output. For example, if you want human-readable output along with file system type:

```bash
df -hT
```

This will show both human-readable sizes and the file system types.

---

### **4. `df` Use Cases**

Here are some common scenarios where the `df` command is useful:

#### **4.1 Checking Free Space on a File System**

You can use `df` to see if a file system is running out of space. For example:

```bash
df -h /dev/sda1
```

This will show the disk usage of the `/dev/sda1` file system in a human-readable format.

#### **4.2 Monitoring Disk Space Usage Over Time**

If you want to keep track of disk space usage, you can periodically run the `df` command and compare the output. You can automate this by using `cron` jobs or write a script that logs the output to a file.

#### **4.3 Identifying File Systems with Low Space**

To identify file systems with high usage, you can sort the output of `df`:

```bash
df -h | sort -k5 -n
```

This will sort the file systems by the percentage of space used (column 5).

#### **4.4 Checking Inode Usage**

Inodes represent the number of files and directories. If the system runs out of inodes, it will not be able to create new files even if there is free disk space. To check inode usage:

```bash
df -i
```

This will show the number of inodes used and free on each file system.

---

### **5. Example Usage Scenarios**

#### **5.1 Check Disk Usage for a Single File System**

```bash
df -h /dev/sda1
```

Output:

```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       10G  2.0G  8.0G  21% /
```

#### **5.2 Check Disk Usage for All File Systems Including Temporary Files**

```bash
df -a
```

#### **5.3 Display Inodes Usage**

```bash
df -i
```

#### **5.4 Exclude Certain File Systems**

```bash
df -x tmpfs
```

---

### **6. Summary of Common `df` Options**

| Option      | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| `-h`        | Human-readable sizes (KB, MB, GB)                                     |
| `-i`        | Show inode usage instead of space usage                               |
| `-T`        | Show the file system type                                             |
| `-a`        | Show all file systems (including 0-block file systems)                |
| `-x [type]` | Exclude file systems of the specified type                            |
| `[path]`    | Display information for the file system containing the specified path |

---

### **Conclusion**

The `df` command is essential for monitoring disk space and ensuring that your system doesn’t run out of storage. It can be used in a variety of scenarios, from checking the overall disk usage on the system to examining specific file systems or inode usage. Understanding and using `df` regularly is an important practice in managing Linux or Unix-like systems effectively.

The `df` command is a widely used utility in Unix-based systems (like Linux and macOS) for displaying information about disk space usage on the file system. It provides an overview of available and used disk space on all mounted filesystems, helping users understand how much disk space is being consumed and how much is free.

Here's an in-depth explanation of the `df` command:

---

### **1. Basic Usage of `df`**

The basic syntax for the `df` command is:

```bash
df [options] [filesystem]
```

- **[filesystem]**: You can specify the directory or mount point (e.g., `/home` or `/`) to display disk space information for a specific filesystem. If no filesystem is specified, `df` will show information for all mounted filesystems.

#### **Example**:

```bash
df
```

This command will display the disk usage for all mounted filesystems in the system.

---

### **2. Common `df` Options**

The `df` command has various options to customize the output. Here are some of the most commonly used options:

#### **2.1 Display Disk Usage in Human-Readable Format**

- **`-h`**: Displays the disk space in a human-readable format, which automatically selects the appropriate unit (KB, MB, GB, etc.).
  ```bash
  df -h
  ```
  Example output:
  ```
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sda1        50G  20G   30G  40% /
  /dev/sdb1       100G  60G   40G  60% /data
  ```

#### **2.2 Display Disk Usage for a Specific Filesystem**

- **`[filesystem]`**: To display the disk usage for a specific filesystem or directory.
  ```bash
  df /home
  ```
  This shows disk space usage for the `/home` directory (if it is mounted on a separate filesystem).

#### **2.3 Display Information in Blocks**

- **`-B [block_size]`**: Displays the disk usage in specified block sizes (e.g., 1K, 1M, 1G).
  ```bash
  df -B 1M
  ```
  This will display disk usage in megabytes.

#### **2.4 Show Inodes Usage**

- **`-i`**: Displays inode usage instead of disk space. Inodes are data structures used by the filesystem to store information about files.
  ```bash
  df -i
  ```
  Example output:
  ```
  Filesystem     Inodes  IUsed   IFree IUse% Mounted on
  /dev/sda1      1310720 100000 1210720    8% /
  /dev/sdb1      1048576 500000 548576    48% /data
  ```

#### **2.5 Show System Information Only for File Systems with Specified Type**

- **`-t [type]`**: Displays information only for filesystems of a specific type (e.g., `ext4`, `xfs`, `tmpfs`).
  ```bash
  df -t ext4
  ```
  This will display only the `ext4` filesystems.

#### **2.6 Exclude Filesystems**

- **`-x [type]`**: Excludes filesystems of a specific type from the output.
  ```bash
  df -x tmpfs
  ```
  This excludes all `tmpfs` filesystems from the disk usage report.

#### **2.7 Display the File System Mount Points**

- **`-a`**: Includes filesystems with 0 blocks, such as pseudo-filesystems, special filesystems (e.g., `proc`), and filesystems that have no disk space.
  ```bash
  df -a
  ```

#### **2.8 Show File System Type**

- **`-T`**: Displays the filesystem type in the output.
  ```bash
  df -T
  ```
  Example output:
  ```
  Filesystem     Type  Size  Used Avail Use% Mounted on
  /dev/sda1      ext4  50G   20G  30G  40% /
  /dev/sdb1      ext4  100G  60G  40G  60% /data
  ```

---

### **3. Output of `df` Command**

The output of the `df` command provides information on each filesystem, including:

- **Filesystem**: The name of the filesystem (e.g., `/dev/sda1`).
- **Size**: The total size of the filesystem.
- **Used**: The amount of space currently used on the filesystem.
- **Avail**: The amount of available space remaining on the filesystem.
- **Use%**: The percentage of used space relative to the total space.
- **Mounted on**: The directory where the filesystem is mounted.

#### **Example**:

```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G  20G   30G  40% /
/dev/sdb1       100G  60G   40G  60% /data
```

---

### **4. Use Cases for `df`**

The `df` command is primarily used for:

#### **4.1 Checking Disk Space Usage**

- You can use `df` to check how much space is used on a particular disk or partition and how much free space remains.

#### **4.2 Monitoring Filesystem Health**

- It helps in monitoring disk space and ensuring you don't run out of space on critical filesystems (e.g., `/` or `/home`).

#### **4.3 Tracking Usage Over Time**

- Regularly using `df` can help track changes in disk space usage and identify unexpected spikes in disk usage.

#### **4.4 Identify Inode Usage**

- Use `df -i` to monitor inode usage. A filesystem can run out of inodes even if there is free space, particularly when dealing with a large number of small files.

#### **4.5 Filesystem Compatibility**

- The `df -T` option allows you to quickly verify the type of filesystem (e.g., `ext4`, `xfs`, `btrfs`) to ensure it matches your expectations.

---

### **5. Examples of `df` Usage**

#### **5.1 Check Disk Space in Human-Readable Format**

```bash
df -h
```

#### **5.2 Check Disk Usage for a Specific Directory**

```bash
df /home
```

#### **5.3 Check Inode Usage**

```bash
df -i
```

#### **5.4 Exclude Temporary File Systems (e.g., `tmpfs`)**

```bash
df -x tmpfs
```

#### **5.5 Display Filesystem Types**

```bash
df -T
```

#### **5.6 Show Disk Usage in Megabytes**

```bash
df -B 1M
```

---

### **6. Summary of Common `df` Options**

| Option      | Description                                |
| ----------- | ------------------------------------------ |
| `-h`        | Human-readable format (KB, MB, GB, etc.)   |
| `-i`        | Display inode usage                        |
| `-T`        | Show filesystem type                       |
| `-B [size]` | Display disk usage in specified block size |
| `-a`        | Include filesystems with 0 blocks          |
| `-t [type]` | Show only filesystems of a specific type   |
| `-x [type]` | Exclude filesystems of a specific type     |

---

### **7. Conclusion**

The `df` command is a vital tool for checking the disk space usage and filesystem status on a Unix-based system. Whether you're monitoring the available space, tracking inode usage, or ensuring your filesystems are functioning as expected, `df` is an essential utility for system administrators and anyone managing disk space. It provides a clear and easy-to-read summary of how disk space is allocated and used on your system, helping you make informed decisions regarding file storage and maintenance.

The `df` command in Unix-like operating systems (Linux, macOS, etc.) is used to report the disk space usage on file systems. It provides details about the available and used disk space on mounted file systems. The `df` command is essential for system administrators to monitor disk usage and prevent disk space from running out, which could lead to performance issues or system crashes.

Here’s an in-depth look at the **`df` command**:

---

### **1. Basic Usage of `df`**

The basic syntax of the `df` command is:

```bash
df [options] [file]
```

- **file** (optional): Specifies a file or directory. If provided, `df` will show disk space for the file system that contains the specified file or directory. If no file is specified, `df` shows disk space for all mounted file systems.

#### **Example**:

- **Check disk usage for all file systems**:

  ```bash
  df
  ```

  This will display information about all the mounted file systems.

- **Check disk usage for a specific file or directory**:
  ```bash
  df /home
  ```
  This will display disk space usage for the file system where the `/home` directory is located.

---

### **2. Understanding `df` Output**

The `df` command typically produces an output with the following columns:

| Column         | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| **Filesystem** | The name of the file system (e.g., `/dev/sda1`, `tmpfs`, `/dev/mapper/vg`) |
| **1K-blocks**  | The total space available on the file system (in kilobytes).               |
| **Used**       | The amount of space used (in kilobytes).                                   |
| **Available**  | The amount of space available for use (in kilobytes).                      |
| **Use%**       | The percentage of space used (calculated as `(Used / 1K-blocks) * 100`).   |
| **Mounted on** | The mount point of the file system (e.g., `/`, `/home`, `/var`, etc.).     |

#### **Example Output**:

```bash
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       1024000  512000   512000  50% /
/dev/sdb1       2048000  1024000  1024000  50% /data
tmpfs            512000     5000   507000   2% /run
```

- The file system `/dev/sda1` has 1,024,000 kilobytes total, with 512,000 kilobytes used and 512,000 kilobytes available, occupying 50% of the disk.
- The file system `/dev/sdb1` has 2,048,000 kilobytes total, with 1,024,000 kilobytes used, and 1,024,000 kilobytes available, also occupying 50% of the disk.

---

### **3. Commonly Used `df` Options**

The `df` command includes several options that change its behavior or provide more specific information. Some of the most commonly used options are:

#### **3.1 Display Disk Space in Human-Readable Format**

- **`-h`**: Displays the disk space in a more human-readable format (using MB, GB, etc.).
  ```bash
  df -h
  ```
  Example output:
  ```bash
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sda1       1.0G  500M  500M  50% /
  /dev/sdb1       2.0G  1.0G  1.0G  50% /data
  tmpfs            500M  5.0M  495M   2% /run
  ```

#### **3.2 Display File System Type**

- **`-T`**: Shows the file system type (e.g., ext4, xfs, tmpfs).
  ```bash
  df -T
  ```
  Example output:
  ```bash
  Filesystem     Type      1K-blocks    Used Available Use% Mounted on
  /dev/sda1      ext4      1024000  512000   512000  50% /
  /dev/sdb1      ext4      2048000  1024000  1024000  50% /data
  tmpfs          tmpfs      512000     5000   507000   2% /run
  ```

#### **3.3 Exclude File Systems from Output**

- **`-x [fstype]`**: Excludes file systems of the specified type from the output. Useful when you want to ignore temporary or virtual file systems like `tmpfs`.
  ```bash
  df -x tmpfs
  ```
  This will exclude all `tmpfs` file systems from the output.

#### **3.4 Show All File Systems**

- **`-a`**: Shows all file systems, including those with 0 blocks, or file systems like virtual file systems (`tmpfs`).
  ```bash
  df -a
  ```

#### **3.5 Report File System Inodes Usage**

- **`-i`**: Shows the inode usage of file systems, which is useful for tracking the number of files on a file system.
  ```bash
  df -i
  ```
  Example output:
  ```bash
  Filesystem     Inodes  IUsed  IFree IUse% Mounted on
  /dev/sda1      262144  2048  260096    1% /
  /dev/sdb1      524288  4096  520192    1% /data
  tmpfs           12800    50  12750    1% /run
  ```

#### **3.6 Display Disk Space for Specific Mount Point**

- **`[mount-point]`**: You can specify the mount point or directory for which you want to check disk usage.
  ```bash
  df /home
  ```
  This shows disk usage for the file system where `/home` is mounted.

#### **3.7 Display File System Usage for All Mounted Devices**

- **`df -l`**: Displays the disk usage for local file systems only, excluding network-mounted file systems (e.g., NFS).
  ```bash
  df -l
  ```

#### **3.8 Display Disk Space in Kilobytes**

- **`-k`**: Forces the display of disk space in kilobytes (this is the default behavior for many systems).
  ```bash
  df -k
  ```

#### **3.9 Show File System Usage for Specific Devices**

- **`df /dev/sda1`**: To check the usage of a specific device or disk partition.
  ```bash
  df /dev/sda1
  ```

---

### **4. Practical Examples of `df`**

- **Check the disk space for the root file system in a human-readable format**:

  ```bash
  df -h /
  ```

- **Check the disk space on all mounted file systems**:

  ```bash
  df -h
  ```

- **Check the file system usage for a specific directory (e.g., `/home`)**:

  ```bash
  df -h /home
  ```

- **View file system type along with disk space**:

  ```bash
  df -hT
  ```

- **Check inode usage for all file systems**:

  ```bash
  df -i
  ```

- **Check disk usage but exclude tmpfs file systems**:
  ```bash
  df -h -x tmpfs
  ```

---

### **5. Advanced `df` Usage Scenarios**

#### **5.1 Monitoring Disk Usage Over Time**

You can periodically monitor disk usage with the `df` command by using a `watch` command to run `df` at regular intervals:

```bash
watch df -h
```

This will update the `df` output every 2 seconds, helping you track disk space in real time.

#### **5.2 Disk Space Usage Alerts**

System administrators often use `df` in scripts to automatically monitor disk space. For example, you could create a script to send an email alert if disk usage exceeds a certain threshold:

```bash
#!/bin/bash
THRESHOLD=90
df -h | grep -vE '^Filesystem' | while read line
do
    USEP=$(echo $line | awk '{ print $5 }' | sed 's/%//g')
    if [ $USEP -ge $THRESHOLD ]; then
        echo "Disk space usage is above threshold: $line" | mail -s "Disk space alert" admin@example.com
    fi
done
```

This script checks disk usage for each file system and sends an alert if the usage exceeds 90%.

---

### **6. Conclusion**

The `df` command is an essential tool for system administrators and users alike to monitor disk usage and ensure systems do not run out of space. With its various options, `df` provides detailed and flexible information about mounted file systems, helping users manage their storage effectively. Regular use of `df` can help prevent potential system failures due to insufficient disk space.
