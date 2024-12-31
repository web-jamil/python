The `stat` command in Linux is used to display detailed information about a file or directory. Unlike commands like `ls`, which provide a summary, `stat` gives in-depth details, including file size, permissions, ownership, timestamps, and more.

---

## **Basic Syntax**

```bash
stat [OPTION]... FILE...
```

### **Output of `stat`**

When you run `stat` on a file or directory, it displays the following details:

1. **File Name**: The name of the file.
2. **File Size**: Size in bytes.
3. **Blocks**: Number of blocks allocated.
4. **IO Block**: Size of each block in bytes.
5. **File Type**: Type of file (e.g., regular file, directory).
6. **Device**: Device ID in hexadecimal and decimal.
7. **Inode**: Inode number of the file.
8. **Links**: Number of hard links to the file.
9. **Access, Modify, Change**:
   - **Access**: Last accessed time.
   - **Modify**: Last modification time of the file content.
   - **Change**: Last change to file metadata (like permissions).

Example:

```bash
stat myfile.txt
```

Output:

```
  File: myfile.txt
  Size: 1234       Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d   Inode: 131072     Links: 1
Access: 2024-12-28 12:00:00.000000000 +0000
Modify: 2024-12-25 15:00:00.000000000 +0000
Change: 2024-12-26 18:00:00.000000000 +0000
 Birth: -
```

---

## **Options**

### **1. Display File Information**

```bash
stat myfile.txt
```

- Shows detailed information about `myfile.txt`.

---

### **2. Use Custom Format**

The `-c` or `--format` option lets you specify the format of the output.

```bash
stat -c "%n %s %y" myfile.txt
```

- `%n`: File name.
- `%s`: File size.
- `%y`: Last modification time.

Example Output:

```
myfile.txt 1234 2024-12-25 15:00:00.000000000 +0000
```

### **Format Specifiers**

Here are some common specifiers for the `-c` option:
| Format | Description |
|--------|------------------------------------------|
| `%n` | File name |
| `%s` | File size (in bytes) |
| `%b` | Number of blocks allocated |
| `%i` | Inode number |
| `%d` | Device number (in decimal) |
| `%f` | Raw mode (in octal) |
| `%F` | File type (e.g., "regular file") |
| `%h` | Number of hard links |
| `%u` | User ID of owner |
| `%U` | User name of owner |
| `%g` | Group ID of owner |
| `%G` | Group name of owner |
| `%x` | Time of last access |
| `%y` | Time of last modification |
| `%z` | Time of last status change |

Example:

```bash
stat -c "%n %F %s bytes" myfile.txt
```

Output:

```
myfile.txt regular file 1234 bytes
```

---

### **3. Print Filesystem Information**

Use the `-f` or `--file-system` option to show filesystem details instead of file details.

```bash
stat -f myfile.txt
```

Output:

```
  File: "myfile.txt"
    ID: 100000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 1000000    Free: 800000     Available: 750000
Inodes: Total: 500000     Free: 480000
```

Explanation:

- **ID**: Filesystem ID.
- **Namelen**: Maximum file name length.
- **Type**: Filesystem type.
- **Block size**: Size of each block.
- **Blocks**: Total, free, and available blocks.

---

### **4. Print Human-Readable Output**

Combine `stat` with commands like `awk` or `human-readable` options (if applicable in your Linux distribution).

Example:

```bash
stat -c "File: %n, Size: %s bytes, Modified: %y" myfile.txt
```

---

## **Real-World Examples**

### **1. Check File Timestamps**

To see when a file was last accessed or modified:

```bash
stat myfile.txt
```

### **2. Verify Inode Number**

Every file has an inode number. To display it:

```bash
stat -c "Inode: %i" myfile.txt
```

### **3. Find File Owner**

To display the owner of a file:

```bash
stat -c "Owner: %U (%u)" myfile.txt
```

### **4. Combine with `find`**

Find files and display their size:

```bash
find /path -type f -exec stat -c "%n %s bytes" {} \;
```

### **5. Get Filesystem Details**

To check the filesystem details for a file:

```bash
stat -f myfile.txt
```

---

## **Differences Between `stat` and Similar Commands**

1. **`ls`**: Shows basic file details like permissions, size, and ownership but not timestamps or inodes in detail.
2. **`du`**: Displays the disk space used by a file, not its metadata.
3. **`file`**: Identifies the type of file (e.g., text, binary) but doesn't provide ownership, size, or timestamps.

---

If you need more details about specific features or advanced use cases, let me know!

The `stat` command in Linux is a powerful utility used to display detailed information about files or directories, including file size, permissions, ownership, timestamps, and inode details. Below is an exhaustive overview of the `stat` command and its usage:

---

## **Basic Syntax**

```bash
stat [OPTION]... FILE...
```

The `stat` command outputs detailed metadata for the specified file or directory.

---

## **Default Output of `stat`**

When you run `stat` on a file or directory, the output includes the following details:

1. **File Name**: The name of the file.
2. **Size**: Size in bytes.
3. **Blocks**: Number of blocks allocated for the file on the disk.
4. **IO Block**: Size of each block (in bytes).
5. **File Type**: Type of file (regular file, directory, symbolic link, etc.).
6. **Device**: Device ID in hexadecimal and decimal.
7. **Inode**: Inode number of the file.
8. **Links**: Number of hard links pointing to the file.
9. **Access, Modify, Change**:
   - **Access**: Last time the file was accessed.
   - **Modify**: Last time the file content was modified.
   - **Change**: Last time the file's metadata (permissions, ownership, etc.) changed.

### Example:

```bash
stat myfile.txt
```

Output:

```
  File: myfile.txt
  Size: 1024       Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d   Inode: 131072     Links: 1
Access: 2024-12-28 12:00:00.000000000 +0000
Modify: 2024-12-27 10:30:00.000000000 +0000
Change: 2024-12-27 11:00:00.000000000 +0000
 Birth: -
```

---

## **Options and Usage**

### **1. File Information (Default Behavior)**

```bash
stat filename
```

This provides detailed metadata about the file.

---

### **2. File System Information**

Use `-f` or `--file-system` to display information about the filesystem containing the file.

```bash
stat -f filename
```

Example output:

```
  File: "filename"
    ID: 100000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 1000000    Free: 800000     Available: 750000
Inodes: Total: 500000     Free: 480000
```

Explanation:

- **ID**: Filesystem ID.
- **Namelen**: Maximum file name length.
- **Type**: Filesystem type (e.g., ext4, xfs).
- **Block size**: Size of filesystem blocks.
- **Blocks**: Total, free, and available blocks.

---

### **3. Custom Output Format**

The `-c` or `--format` option allows you to customize the output.

#### **Format Specifiers**

| Specifier | Description                |
| --------- | -------------------------- |
| `%n`      | File name                  |
| `%s`      | File size in bytes         |
| `%b`      | Number of blocks allocated |
| `%i`      | Inode number               |
| `%h`      | Number of hard links       |
| `%u`      | User ID of owner           |
| `%U`      | User name of owner         |
| `%g`      | Group ID of owner          |
| `%G`      | Group name of owner        |
| `%F`      | File type                  |
| `%x`      | Time of last access        |
| `%y`      | Time of last modification  |
| `%z`      | Time of last status change |

#### **Example 1: Show File Name and Size**

```bash
stat -c "%n %s bytes" myfile.txt
```

Output:

```
myfile.txt 1024 bytes
```

#### **Example 2: Show File Owner and Permissions**

```bash
stat -c "Owner: %U, Group: %G, Permissions: %A" myfile.txt
```

Output:

```
Owner: user, Group: group, Permissions: -rw-r--r--
```

---

### **4. Readable Time Format**

To display time in a more human-readable format, use:

```bash
stat -c "Last modified: %y" myfile.txt
```

---

### **5. Combine `stat` with `find`**

Use `find` to search for files and display their details with `stat`.

#### **Example: Display Metadata of All `.txt` Files**

```bash
find . -name "*.txt" -exec stat {} \;
```

#### **Example: Show Size and Modification Time for `.log` Files**

```bash
find /logs -name "*.log" -exec stat -c "%n %s %y" {} \;
```

---

## **Practical Examples**

### **1. Check File Timestamps**

Display the last access, modification, and metadata change times of a file:

```bash
stat myfile.txt
```

### **2. Verify Inode Number**

Every file has an inode number. To display it:

```bash
stat -c "Inode: %i" myfile.txt
```

### **3. Compare File Sizes**

Compare the sizes of multiple files:

```bash
stat -c "%n %s bytes" file1 file2
```

### **4. Display File Type**

```bash
stat -c "Type: %F" myfile.txt
```

Output:

```
Type: regular file
```

### **5. Display Filesystem Details**

```bash
stat -f /home
```

### **6. Display File Ownership**

To show the owner and group of a file:

```bash
stat -c "Owner: %U, Group: %G" myfile.txt
```

---

## **Differences Between `stat` and Similar Commands**

1. **`ls -l`**: Provides a summary of file details like permissions and ownership but not inode or timestamps.
2. **`du`**: Focuses on disk usage rather than file metadata.
3. **`file`**: Identifies the type of content inside a file (e.g., text or binary) but doesn't provide metadata like `stat`.

---

## **Advanced Tips**

1. **Check Hidden Files**:

   ```bash
   stat .hidden_file
   ```

2. **Use Aliases**:
   Create an alias for custom outputs:

   ```bash
   alias stat-size='stat -c "%n: %s bytes"'
   ```

   Then use:

   ```bash
   stat-size myfile.txt
   ```

3. **Readable Output for Human Sizes**:
   Combine with other commands (like `awk`) to convert sizes into human-readable format:
   ```bash
   stat -c "%n %s" myfile.txt | awk '{print $1, $2/1024 " KB"}'
   ```

---

### **Summary Cheat Sheet**

| Command                                 | Description                                  |
| --------------------------------------- | -------------------------------------------- |
| `stat file`                             | Display detailed file metadata               |
| `stat -f file`                          | Display filesystem information               |
| `stat -c "%n %s" file`                  | Show file name and size                      |
| `stat -c "%U %G" file`                  | Show owner and group                         |
| `stat -c "%x %y %z" file`               | Show access, modify, and change times        |
| `find . -name "*.txt" -exec stat {} \;` | Find and display metadata for specific files |

---

If you need more details about specific features or use cases, feel free to ask!

The `stat` command in Linux provides comprehensive information about files and directories, including size, permissions, ownership, timestamps, and file type. Below is an in-depth guide to the `stat` command, including syntax, examples, and advanced usage.

---

## **Basic Syntax**

```bash
stat [OPTION]... FILE...
```

### **Default Output**

The default `stat` output includes:

1. **File Name**: The name of the file.
2. **Size**: File size in bytes.
3. **Blocks**: Number of allocated blocks.
4. **IO Block**: Block size used for I/O operations.
5. **File Type**: Type of file (e.g., regular file, directory).
6. **Device**: Device ID in hexadecimal and decimal format.
7. **Inode**: Inode number of the file.
8. **Links**: Number of hard links to the file.
9. **Timestamps**:
   - **Access**: Last time the file was read.
   - **Modify**: Last time the file content was modified.
   - **Change**: Last time file metadata was modified.

### Example

```bash
stat myfile.txt
```

Output:

```
  File: myfile.txt
  Size: 2048       Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d   Inode: 131072     Links: 1
Access: 2024-12-27 14:00:00.000000000 +0000
Modify: 2024-12-26 12:00:00.000000000 +0000
Change: 2024-12-26 15:30:00.000000000 +0000
 Birth: -
```

---

## **Common Options**

### **1. Display Filesystem Information**

Use `-f` to display information about the filesystem instead of the file:

```bash
stat -f myfile.txt
```

Output:

```
  File: "myfile.txt"
    ID: 100000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 1000000    Free: 800000     Available: 750000
Inodes: Total: 500000     Free: 480000
```

### **2. Custom Format with `-c`**

The `-c` (or `--format`) option lets you customize the output using format specifiers.

Example:

```bash
stat -c "File: %n, Size: %s bytes, Modified: %y" myfile.txt
```

Output:

```
File: myfile.txt, Size: 2048 bytes, Modified: 2024-12-26 12:00:00.000000000 +0000
```

### Common Format Specifiers:

| Format | Description                               |
| ------ | ----------------------------------------- |
| `%n`   | File name                                 |
| `%s`   | File size (in bytes)                      |
| `%b`   | Number of blocks allocated                |
| `%i`   | Inode number                              |
| `%d`   | Device number (decimal)                   |
| `%F`   | File type (e.g., regular file, directory) |
| `%h`   | Number of hard links                      |
| `%u`   | User ID of the owner                      |
| `%U`   | User name of the owner                    |
| `%g`   | Group ID of the owner                     |
| `%G`   | Group name of the owner                   |
| `%x`   | Time of last access                       |
| `%y`   | Time of last modification                 |
| `%z`   | Time of last status change                |

---

## **Advanced Usage Examples**

### **1. Check File Size**

To display just the file name and size:

```bash
stat -c "%n %s bytes" myfile.txt
```

Output:

```
myfile.txt 2048 bytes
```

### **2. Check File Ownership**

To see the file owner’s username and group:

```bash
stat -c "Owner: %U (%u), Group: %G (%g)" myfile.txt
```

Output:

```
Owner: user (1000), Group: group (1000)
```

### **3. Find File Timestamps**

To display only the file's timestamps:

```bash
stat -c "Access: %x, Modify: %y, Change: %z" myfile.txt
```

Output:

```
Access: 2024-12-27 14:00:00.000000000 +0000, Modify: 2024-12-26 12:00:00.000000000 +0000, Change: 2024-12-26 15:30:00.000000000 +0000
```

### **4. Display File Type Only**

```bash
stat -c "File Type: %F" myfile.txt
```

Output:

```
File Type: regular file
```

### **5. Combining with Other Commands**

#### a. **Find Files and Display Details**

Use `find` to locate files and `stat` to display their details:

```bash
find /path -type f -exec stat {} \;
```

#### b. **Disk Usage of Files**

Use `stat` with `awk` to compute disk usage:

```bash
stat -c "%s %n" * | awk '{sum += $1} END {print "Total bytes: " sum}'
```

---

## **Differences Between `stat` and Similar Commands**

| Command | Description                                                                 |
| ------- | --------------------------------------------------------------------------- |
| `ls -l` | Displays file details but lacks inode, block size, or metadata change time. |
| `du`    | Shows disk usage of files, but no metadata details.                         |
| `file`  | Determines the type of a file but lacks size or timestamps.                 |

---

## **Real-World Use Cases**

### **1. Backup Automation**

Check the size and timestamps of files before including them in a backup:

```bash
stat -c "File: %n, Size: %s bytes, Modified: %y" /backup/*
```

### **2. File Integrity**

Verify inode and block allocation to detect possible corruption:

```bash
stat -c "File: %n, Inode: %i, Blocks: %b" myfile.txt
```

### **3. Check Last Access**

Monitor when a file was last accessed for cleanup:

```bash
stat -c "Last Access: %x" /tmp/*
```

### **4. Filesystem Analysis**

Analyze the filesystem where a file resides:

```bash
stat -f myfile.txt
```

---

## **Performance and Limitations**

1. **Large Directories**: Use `find` with `stat` for bulk operations to avoid command-line limits.
2. **Human-Readable Output**: `stat` doesn’t natively support human-readable formats (e.g., KB, MB). Combine with `awk` or other utilities for better readability.

---

### **Summary Cheat Sheet**

| Command                                    | Description                        |
| ------------------------------------------ | ---------------------------------- |
| `stat myfile.txt`                          | Display full details about a file. |
| `stat -f myfile.txt`                       | Display filesystem information.    |
| `stat -c "%n %s %y" myfile.txt`            | Display custom file details.       |
| `find /path -type f -exec stat {} \;`      | Combine `stat` with `find`.        |
| `stat -c "Owner: %U, Size: %s bytes" file` | Show file owner and size.          |

Let me know if you need more information!

The `stat` command in Linux is used to display detailed information about a file or directory. It provides a wealth of data beyond what `ls` offers, such as file sizes, timestamps, inode numbers, and file permissions. Here’s a comprehensive breakdown of the `stat` command:

---

## **Basic Syntax**

```bash
stat [OPTION]... FILE...
```

Where `FILE` is the name of the file or directory you want to get information about.

---

## **Output of `stat`**

When you run the `stat` command on a file or directory, it shows the following details:

1. **File Name**: The name of the file or directory.
2. **File Size**: The size of the file in bytes.
3. **Blocks**: The number of 512-byte blocks allocated to the file.
4. **IO Block**: The size of each block used by the file (usually 4096 bytes).
5. **File Type**: The type of file (regular file, directory, symbolic link, etc.).
6. **Device**: The device ID in both hexadecimal and decimal formats.
7. **Inode**: The inode number of the file, which is a unique identifier in the filesystem.
8. **Links**: The number of hard links to the file.
9. **Access, Modify, Change**:
   - **Access time (`atime`)**: The last time the file was accessed.
   - **Modify time (`mtime`)**: The last time the content of the file was modified.
   - **Change time (`ctime`)**: The last time the file’s metadata (e.g., permissions) was changed.

### **Example Output**:

```bash
stat myfile.txt
```

Output:

```
  File: myfile.txt
  Size: 1234       Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d   Inode: 131072     Links: 1
Access: 2024-12-28 12:00:00.000000000 +0000
Modify: 2024-12-25 15:00:00.000000000 +0000
Change: 2024-12-26 18:00:00.000000000 +0000
 Birth: -
```

---

## **Common Options**

### **1. Display File Information**

By default, `stat` shows detailed information about a single file:

```bash
stat myfile.txt
```

### **2. Use Custom Format**

The `-c` (or `--format`) option allows you to specify which fields to display in a custom format. You can combine several format specifiers.

#### Common Format Specifiers:

| Format | Description                      |
| ------ | -------------------------------- |
| `%n`   | File name                        |
| `%s`   | Size of the file (in bytes)      |
| `%i`   | Inode number                     |
| `%f`   | Raw mode (permissions in octal)  |
| `%F`   | File type (e.g., "regular file") |
| `%h`   | Number of hard links             |
| `%U`   | User name of the file’s owner    |
| `%G`   | Group name of the file’s owner   |
| `%y`   | Last modification time           |
| `%z`   | Time of last status change       |

Example: Display only the file name and modification time:

```bash
stat -c "%n %y" myfile.txt
```

Output:

```
myfile.txt 2024-12-25 15:00:00.000000000 +0000
```

### **3. Display Filesystem Information**

The `-f` or `--file-system` option shows information about the filesystem containing the file, rather than the file itself.

```bash
stat -f myfile.txt
```

Output:

```
  File: "myfile.txt"
    ID: 100000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 1000000    Free: 800000     Available: 750000
Inodes: Total: 500000     Free: 480000
```

Explanation:

- **ID**: Filesystem ID.
- **Namelen**: Maximum file name length.
- **Type**: Filesystem type (e.g., `ext4`, `ntfs`).
- **Block size**: Size of each block in bytes.
- **Blocks**: Number of total, free, and available blocks.
- **Inodes**: Number of total and free inodes.

### **4. Display Access, Modify, and Change Times in a Custom Format**

You can also use `stat` to get timestamps in a format you define. For example:

```bash
stat -c "File: %n, Modified: %y, Accessed: %x" myfile.txt
```

This shows:

```
File: myfile.txt, Modified: 2024-12-25 15:00:00.000000000 +0000, Accessed: 2024-12-28 12:00:00.000000000 +0000
```

### **5. Human-Readable Output**

To display file sizes in a human-readable format (e.g., KB, MB, GB), use `-h` with the `-c` option:

```bash
stat -c "File: %n, Size: %s bytes, Modified: %y" myfile.txt
```

---

## **Real-World Use Cases**

### **1. Checking File Ownership and Permissions**

To check who owns a file and its permissions:

```bash
stat myfile.txt
```

You will get details such as the user name (`%U`) and group name (`%G`).

### **2. Finding File Size**

To find the size of a file in bytes:

```bash
stat -c "%n %s bytes" myfile.txt
```

Output:

```
myfile.txt 1234 bytes
```

### **3. Using `stat` with `find` to Get Information on Multiple Files**

You can use `find` to locate files and pass them to `stat` to display detailed information:

```bash
find /path/to/dir -type f -exec stat -c "%n %s %y" {} \;
```

This will give you the file name, size, and last modification time for each file.

### **4. Displaying Inode Number**

You can print the inode number of a file:

```bash
stat -c "%i" myfile.txt
```

Output:

```
131072
```

### **5. Checking File Type**

To check the file type, use the `%F` specifier:

```bash
stat -c "%n is a %F file" myfile.txt
```

Output:

```
myfile.txt is a regular file
```

---

## **Comparison with Other Commands**

- **`ls`**: `ls` shows basic file information like permissions, size, and timestamps but not detailed information such as inode numbers or filesystem stats.
- **`du`**: The `du` command shows the disk usage of files and directories but doesn't provide information on ownership, permissions, or file timestamps.
- **`file`**: The `file` command determines the type of a file but doesn't show metadata like file size, access times, or inode numbers.

---

## **Additional Notes**

1. **Symbolic Links**: `stat` will show detailed information about symbolic links as well, including the target of the link.

   Example:

   ```bash
   stat symlink
   ```

2. **Displaying Metadata Only for Directories**:
   To get metadata about a directory, use `stat` just like for files. However, directories may show `-` for file content-related times like modification time if they are empty.

   Example:

   ```bash
   stat /path/to/directory
   ```

3. **File System Type with `-f`**:
   If you need to know about the filesystem the file resides in (e.g., ext4, NTFS), the `-f` option is very useful.

---

## **Summary Cheat Sheet**

| Option      | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| `stat FILE` | Show file details for `FILE`.                                 |
| `-c FORMAT` | Customize output format using `FORMAT` (e.g., `%n` for name). |
| `-f`        | Display filesystem information.                               |
| `-t`        | Output in a terse (non-human-readable) format.                |
| `-h`        | Output file size in human-readable format.                    |
| `-L`        | Show the information of the target file for symbolic links.   |

---

Let me know if you'd like further details or have specific use cases in mind!

Here’s an **even more detailed guide** on the `stat` command, expanding on every key aspect of its functionality, options, and advanced use cases.

---

## **What is `stat`?**

The `stat` command provides **comprehensive information about files or directories** in a Linux filesystem. This includes metadata like:

- File size
- Ownership
- Permissions
- Timestamps (Access, Modify, Change)
- Filesystem-related statistics
- Inode numbers and more

### **Core Concepts Related to `stat`**

1. **Access Time (`atime`)**: The last time the file was accessed (read).
2. **Modify Time (`mtime`)**: The last time the file content was modified.
3. **Change Time (`ctime`)**: The last time metadata (e.g., permissions, ownership) changed.
4. **Birth Time**: Some filesystems (e.g., NTFS) support file creation time, but not all Linux filesystems (e.g., ext4) store this information.

---

## **Detailed Output Breakdown**

When you run:

```bash
stat myfile.txt
```

### Example Output:

```
  File: myfile.txt
  Size: 1234       Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d   Inode: 131072     Links: 1
Access: 2024-12-28 12:00:00.000000000 +0000
Modify: 2024-12-25 15:00:00.000000000 +0000
Change: 2024-12-26 18:00:00.000000000 +0000
 Birth: -
```

### Field Explanations:

- **File**: Name of the file or directory.
- **Size**: File size in bytes.
- **Blocks**: Number of 512-byte blocks allocated for the file.
- **IO Block**: Optimal block size for file I/O.
- **File Type**: Indicates whether it’s a regular file, directory, symbolic link, etc.
- **Device**: Device on which the file resides (hexadecimal and decimal representation).
- **Inode**: A unique identifier for the file within the filesystem.
- **Links**: Number of hard links pointing to the file.
- **Access**: The last time the file was accessed (read).
- **Modify**: The last time the content of the file was modified.
- **Change**: The last time the file’s metadata (e.g., permissions, ownership) was changed.
- **Birth**: The file creation time, if supported by the filesystem. (On ext4, this often shows as `-`.)

---

## **Advanced Options and Use Cases**

### **1. Displaying Custom Output Format**

To tailor the output to show only specific details, use `-c` or `--format`:

```bash
stat -c "%n %s %y" myfile.txt
```

- `%n`: File name
- `%s`: File size
- `%y`: Last modification time

#### Full List of Format Specifiers:

| Format | Description                             |
| ------ | --------------------------------------- |
| `%n`   | File name                               |
| `%s`   | File size (in bytes)                    |
| `%b`   | Number of blocks allocated              |
| `%i`   | Inode number                            |
| `%h`   | Number of hard links                    |
| `%u`   | User ID of the owner                    |
| `%U`   | User name of the owner                  |
| `%g`   | Group ID of the owner                   |
| `%G`   | Group name of the owner                 |
| `%x`   | Time of last access                     |
| `%y`   | Time of last modification               |
| `%z`   | Time of last metadata change            |
| `%F`   | File type (e.g., regular file, symlink) |
| `%D`   | Device number (in hex)                  |

### Example:

```bash
stat -c "Name: %n, Size: %s bytes, Type: %F" myfile.txt
```

Output:

```
Name: myfile.txt, Size: 1234 bytes, Type: regular file
```

---

### **2. Display Filesystem Information**

To view filesystem-level details, use the `-f` (or `--file-system`) option:

```bash
stat -f myfile.txt
```

#### Output Example:

```
  File: "myfile.txt"
    ID: 100000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 1000000    Free: 800000     Available: 750000
Inodes: Total: 500000     Free: 480000
```

#### Explanation:

- **ID**: Filesystem ID.
- **Namelen**: Maximum file name length.
- **Type**: Filesystem type (e.g., ext4, xfs).
- **Block size**: Size of individual blocks in bytes.
- **Blocks**: Total, free, and available blocks on the filesystem.
- **Inodes**: Total and free inodes on the filesystem.

---

### **3. Combining `stat` with `find`**

You can use `find` to locate files and pass them to `stat` for detailed information:

```bash
find /path/to/dir -type f -exec stat -c "%n %s %y" {} \;
```

This command:

- Finds all files in `/path/to/dir`
- Runs `stat` on each file
- Displays file name, size, and last modification time.

---

### **4. Use `stat` with Symbolic Links**

By default, `stat` shows details about the symlink itself (not the target). To follow the symlink and show details of the target file, use the `-L` option:

```bash
stat -L mysymlink
```

---

### **5. Script Automation with `stat`**

`stat` is useful in shell scripting for retrieving file metadata programmatically.

#### Example: Check if a file has been modified in the last hour

```bash
if [[ $(stat -c %Y myfile.txt) -ge $(date -d '1 hour ago' +%s) ]]; then
  echo "File has been modified in the last hour."
fi
```

- `%Y`: Last modification time in seconds since the epoch.
- `date -d '1 hour ago' +%s`: Calculates the timestamp for one hour ago.

---

### **6. Comparing File Sizes**

If you want to compare the sizes of multiple files:

```bash
stat -c "%n %s bytes" file1 file2 file3
```

---

### **7. Display File Mode in Octal**

To view file permissions in octal format:

```bash
stat -c "%a" myfile.txt
```

Output:

```
644
```

---

## **Practical Examples**

### **1. Get Metadata for Multiple Files**

```bash
stat file1.txt file2.txt file3.txt
```

Displays detailed stats for each file.

---

### **2. Check if a File is a Directory**

```bash
stat -c "%F" myfile.txt
```

Output:

```
directory
```

---

### **3. Show Last Access Time**

```bash
stat -c "%n was last accessed on %x" myfile.txt
```

Output:

```
myfile.txt was last accessed on 2024-12-28 12:00:00.000000000 +0000
```

---

## **Advanced Notes**

1. **File Creation Time**:

   - Linux filesystems like ext4 often don’t store file creation (`birth`) times. Filesystems like NTFS and btrfs do support it.
   - To view file creation times, tools like `debugfs` or `lsattr` may be needed.

2. **`stat` vs `ls`**:

   - `ls` is user-friendly and provides basic file details.
   - `stat` is more detailed and suited for scripting or in-depth analysis.

3. **Compatibility**:
   - The exact output of `stat` may vary across distributions and versions. Always check the manual with `man stat`.

---

If you’d like further insights, examples, or use cases, feel free to ask!
