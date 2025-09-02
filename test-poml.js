#!/usr/bin/env node

/**
 * Simple validation script for POML files
 * This script checks basic syntax and file references
 */

const fs = require('fs');
const path = require('path');

// POML files to validate
const pomlFiles = [
  'examples/customer-support.poml',
  'examples/ecommerce-report.poml',
  'examples/image-analysis.poml'
];

// Data files referenced in POML files
const dataFiles = [
  'examples/data/customer_history.json',
  'examples/data/inventory.csv',
  'examples/data/knowledge_base.csv',
  'examples/data/market_trends.txt'
];

function validatePomlFiles() {
  console.log('Validating POML files...\\n');
  
  let allValid = true;
  
  // Check if POML files exist
  for (const file of pomlFiles) {
    if (fs.existsSync(file)) {
      console.log(`✓ Found ${file}`);
      
      // Basic XML validation could be added here
      const content = fs.readFileSync(file, 'utf8');
      if (!content.includes('<poml>') || !content.includes('</poml>')) {
        console.log(`✗ ${file} may not be a valid POML file (missing <poml> tags)`);
        allValid = false;
      }
    } else {
      console.log(`✗ Missing ${file}`);
      allValid = false;
    }
  }
  
  console.log('\\nValidating data files...\\n');
  
  // Check if data files exist
  for (const file of dataFiles) {
    if (fs.existsSync(file)) {
      console.log(`✓ Found ${file}`);
    } else {
      console.log(`✗ Missing ${file}`);
      allValid = false;
    }
  }
  
  console.log('\\n' + (allValid ? 'All files are present and valid!' : 'Some files are missing or invalid.'));
  return allValid;
}

// Run validation
if (require.main === module) {
  const isValid = validatePomlFiles();
  process.exit(isValid ? 0 : 1);
}