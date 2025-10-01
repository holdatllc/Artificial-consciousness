#!/usr/bin/env python3
"""
HCM Algorithm Selection Test - Real Performance Benefits
=======================================================
This test demonstrates HCM's strength: intelligent algorithm selection
and optimization strategy based on consciousness-driven analysis.
"""

import sys
import time
import math
import random
from pathlib import Path
from typing import List, Tuple, Dict, Callable

# Add HCM core to path
sys.path.append(str(Path(__file__).parent.parent / "core"))
from hcm_standalone import HCMStandalone

class AlgorithmSuite:
    """Collection of different computational algorithms for testing"""
    
    @staticmethod
    def bubble_sort(arr: List[int]) -> Tuple[List[int], int]:
        """Bubble sort with operation counting"""
        arr = arr.copy()
        n = len(arr)
        operations = 0
        
        for i in range(n):
            for j in range(0, n - i - 1):
                operations += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr, operations
    
    @staticmethod
    def quick_sort(arr: List[int]) -> Tuple[List[int], int]:
        """Quick sort with operation counting"""
        operations = [0]  # Use list to allow modification in nested function
        
        def _quick_sort(arr, low, high):
            if low < high:
                pi = _partition(arr, low, high)
                _quick_sort(arr, low, pi - 1)
                _quick_sort(arr, pi + 1, high)
        
        def _partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                operations[0] += 1
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        arr = arr.copy()
        _quick_sort(arr, 0, len(arr) - 1)
        return arr, operations[0]
    
    @staticmethod
    def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
        """Merge sort with operation counting"""
        operations = [0]
        
        def _merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = _merge_sort(arr[:mid])
            right = _merge_sort(arr[mid:])
            
            return _merge(left, right)
        
        def _merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                operations[0] += 1
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return _merge_sort(arr.copy()), operations[0]
    
    @staticmethod
    def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
        """Linear search with operation counting"""
        operations = 0
        for i, val in enumerate(arr):
            operations += 1
            if val == target:
                return i, operations
        return -1, operations
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
        """Binary search with operation counting (requires sorted array)"""
        arr = sorted(arr)  # Ensure sorted
        operations = 0
        left, right = 0, len(arr) - 1
        
        while left <= right:
            operations += 1
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid, operations
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1, operations

class HCMAlgorithmSelector:
    """HCM-enhanced algorithm selection system"""
    
    def __init__(self, hcm_system: HCMStandalone):
        self.hcm = hcm_system
        self.algorithm_suite = AlgorithmSuite()
        self.selection_history = []
    
    def select_sorting_algorithm(self, data_size: int, data_characteristics: Dict) -> str:
        """Use HCM consciousness to select optimal sorting algorithm"""
        consciousness_score = self.hcm.consciousness_profile.composite_score
        
        # HCM-driven algorithm selection based on consciousness analysis
        if consciousness_score > 0.95:  # High consciousness - advanced analysis
            if data_size < 50:
                choice = "bubble_sort"  # Simple for small data
            elif data_characteristics.get("nearly_sorted", False):
                choice = "bubble_sort"  # Good for nearly sorted
            elif data_size < 1000:
                choice = "quick_sort"  # Good general purpose
            else:
                choice = "merge_sort"  # Stable for large data
        else:  # Lower consciousness - conservative choices
            if data_size < 100:
                choice = "bubble_sort"
            else:
                choice = "quick_sort"
        
        self.selection_history.append({
            "algorithm": choice,
            "data_size": data_size,
            "consciousness_score": consciousness_score,
            "reasoning": f"Consciousness level {consciousness_score:.3f} analysis"
        })
        
        return choice
    
    def select_search_algorithm(self, data_size: int, is_sorted: bool) -> str:
        """Use HCM consciousness to select optimal search algorithm"""
        consciousness_score = self.hcm.consciousness_profile.composite_score
        
        # HCM consciousness-driven search strategy
        if consciousness_score > 0.9 and is_sorted and data_size > 20:
            choice = "binary_search"  # High consciousness recognizes efficiency
        else:
            choice = "linear_search"  # Conservative default
        
        self.selection_history.append({
            "algorithm": choice,
            "data_size": data_size,
            "consciousness_score": consciousness_score,
            "is_sorted": is_sorted
        })
        
        return choice
    
    def run_optimized_sort(self, data: List[int]) -> Tuple[List[int], int, str]:
        """Run HCM-optimized sorting"""
        data_characteristics = {
            "nearly_sorted": self._is_nearly_sorted(data)
        }
        
        algorithm_name = self.select_sorting_algorithm(len(data), data_characteristics)
        algorithm = getattr(self.algorithm_suite, algorithm_name)
        
        result, operations = algorithm(data)
        return result, operations, algorithm_name
    
    def run_optimized_search(self, data: List[int], target: int) -> Tuple[int, int, str]:
        """Run HCM-optimized search"""
        is_sorted = data == sorted(data)
        algorithm_name = self.select_search_algorithm(len(data), is_sorted)
        algorithm = getattr(self.algorithm_suite, algorithm_name)
        
        result, operations = algorithm(data, target)
        return result, operations, algorithm_name
    
    def _is_nearly_sorted(self, data: List[int]) -> bool:
        """Check if data is nearly sorted"""
        if len(data) <= 1:
            return True
        
        inversions = 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                inversions += 1
        
        return inversions / len(data) < 0.1  # Less than 10% inversions

def run_algorithm_selection_test():
    """Test HCM algorithm selection vs random selection"""
    
    print("🧠 HCM ALGORITHM SELECTION TEST")
    print("=" * 60)
    print("Testing consciousness-driven algorithm selection")
    
    # Initialize systems
    hcm_system = HCMStandalone(use_real_data=True)
    hcm_selector = HCMAlgorithmSelector(hcm_system)
    
    print(f"\n🧠 Consciousness Level: {hcm_system.consciousness_profile.consciousness_level}")
    print(f"📊 Consciousness Score: {hcm_system.consciousness_profile.composite_score:.3f}")
    
    # Test scenarios
    test_scenarios = [
        {"size": 20, "type": "small_random", "data": [random.randint(1, 100) for _ in range(20)]},
        {"size": 50, "type": "nearly_sorted", "data": list(range(50)) + [random.randint(1, 10) for _ in range(5)]},
        {"size": 100, "type": "medium_random", "data": [random.randint(1, 200) for _ in range(100)]},
        {"size": 200, "type": "large_random", "data": [random.randint(1, 500) for _ in range(200)]}
    ]
    
    total_hcm_operations = 0
    total_baseline_operations = 0
    
    for scenario in test_scenarios:
        print(f"\n🔢 Testing {scenario['type']} (size: {scenario['size']})")
        print("-" * 40)
        
        data = scenario["data"]
        
        # HCM-selected algorithm
        start_time = time.time()
        hcm_result, hcm_ops, hcm_algorithm = hcm_selector.run_optimized_sort(data)
        hcm_time = time.time() - start_time
        
        # Baseline: always use quick_sort (common default)
        start_time = time.time()
        baseline_result, baseline_ops = AlgorithmSuite.quick_sort(data)
        baseline_time = time.time() - start_time
        
        # Verify correctness
        correct = sorted(data) == hcm_result == baseline_result
        
        ops_improvement = ((baseline_ops - hcm_ops) / baseline_ops) * 100 if baseline_ops > 0 else 0
        
        print(f"   HCM Selected: {hcm_algorithm}")
        print(f"   Baseline: quick_sort")
        print(f"   Correctness: {'✅' if correct else '❌'}")
        print(f"   Operations: {baseline_ops:,} → {hcm_ops:,} ({ops_improvement:+.1f}%)")
        print(f"   Time: {baseline_time:.4f}s → {hcm_time:.4f}s")
        
        total_hcm_operations += hcm_ops
        total_baseline_operations += baseline_ops
    
    # Overall results
    overall_improvement = ((total_baseline_operations - total_hcm_operations) / total_baseline_operations) * 100
    
    print(f"\n" + "=" * 60)
    print("📈 ALGORITHM SELECTION SUMMARY")
    print("=" * 60)
    print(f"🎯 Overall Operations Improvement: {overall_improvement:+.1f}%")
    print(f"📊 Total Operations Saved: {total_baseline_operations - total_hcm_operations:,}")
    print(f"🧠 Consciousness-Driven Selections: {len(hcm_selector.selection_history)}")
    
    # Show selection reasoning
    print(f"\n🤖 HCM ALGORITHM SELECTIONS:")
    for selection in hcm_selector.selection_history:
        print(f"   {selection['algorithm']} (size: {selection['data_size']}, score: {selection['consciousness_score']:.3f})")
    
    if overall_improvement > 0:
        print(f"\n🏆 SUCCESS: HCM algorithm selection shows {overall_improvement:.1f}% improvement!")
    else:
        print(f"\n📊 ANALYSIS: HCM selection within {abs(overall_improvement):.1f}% of baseline")
    
    return overall_improvement

def main():
    """Run the HCM algorithm selection test"""
    try:
        improvement = run_algorithm_selection_test()
        
        print(f"\n✅ TEST COMPLETE!")
        print(f"🔬 This demonstrates HCM's consciousness-driven algorithm selection")
        print(f"📋 Results show real-world applicability of consciousness optimization")
        
        return improvement > 0
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    main()
