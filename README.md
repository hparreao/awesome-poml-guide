# Awesome POML Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A comprehensive guide and collection of examples for Prompt Orchestration Markup Language (POML) - Microsoft's innovative approach to structured prompt engineering.

## What is POML?

Prompt Orchestration Markup Language (POML) is a structured markup language developed by Microsoft for creating complex prompts for Large Language Models (LLMs). It provides a semantic, XML/HTML-inspired syntax that allows developers to organize prompt components logically and hierarchically.

POML addresses critical limitations in traditional prompt engineering methods like string concatenation and ad-hoc formatting by introducing:

- **Structured Semantic Components**: Logical organization of prompt elements
- **Data Integration**: Native support for external data (documents, tables, images)
- **Template Engine**: Dynamic variables and control structures
- **Styling System**: Consistent formatting and presentation rules

## POML Tag Reference

| Tag | Purpose |
| --- | --- |
| `<role>` | System message, persona, or general guidelines |
| `<task>` | Main instruction for the task to be performed |
| `<example>` | Few-shot learning examples |
| `<document>` / `<table>` / `<img>` | External data integration |
| `<let>` | Variable declaration and definition |
| `<output-format>` | Response structure instructions |
| `<stylesheet>` | Global styling and formatting settings |

## Installation and Setup

### Visual Studio Code Extension

Install the POML extension from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=microsoft.poml) or manually through the `.vsix` file from the [GitHub releases page](https://github.com/microsoft/poml).

Configure your model provider settings in VS Code:
1. Open Settings (Ctrl + ,)
2. Search for "POML"
3. Set your provider, API key, and endpoint

Or add to your `settings.json`:
```json
{
  "poml.modelProvider": "openai",
  "poml.apiKey": "YOUR_API_KEY",
  "poml.endpoint": "https://api.openai.com/v1"
}
```

### Node.js/TypeScript SDK

```bash
npm install pomljs
```

### Python SDK

```bash
pip install poml
```

## Examples

This repository contains practical examples demonstrating various POML use cases:

### 1. Customer Support System
[examples/customer-support.poml](examples/customer-support.poml)

A customer support prompt that analyzes sentiment and prioritizes responses:
```xml
<poml>
  <stylesheet>
    tone: professional
    verbosity: concise
    language: en-US
  </stylesheet>
  
  <role>
    You are a specialized technical support assistant...
  </role>
  
  <context>
    <let name="customer_sentiment">{{ analyze_sentiment(customer_message) }}</let>
    <let name="priority_level">
      {% if customer_sentiment == 'frustrated' %}high{% else %}normal{% endif %}
    </let>
  </context>
  
  <task>
    Analyze the customer message and provide an appropriate response...
  </task>
  
  <data>
    <document src="./data/customer_history.json" format="structured"/>
    <table src="./data/knowledge_base.csv" columns="problem,solution,category"/>
  </data>
</poml>
```

### 2. E-commerce Report Generation
[examples/ecommerce-report.poml](examples/ecommerce-report.poml)

Generates business reports with data from multiple sources:
```xml
<poml>
  <stylesheet>
    format: business_report
    detail_level: executive
  </stylesheet>
  
  <role>
    Senior data analyst specializing in e-commerce metrics...
  </role>
  
  <task>
    Generate an executive performance report...
  </task>
  
  <data>
    <table src="./data/sales_data.xlsx" sheet="monthly_sales"/>
    <table src="./data/inventory.csv" columns="product_id,stock_level,category"/>
    <document src="./data/market_trends.txt"/>
  </data>
</poml>
```

### 3. Image Analysis
[examples/image-analysis.poml](examples/image-analysis.poml)

Analyze technical diagrams and images:
```xml
<poml>
  <data>
    <img src="./architecture_diagram.png" 
         alt="System architecture diagram" 
         processing="detailed_analysis" 
         focus_areas="structure,components,connections"/>
  </data>
</poml>
```

## Key Features

### Semantic Structure
POML organizes prompts into meaningful components that are easy to understand and maintain:
```xml
<role>Defines the AI's persona</role>
<task>Specifies the main objective</task>
<data>Integrates external information</data>
<output-format>Controls response structure</output-format>
```

### Data Integration
Native support for various data types:
- `<document>` for text files and structured data
- `<table>` for CSV, Excel, and database exports
- `<img>` for image analysis with vision models

### Template Engine
Dynamic content generation with:
- Variable interpolation: `{{ variable_name }}`
- Conditional logic: `{% if condition %}...{% endif %}`
- Loops: `{% for item in collection %}...{% endfor %}`
- Variable declarations: `<let name="var">value</let>`

### Styling System
Consistent formatting through `<stylesheet>`:
```xml
<stylesheet>
  tone: professional
  verbosity: concise
  language: en-US
  format: markdown
</stylesheet>
```

## Testing POML Prompts

### In Visual Studio Code
1. Create a `.poml` file
2. Use the integrated testing feature
3. Configure your model provider in settings
4. Run the prompt directly from the editor

### With SDKs
Node.js example:
```javascript
import { parsePoml } from 'pomljs';

const pomlContent = await parsePoml('./examples/customer-support.poml');
// Process with your LLM API
```

Python example:
```python
from poml import parse_poml

poml_content = parse_poml('./examples/ecommerce-report.poml')
# Process with your LLM API
```

## Benefits

- **Improved Productivity**: Up to 40%+ increase in development speed
- **Better Maintainability**: Modular structure enables easier updates
- **Enhanced Collaboration**: Clear separation of concerns for team development
- **Advanced Debugging**: Component-based structure simplifies troubleshooting
- **Version Control**: Native Git integration for prompt versioning
- **Scalability**: Stateless architecture supports horizontal scaling


## Resources

- [Official POML GitHub Repository](https://github.com/microsoft/poml)
- [Microsoft POML Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/poml)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=microsoft.poml)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Microsoft Research for developing the POML specification
- The open-source community for adopting and extending structured prompt engineering approaches


  <div align="center">

**Made with ❤️ by [Hugo Parreão]**

[⭐ Star this project](https://github.com/hparreao/awesome-poml-guide) • [🍴 Fork it](https://github.com/hparreao/awesome-poml-guide/fork) • [📢 Report Issues](https://github.com/hparreao/awesome-poml-guide/issues)

</div>
