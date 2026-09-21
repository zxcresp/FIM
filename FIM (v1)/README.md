# FIMv1

**FIMv1** is the first educational version of the **File Integrity Monitor** project.

The program monitors files inside a selected directory and detects three types of events:

```
NEW
MODIFIED
DELETED
```

This version is primarily designed for learning Python and understanding the basic principles of File Integrity Monitoring.

---

## Features

FIMv1 can:

- Accept a directory to monitor
- Recursively find files inside the directory
- Calculate a SHA-512 hash for each file
- Create a baseline
- Detect new files
- Detect modified files
- Detect deleted files
- Write events to a text report
- Record the time when an event was detected
- Continuously monitor the directory

---

## How It Works

### 1. Selecting a Directory

The user specifies a directory to monitor:

```
Enter a directory to check:
```

The program checks whether the specified directory exists.

---

### 2. Scanning Files

FIM uses `os.walk()` to recursively find files.

For example:

```
monitor/
├── file.txt
├── image.png
└── documents/
    ├── document.pdf
    └── notes.txt
```

The program will find all files, including files inside subdirectories.

---

### 3. Calculating Hashes

A SHA-512 hash is calculated for every file.

For example:

```
file.txt → 8a7f...c421
```

Files are read in binary mode in small chunks:

```python
with open(filepath, 'rb') as f:
    while chunk := f.read(4096):
        hash_sha512.update(chunk)
```

This prevents the entire file from being loaded into memory at once.

---

## Baseline

After the initial scan, the program creates a baseline.

The baseline stores a relationship between:

```
file path → file hash
```

For example:

```python
{
    "D:\\monitor\\file.txt": "hash1",
    "D:\\monitor\\image.png": "hash2"
}
```

The baseline represents the state of the monitored directory at a specific point in time.

---

## Detecting Changes

After creating the initial baseline, the program periodically scans the directory again and creates a new baseline.

The two states are then compared.

### NEW

A file exists in the new state but not in the old state:

```
old baseline:
A.txt

new baseline:
A.txt
B.txt
```

Result:

```
NEW: B.txt
```

---

### MODIFIED

A file exists in both states, but its hash has changed:

```
old:
A.txt → hash1

new:
A.txt → hash2
```

Result:

```
MODIFIED: A.txt
```

---

### DELETED

A file existed in the old state but is missing from the new state:

```
old:
A.txt
B.txt

new:
A.txt
```

Result:

```
DELETED: B.txt
```

---

## Monitoring Loop

After creating the initial baseline, the program starts continuous monitoring:

```
Scan
 ↓
Hash files
 ↓
Create current baseline
 ↓
Compare with previous baseline
 ↓
Write changes
 ↓
Replace old baseline
 ↓
Wait 5 seconds
 ↓
Repeat
```

The current monitoring interval is:

```python
time.sleep(5)
```

This means the directory is checked every 5 seconds.

---

## Reports

Detected changes are written to `report.txt`.

Example:

```
[2026-09-21 20:25:07] NEW: D:\monitor\file.txt
[2026-09-21 20:25:17] MODIFIED: D:\monitor\file.txt
[2026-09-21 20:25:27] DELETED: D:\monitor\file.txt
```

Each entry contains:

- Timestamp
- Event type
- Full file path

---

## Project Structure

The main logic of FIMv1 is divided into several functions:

```
get_files()
      │
      ▼
calculate_file_hash()
      │
      ▼
create_baseline()
      │
      ▼
compare_baselines()
      │
      ▼
write_report()
```

### `get_files()`

Recursively finds files inside the selected directory.

### `calculate_file_hash()`

Calculates the SHA-512 hash of a file.

### `create_baseline()`

Creates a dictionary containing:

```
path → hash
```

### `compare_baselines()`

Compares the old and new states and identifies:

```
NEW
MODIFIED
DELETED
```

### `write_report()`

Writes detected changes to the report file.

---

## Requirements

- Python 3.8+
- Python standard library

No external packages are required.

---

## Running

Run the program:

```bash
python fim.py
```

After starting the program, specify the directory to monitor and the location where the report should be saved.

For example:

```
Enter a directory to check: D:\monitor
Enter location where you want to save the report: D:\reports
```

The program will then start monitoring the selected directory.

---

## Current Limitations

FIMv1 is an educational prototype and has several limitations.

### Full Re-Hashing

Every 5 seconds, the program recalculates the hash of every accessible file.

For large directories, this can create significant:

- CPU usage
- Disk usage
- File system activity

---

### Polling

FIMv1 continuously scans the directory:

```
scan → wait → scan → wait → ...
```

This approach is simple to implement, but less efficient than using operating system file system events.

---

### Rename Detection

A file rename may be detected as two separate events:

```
DELETED: old_name.txt
NEW: new_name.txt
```

FIMv1 does not currently determine that these are the same file.

---

### Temporary Baseline

The baseline exists only while the program is running.

After the program terminates, the baseline is not preserved for the next execution.

---

### Report Location

The report should preferably be stored **outside the monitored directory**.

Otherwise, FIM may detect its own `report.txt` as a modified or newly created file.

---

### No Authentication

FIMv1 does not protect the report or baseline from modification by another process.

This is an educational version, so integrity protection mechanisms have not yet been implemented.

---

## Why SHA-512?

FIMv1 uses SHA-512 to generate a fixed-size value that can be used to compare file contents.

If the contents of a file change, its hash will normally change as well:

```
file
 ↓
SHA-512
 ↓
hash
```

During the next scan:

```
old hash != new hash
```

The program identifies the file as:

```
MODIFIED
```

---

## Educational Goals

FIMv1 was created to practice:

- Python functions
- `for` and `while` loops
- Lists
- Dictionaries
- File I/O
- Binary file reading
- `os.walk()`
- `os.path`
- Exception handling
- Hashing
- State comparison
- Basic logging
- Program architecture

---

## Future Versions

Future versions of the project will focus on improving the architecture, performance, and functionality of FIM.

Possible development path:

```
FIMv1
  ↓
FIMv2
  ↓
FIMv3
  ↓
Production-oriented FIM
```

Possible improvements include:

- Event-based monitoring
- Persistent baseline
- Rename detection
- File and directory exclusion rules
- Configuration file
- Improved logging
- CLI arguments
- Better error handling
- Optimized hashing
- Service/daemon mode
- Baseline integrity protection
- More advanced reporting

---

## Author

GitHub: https://github.com/zxcresp
