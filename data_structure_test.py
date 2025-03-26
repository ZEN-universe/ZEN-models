import os
import json

# Paths
DATASET_DIR = "data"  # Root dataset directory
REQUIRED_FILES_FOLDERS = {
    'energy_system': ['base_units.json', 'set_nodes.csv', 'set_edges.csv'],
    'set_technologies': ['set_conversion_technologies', 'set_storage_technologies', 'set_transport_technologies'],
    'set_carriers': []
}

def check_file_exists(path, filename):
    """Check if a file exists in a directory."""
    return os.path.isfile(os.path.join(path, filename))

def check_folder_exists(path, folder):
    """Check if a folder exists in a directory."""
    return os.path.isdir(os.path.join(path, folder))

def check_folder_structure(path, folder_structure):
    """Check if the folder structure is correct and required files exist."""
    for folder, required_folders in folder_structure.items():
        folder_path = os.path.join(path, folder)

        if not os.path.isdir(folder_path):
            raise ValueError(f"Error: Missing folder {folder} at {folder_path}")

        # Check for required files in each folder
        for required_folder in required_folders:
            if not check_folder_exists(folder_path, required_folder):
                raise ValueError(f"Error: Missing file {required_folder} in {folder_path}")
        # Recursively check subfolders if they exist
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)
            check_subfolder_structure(subfolder_path)

def check_subfolder_structure(subfolder_path):
    """ ensures that the subfolders are correctly structured"""
    if os.path.isdir(subfolder_path):
        for subsubfolder in os.listdir(subfolder_path):
            subsubfolder_path = os.path.join(subfolder_path, subsubfolder)
            check_subfolder_structure(subsubfolder_path)
        check_csv_files_only(subfolder_path)

def check_csv_files_only(path):
    """Ensure all files in the folder are .csv files or attributes.json."""
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isdir(file_path):
            continue  # Skip directories
        if not (filename.endswith('.csv') or filename == 'attributes.json'):
            raise ValueError(
                f"Error: Invalid file {filename} in {path}. Only .csv and attributes.json files are allowed.")


def validate_system_json(path):
    """Ensure system.json exists and is a valid JSON file."""
    system_json_path = os.path.join(path, 'system.json')
    if not check_file_exists(path, 'system.json'):
        raise ValueError(f"Error: Missing system.json in {path}")
    else:
        try:
            with open(system_json_path, 'r') as file:
                json.load(file)  # Try to load and validate the JSON file
        except json.JSONDecodeError:
            raise ValueError(f"Error: Invalid JSON in system.json at {system_json_path}")


def validate_config(path):
    """Ensure config.json exists and is valid."""
    config_path = os.path.join(path, 'config.json')
    if not check_file_exists(path, 'config.json'):
        raise ValueError(f"Error: Missing config.json at {path}")
    else:
        try:
            with open(config_path, 'r') as file:
                json.load(file)  # Try to load and validate the JSON file
        except json.JSONDecodeError:
            raise ValueError(f"Error: Invalid JSON in config.json at {config_path}")

def validate_scenarios(path):
    """ ensures scenarios.json is valid if it exists """
    scenarios_path = os.path.join(path, 'scenarios.json')
    if check_file_exists(path, 'scenarios.json'):
        try:
            with open(scenarios_path, 'r') as file:
                json.load(file)  # Try to load and validate the JSON file
        except json.JSONDecodeError:
            raise ValueError(f"Error: Invalid JSON in scenarios.json at {scenarios_path}")

def validate_dataset(path=DATASET_DIR,dataset_name=None):
    """Main function to validate the dataset structure."""
    # assert that path exists
    assert (os.path.exists(path)), f"Error: Invalid dataset path: {path}"
    # validate config.json
    validate_config(path)
    # validate data folder
    if dataset_name is None:
        # assert that only two elements are in the path: config.json and the dataset
        assert (len(os.listdir(path)) == 2), "Error: Only config.json and one dataset folder are allowed."
        dataset_name = [f for f in os.listdir(path) if f != "config.json"][0]
    dataset_path = os.path.join(path, dataset_name)
    # Validate system file
    validate_system_json(dataset_path)
    # validate scenarios file
    validate_scenarios(dataset_path)
    # Validate energy system files
    energy_system_path = os.path.join(dataset_path, 'energy_system')
    assert os.path.isdir(energy_system_path), "Error: No energy system found."
    for required_file in REQUIRED_FILES_FOLDERS['energy_system']:
        if not check_file_exists(energy_system_path, required_file):
            raise ValueError(f"Error: Missing required file {required_file} in {energy_system_path}")
    check_folder_structure(dataset_path, {'set_technologies': REQUIRED_FILES_FOLDERS['set_technologies'],
                                  'set_carriers': REQUIRED_FILES_FOLDERS['set_carriers']})

if __name__ == "__main__":
    try:
        validate_dataset()
    except ValueError as e:
        print(e)
        exit(1)  # Exit with error code 1 to indicate failure
    print("Dataset structure is valid.")
