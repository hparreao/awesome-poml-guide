#!/usr/bin/env python3

"""
Simple validation script for POML files
This script checks basic syntax and file references
"""

import os

# POML files to validate
poml_files = [
    'examples/customer-support.poml',
    'examples/ecommerce-report.poml',
    'examples/image-analysis.poml'
]

# Data files referenced in POML files
data_files = [
    'examples/data/customer_history.json',
    'examples/data/inventory.csv',
    'examples/data/knowledge_base.csv',
    'examples/data/market_trends.txt'
]

def validate_poml_files():
    print('Validating POML files...\n')
    
    all_valid = True
    
    # Check if POML files exist
    for file in poml_files:
        if os.path.exists(file):
            print(f'✓ Found {file}')
            
            # Basic XML validation could be added here
            with open(file, 'r') as f:
                content = f.read()
                if '<poml>' not in content or '</poml>' not in content:
                    print(f'✗ {file} may not be a valid POML file (missing <poml> tags)')
                    all_valid = False
        else:
            print(f'✗ Missing {file}')
            all_valid = False
    
    print('\nValidating data files...\n')
    
    # Check if data files exist
    for file in data_files:
        if os.path.exists(file):
            print(f'✓ Found {file}')
        else:
            print(f'✗ Missing {file}')
            all_valid = False
    
    print('\n' + ('All files are present and valid!' if all_valid else 'Some files are missing or invalid.'))
    return all_valid

# Run validation
if __name__ == '__main__':
    is_valid = validate_poml_files()
    exit(0 if is_valid else 1)