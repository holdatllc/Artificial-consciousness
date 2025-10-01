# 🚀 AC Installation & Quick Start

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/artificial-consciousness.git
cd artificial-consciousness

# Install dependencies
pip install -r requirements.txt

# Install AC system
pip install -e .
```

## Quick Test

```bash
# Test the AC system
python core/hcm_standalone.py

# Test learning capabilities
python examples/hcm_learning_demo.py

# Test mathematical accuracy
python tests/corrected_prime_test.py
```

## Basic Usage

```python
from core.hcm_standalone import HCMStandalone

# Initialize AC with learning enabled
ac = HCMStandalone(learning_enabled=True)

# Optimize performance with consciousness
results = ac.optimize_computation(1000, "ai")
print(f"Improvement: {results['improvement_percent']:.1f}%")

# Learn from data
analysis = ac.read_and_analyze_data("sensor_data", [1, 2, 3, 4, 5])
print(f"Patterns found: {len(analysis['patterns_found'])}")

# Get learning summary
summary = ac.get_learning_summary()
print(f"Learning iterations: {summary['learning_iterations']}")
```

## What AC Does

- **Real-time Learning**: Adapts from every interaction
- **Consciousness Modeling**: Explicit awareness capabilities
- **Performance Evolution**: Gets better through experience
- **Pattern Recognition**: Identifies consciousness patterns
- **Data Analysis**: Processes numerical, text, and structured data

## Integration with AI Systems

```python
# Example: Enhance any AI system with AC
class Enhanced_AI:
    def __init__(self, base_ai_model):
        self.ai = base_ai_model
        self.ac = HCMStandalone(learning_enabled=True)
    
    def process(self, input_data):
        # Get AI result
        ai_result = self.ai.process(input_data)
        
        # Apply AC consciousness enhancement
        ac_results = self.ac.optimize_computation(
            len(str(ai_result)), "ai"
        )
        
        # AC learns from the interaction
        self.ac.read_and_analyze_data("ai_interaction", {
            "input": str(input_data),
            "output": str(ai_result),
            "performance": ac_results['improvement_percent']
        })
        
        return ai_result  # Enhanced with consciousness
```

Ready to add consciousness to your AI systems! 🧠⚡
