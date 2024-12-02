# Day 2: Red-Nosed Reports

## Problem Description

The challenge involves analyzing safety reports from the Red-Nosed reactor. Each report consists of a list of numbers (levels) that need to be validated against specific safety criteria:
1. Part 1: Identify safe reports based on strictly increasing/decreasing patterns
2. Part 2: Account for the Problem Dampener that can remove one problematic level

## Approach

### Part 1: Basic Safety Validation
```python
def is_safe(report_data: list[int]):
    if len(report_data) == 1:
        return True
        
    movement_direction = "increasing" if report_data[0] < report_data[1] else "decreasing"

    for i in range(len(report_data) - 1):
        if report_data[i] == report_data[i + 1]:
            return False
        
        new_movement_direction = "increasing" if report_data[i] < report_data[i + 1] else "decreasing"
        if new_movement_direction != movement_direction:
            return False
        
        if not (1 <= abs(report_data[i] - report_data[i + 1]) <= 3):
            return False

    return True
```
- Read input file and parse each line into lists of integers
- Implement safety validation function that checks:
  - Consistent direction (all increasing or all decreasing)
  - Adjacent level differences between 1 and 3
  - No equal adjacent levels
- Count total number of safe reports using map and sum

### Part 2: Problem Dampener Implementation
```python
def is_any_safe(report_data: list[int]):
    for i in range(len(report_data)):
        if is_safe(report_data[:i] + report_data[i + 1:]):
            return True
    return False
```
- Extends part 1's solution to handle the Problem Dampener feature
- For each report, tries removing each level one at a time
- If any resulting sequence is safe, the report is considered safe
- Uses list slicing to create new sequences without the removed level
- Brute force approach that checks all possible single-level removals

## Notes

- Input parsing handles space-separated integers
- Early returns optimize validation checks
- Solution leverages functional programming with map and lambda functions
- Careful handling of edge cases (single-element lists)
- Part 2 uses a brute force approach that could be optimized

## Performance

- Part 1: 2.26 ms
- Part 2: 4.08 ms

## Future Improvements

- Optimize part 2's brute force approach
