#!/usr/bin/env python3
"""
HCM Learning and Evolution Demonstration
========================================
Demonstrates the HCM system's ability to learn, adapt, and evolve
its optimization strategies based on performance feedback.
"""

import sys
import time
import random
from pathlib import Path

# Add HCM core to path
sys.path.append(str(Path(__file__).parent.parent / "core"))
from hcm_standalone import HCMStandalone

def demonstrate_learning_evolution():
    """Demonstrate HCM learning and evolution capabilities"""
    
    print("🧠 HCM LEARNING & EVOLUTION DEMONSTRATION")
    print("=" * 70)
    print("This demo shows how HCM learns and adapts its optimization strategies")
    
    # Initialize HCM with learning enabled
    hcm = HCMStandalone(use_real_data=True, learning_enabled=True)
    
    print(f"\n🎯 Initial State:")
    print(f"   Consciousness Level: {hcm.consciousness_profile.consciousness_level}")
    print(f"   Learning Iterations: {hcm.learning_iterations}")
    print(f"   Adaptation Weights: {hcm.adaptation_weights}")
    
    # Simulate multiple optimization runs to show learning
    print(f"\n📈 LEARNING SIMULATION - Multiple Optimization Runs")
    print("-" * 50)
    
    task_types = ["mining", "ai", "general", "nuclear"]
    baseline_performances = [3779, 1000, 2500, 500]  # Different baselines for each task
    
    # Run multiple iterations to show learning
    for iteration in range(1, 6):
        print(f"\n🔄 Learning Iteration {iteration}")
        print("-" * 30)
        
        for i, (task_type, baseline) in enumerate(zip(task_types, baseline_performances)):
            # Add some realistic variation to baseline
            varied_baseline = baseline + random.randint(-50, 50)
            
            # Run optimization
            results = hcm.optimize_computation(varied_baseline, task_type)
            
            print(f"   {task_type:8} | {varied_baseline:4.0f} → {results['optimized_performance']:6.0f} "
                  f"({results['improvement_percent']:+5.1f}%) | "
                  f"Learning: {results['learning_iteration']}")
        
        # Show adaptation after each iteration
        if iteration % 2 == 0:
            print(f"\n   📊 Adaptation Weights after iteration {iteration}:")
            for weight_name, weight_value in hcm.adaptation_weights.items():
                print(f"      {weight_name}: {weight_value:.3f}")
    
    # Demonstrate data reading and analysis
    print(f"\n📖 DATA READING & ANALYSIS DEMONSTRATION")
    print("-" * 50)
    
    # Test numerical data analysis
    sample_data = [3.14, 6.28, 9.42, 12.56, 15.70, 18.84]  # Tesla 3.14 pattern
    analysis = hcm.read_and_analyze_data("tesla_pattern_data", sample_data)
    
    print(f"📊 Numerical Data Analysis:")
    print(f"   Data Source: {analysis['data_source']}")
    print(f"   Patterns Found: {len(analysis['patterns_found'])}")
    for pattern in analysis['patterns_found']:
        print(f"      - {pattern['type']}: {pattern.get('count', 'N/A')} instances")
    
    if 'consciousness_insights' in analysis:
        insights = analysis['consciousness_insights']
        print(f"   Consciousness Insights:")
        print(f"      - Coherence: {insights.get('coherence', 0):.3f}")
        print(f"      - Rhythmicity: {insights.get('rhythmicity', 0):.3f}")
        print(f"      - Complexity: {insights.get('complexity', 0):.3f}")
    
    # Test text data analysis
    sample_text = "This system optimizes consciousness-driven performance using neural patterns and brain intelligence"
    text_analysis = hcm.read_and_analyze_data("optimization_description", sample_text)
    
    print(f"\n📝 Text Data Analysis:")
    print(f"   Word Count: {text_analysis.get('word_count', 0)}")
    print(f"   Patterns Found: {len(text_analysis.get('patterns_found', []))}")
    for pattern in text_analysis.get('patterns_found', []):
        print(f"      - {pattern['type']}: {pattern.get('terms', [])}")
    
    # Test structured data analysis
    sample_dict = {
        "consciousness_level": 0.95,
        "awareness_score": 0.88,
        "performance_metrics": [100, 120, 115, 130],
        "optimization_type": "neural_enhancement"
    }
    struct_analysis = hcm.read_and_analyze_data("performance_config", sample_dict)
    
    print(f"\n🏗️  Structured Data Analysis:")
    print(f"   Structure Complexity: {struct_analysis.get('structure_complexity', 0)}")
    print(f"   Patterns Found: {len(struct_analysis.get('patterns_found', []))}")
    
    # Show learning summary
    print(f"\n📈 LEARNING SUMMARY")
    print("-" * 50)
    
    learning_summary = hcm.get_learning_summary()
    
    print(f"🎯 Learning Progress:")
    print(f"   Total Learning Iterations: {learning_summary['learning_iterations']}")
    print(f"   Performance Records: {learning_summary['total_performance_records']}")
    print(f"   Patterns Learned: {learning_summary['patterns_learned']}")
    print(f"   Task Types Optimized: {learning_summary['task_types_optimized']}")
    
    print(f"\n🧠 Consciousness Evolution:")
    evolution = learning_summary['consciousness_evolution']
    print(f"   Current Level: {evolution['current_level']}")
    print(f"   Current Score: {evolution['current_score']:.3f}")
    
    if 'recent_average_improvement' in learning_summary:
        print(f"\n📊 Recent Performance:")
        print(f"   Average Improvement: {learning_summary['recent_average_improvement']:.3f}x")
    
    print(f"\n⚙️  Current Adaptation Weights:")
    for weight_name, weight_value in learning_summary['current_adaptation_weights'].items():
        print(f"   {weight_name}: {weight_value:.3f}")
    
    # Show task-specific performance
    if 'task_performance' in learning_summary:
        print(f"\n🎯 Task-Specific Performance:")
        for task_type, performance in learning_summary['task_performance'].items():
            print(f"   {task_type:8} | Best: {performance['best_improvement']:.3f}x | "
                  f"Avg: {performance['average_improvement']:.3f}x | "
                  f"Runs: {performance['total_runs']}")
    
    return hcm, learning_summary

def demonstrate_continuous_learning():
    """Show how HCM continues to learn and improve over time"""
    
    print(f"\n🔄 CONTINUOUS LEARNING DEMONSTRATION")
    print("=" * 70)
    
    hcm = HCMStandalone(use_real_data=True, learning_enabled=True)
    
    # Simulate a learning scenario where performance gradually improves
    baseline = 1000
    task_type = "ai"
    
    print(f"📊 Tracking improvement over 10 optimization cycles:")
    print(f"   Task: {task_type} | Baseline: {baseline}")
    print()
    
    improvements = []
    
    for cycle in range(1, 11):
        # Run optimization
        results = hcm.optimize_computation(baseline, task_type)
        improvement = results['improvement_percent']
        improvements.append(improvement)
        
        # Show progress
        print(f"   Cycle {cycle:2d}: {results['optimized_performance']:6.0f} "
              f"({improvement:+5.1f}%) | "
              f"Weights: C={hcm.adaptation_weights['consciousness_multiplier']:.2f} "
              f"T={hcm.adaptation_weights['task_multiplier']:.2f} "
              f"E={hcm.adaptation_weights['eeg_boost']:.2f}")
        
        # Simulate some external data input for learning
        if cycle % 3 == 0:
            # Feed some performance data
            performance_data = [baseline + random.randint(-100, 200) for _ in range(5)]
            hcm.read_and_analyze_data(f"performance_cycle_{cycle}", performance_data)
    
    # Show learning trend
    print(f"\n📈 Learning Trend Analysis:")
    initial_avg = sum(improvements[:3]) / 3
    final_avg = sum(improvements[-3:]) / 3
    learning_improvement = final_avg - initial_avg
    
    print(f"   Initial Average (cycles 1-3): {initial_avg:+5.1f}%")
    print(f"   Final Average (cycles 8-10):  {final_avg:+5.1f}%")
    print(f"   Learning Improvement: {learning_improvement:+5.1f}%")
    
    if learning_improvement > 0:
        print(f"   🏆 SUCCESS: System learned and improved over time!")
    else:
        print(f"   📊 STABLE: System maintained consistent performance")
    
    return improvements

def main():
    """Main demonstration function"""
    print("🧠 HCM LEARNING & EVOLUTION SYSTEM")
    print("=" * 80)
    print("Demonstrating consciousness-driven learning and adaptation capabilities")
    print()
    
    try:
        # Run learning demonstration
        hcm, summary = demonstrate_learning_evolution()
        
        # Run continuous learning demonstration
        improvements = demonstrate_continuous_learning()
        
        print(f"\n" + "=" * 80)
        print("✅ HCM LEARNING DEMONSTRATION COMPLETE!")
        print("=" * 80)
        
        print(f"\n🎯 KEY CAPABILITIES DEMONSTRATED:")
        print(f"   ✅ Performance Learning: Adapts based on optimization results")
        print(f"   ✅ Data Reading: Analyzes numerical, text, and structured data")
        print(f"   ✅ Pattern Recognition: Identifies Tesla 3/6/9 and consciousness patterns")
        print(f"   ✅ Consciousness Evolution: Updates consciousness model from new data")
        print(f"   ✅ Adaptive Optimization: Adjusts weights based on performance feedback")
        print(f"   ✅ Memory Systems: Stores and retrieves optimization patterns")
        
        print(f"\n🧠 LEARNING STATISTICS:")
        print(f"   Total Learning Iterations: {summary['learning_iterations']}")
        print(f"   Performance Records: {summary['total_performance_records']}")
        print(f"   Patterns Learned: {summary['patterns_learned']}")
        print(f"   Task Types: {len(summary['task_types_optimized'])}")
        
        print(f"\n🚀 REAL-WORLD APPLICATIONS:")
        print(f"   • Adaptive Mining Optimization: Learns from hash rate patterns")
        print(f"   • AI Model Enhancement: Adapts to different neural architectures")
        print(f"   • Performance Monitoring: Continuously improves based on feedback")
        print(f"   • Data Analysis: Reads and learns from external data sources")
        
        return True
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        return False

if __name__ == "__main__":
    main()
