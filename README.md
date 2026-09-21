# FIM - File Integrity Monitor

**FIM (File Integrity Monitor)** is a project designed to detect changes in a file system.

The project monitors files inside a selected directory and detects events such as:

- File creation
- File modification
- File deletion

FIM is being developed through multiple versions, starting with a simple educational prototype and gradually moving toward a more complete File Integrity Monitoring system.

---

## Project Status

The project is currently under active development.

### Current Version

**FIMv1 — Education Version**

The first version of the project was created as an educational prototype for learning:

- Python
- File system operations
- Hashing
- Lists and dictionaries
- Functions
- Exception handling
- File monitoring
- Basic File Integrity Monitoring concepts

---

## How FIM Works

The main idea behind FIM is to create a **baseline** - a snapshot of the current state of the monitored files.

Future states of the file system are compared against this baseline.

```text
             Selected directory
                    │
                    ▼
               Scan files
                    │
                    ▼
             Calculate hashes
                    │
                    ▼
                Baseline
           path → SHA-512 hash
                    │
                    ▼
             Wait / Monitor
                    │
                    ▼
              Scan directory
                    │
                    ▼
          Calculate new hashes
                    │
                    ▼
           Compare baselines
              /      |       \
             /       |        \
          NEW     MODIFIED   DELETED
             \       |        /
              \      |       /
                     ▼
                Write report
```

---

## Versions

### FIMv1

The first educational version of the project.

The main workflow is:

```text
Directory
    ↓
File paths
    ↓
SHA-512 hashes
    ↓
Baseline
    ↓
Repeated scanning
    ↓
Comparison
    ↓
Report
```

FIMv1 uses polling: the monitored directory is periodically scanned again to detect changes.

More information:

**[`FIMv1/`](./FIMv1/)**

---

## Planned Development

Future versions may introduce:

- More efficient change detection
- File system event monitoring instead of continuous full scans
- File rename detection
- File and directory exclusion rules
- Configuration files
- More detailed reports
- Structured logging
- Persistent baseline storage
- Baseline integrity protection
- System service mode
- Better performance on large directories
- Improved error handling
- CLI interface
- Additional monitoring modes

---

## Project Architecture

As the project grows, its architecture will be divided into separate components and versions.

Possible future structure:

```text
FIM/
│
├── FIMv1/
│   ├── fim.py
│   └── README.md
│
├── FIMv2/
│   └── ...
│
├── docs/
│   └── ...
│
├── tests/
│   └── ...
│
└── README.md
```

---

## Technologies

Primary language:

- Python

Current standard libraries:

- `os`
- `hashlib`
- `datetime`
- `time`

The dependencies may change in future versions.

---

## Educational Purpose

FIM is not only being developed as a program, but also as a practical learning project.

During development, the project covers:

- File system operations
- Recursive directory traversal
- Functions
- Loops
- Lists
- Dictionaries
- Exception handling
- Binary file reading
- Cryptographic hashing
- State comparison
- Event logging
- Basic software project organization

---

## Security Context

File Integrity Monitoring is used as one of the mechanisms for monitoring the integrity of files.

A file modification can be a normal event, such as a software update, or something that requires further investigation.

> FIM itself does not determine whether a change is malicious.

It detects the change and provides information for further analysis.

---

## Project Goal

The main goal of the project is to gradually transform a simple Python prototype into a more complete File Integrity Monitoring system while maintaining the educational value of each version.

Each new version should address real limitations of the previous version rather than simply adding more features.

---

## Author

GitHub: https://github.com/zxcresp
