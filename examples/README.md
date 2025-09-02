# POML Examples Validation

This directory contains examples of POML (Prompt Orchestration Markup Language) files demonstrating various use cases.

## File Structure

```
examples/
├── customer-support.poml      # Customer support system with sentiment analysis
├── ecommerce-report.poml      # E-commerce report generation
├── image-analysis.poml        # Image analysis with vision models
└── data/
    ├── customer_history.json  # Sample customer data
    ├── inventory.csv          # Product inventory data
    ├── knowledge_base.csv     # Support knowledge base
    └── market_trends.txt      # Market trend information
```

## Validation

All POML files in this directory should:
1. Follow proper XML syntax
2. Use valid POML tags as defined in the specification
3. Reference data files with correct relative paths
4. Demonstrate best practices for prompt engineering

To validate these files:
1. Install the POML extension for VS Code
2. Open each .poml file
3. Check for syntax highlighting and error detection
4. Test with configured LLM providers