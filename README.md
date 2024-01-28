# Hadoop Distributed File System (HDFS) in Python

## Overview

This project is a simplified implementation of a Hadoop Distributed File System (HDFS) using Python. The system consists of a master server and multiple data nodes that collaborate to store and manage large files across a distributed network.

## Features

- **Centralized Metadata Management:** The master server maintains metadata about file locations, data nodes, and file structure.
  
- **Distributed Storage:** Data nodes store file chunks, and the master server coordinates file distribution and retrieval.

- **Basic File Operations:** Upload and download files to and from the distributed file system.

## Project Structure

- **`master.py`:** The master server that manages metadata and coordinates file operations.
  
- **`datanode.py`:** Data nodes that store and serve data chunks.
  
- **`client.py`:** A client to interact with the distributed file system.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/hadoop-dfs-python.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hadoop-dfs-python
    ```

### Usage

1. Start the master server:

    ```bash
    python master.py
    ```

2. Run one or more data nodes:

    ```bash
    python datanode.py
    ```

3. Interact with the distributed file system using the client:

    ```bash
    python client.py
    ```

## Contributing

Contributions are welcome! Feel free to open issues, propose new features, or submit pull requests to enhance the functionality of the Hadoop Distributed File System.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project is a simplified demonstration and should not be used in a production environment without significant enhancements and testing.
  
- Special thanks to the Python community and contributors to open-source libraries used in this project.
