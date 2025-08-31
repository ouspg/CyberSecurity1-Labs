# Flag Generator

The Flag Generator is a CLI application designed to create dynamic flags for hacking labs. It supports injecting unique flags into multiple lab environments using a plugin-based architecture.

## Features

- **Dynamic Flag Generation:** Generates unique flags for each user or email.
- **Plugin Architecture:** Easily extendable to support new labs by adding plugins.
- **Configurable:** Uses a configuration file for logging and other settings.
- **Batch Processing:** Generate flags for a single user or a list of users from a file.
- **Export:** Save generated flags to a JSON file for later use.

## Directory Structure

```bash
flag_generator/
│
├── app/
│   ├── main.py           # Main CLI entry point
│   ├── generator.py      # Flag generation logic
│   ├── injector.py       # Flag injection logic
│   ├── utils/            # Helper modules (config, logger, etc.)
│   ├── labs/             # Lab plugins (metasploit, priv_esc, etc.)
│   ├── config.ini        # App configuration
│   ├── requirements.txt  # Python dependencies
│   └── README.md         # This file
├── flags.json            # Example output file
├── output.json           # Example output file
```

## Usage

### Generate and Inject Flags for a Single Email

```sh
python -m app.main --email user@example.com
```

Flags are only injected for a single email

### Export Flags to JSON

Add the `--export` option to save the generated flags:

```sh
python -m app.main --email user@example.com --export flags.json
python -m app.main --file emails.txt --export flags.json
```

## Configuration

Edit `app/config.ini` to set logging levels and other options:

```ini
[logging]
level=DEBUG
```

## Requirements

- Python 3.10+
- See `app/requirements.txt` for dependencies.

## Development

Install dependencies:

```sh
pip install -r app/requirements.txt
```

## Developer Guide: Creating and Integrating Lab Plugins

The Flag Generator is designed with extensibility in mind. You can add support for new labs by developing plugins that follow a simple interface. This section outlines the recommended approach for creating, configuring, and integrating new lab plugins.

### Plugin Structure

Each plugin is a Python package (folder) inside `app/labs/`. The typical structure for a plugin is:

```
app/labs/
└── my_lab/
    ├── __init__.py      # Plugin implementation
    └── config.ini       # Lab-specific configuration (optional)
```

### Implementing a Plugin

1. **Create the Plugin Folder:**  
   Inside `app/labs/`, create a new directory for your lab (e.g., `my_lab/`).

2. **Define Tasks:**  
   In `__init__.py`, define one or more subclasses of the `Task` base class. Each subclass should represent a specific task or challenge in your lab.  
   - Each `Task` subclass must override the `inject()` method, which is responsible for injecting the generated flag into the lab environment.
  
3. **Bundle Tasks in a Lab:**  
   Implement a `create_lab()` function in your plugin’s `__init__.py`. This function should instantiate your `Task` objects, bundle them into a `Lab` object, and return it.  
   This function is called automatically when the application discovers plugins.
    - Set the required attributes such as `task_id` and `lab_id` for each task. These are important and used for generating dynamic flags.

4. **Configuration (Optional):**  
   If your lab requires specific configuration, add a `config.ini` file in your plugin directory. You can access these settings from your plugin code.

For details, you can look at the included lab plugins
