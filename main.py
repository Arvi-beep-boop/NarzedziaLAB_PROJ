import sys
import json
import yaml
import xml.etree.ElementTree as ET

def read_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    elif file_path.endswith('.xml'):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return ET.tostring(root, encoding='unicode')
    else:
        raise ValueError('Unsupported file format')

def write_file(data, file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    elif file_path.endswith('.xml'):
        root = ET.fromstring(data)
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='unicode')
    else:
        raise ValueError('Unsupported file format')

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        data = read_file(input_file)
        write_file(data, output_file)
        print(f"Conversion from {input_file} to {output_file} completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
