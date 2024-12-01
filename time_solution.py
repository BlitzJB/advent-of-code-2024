import time
import sys

if len(sys.argv) != 2:
    print("Usage: python time_solution.py <solution_file>")
    sys.exit(1)

solution_file = sys.argv[1]
start_time = time.time()

exec(open(solution_file).read())

end_time = time.time()
print(f"\nExecution time: {(end_time - start_time)*1000:.2f} ms") 