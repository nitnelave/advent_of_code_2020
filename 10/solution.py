import operator
import math

adapters = sorted(list(map(int, open('input'))))

adapters = [0] + adapters + [max(adapters) + 3]

diffs = list(map(operator.sub, adapters[1:], adapters[:-1]))

print(diffs.count(1) * diffs.count(3))

# The input can be split into segments: every jump of 3 must be made, so every
# combination will include them. We can split every time and multiply the
# possibilities before and after the big jump. Each segment will consist of a
# consecutive number of adapters with a 1-joltage difference.
# Note that the problem is simplified by the absence of 2-joltage difference.
index_of_3 = [i for i, x in enumerate(diffs) if x == 3]
# The specific values of the adapters are not important, just the number of
# consecutive adapters.
# We add a fake 3-jump before the beginning of the list (index -1) to force the
# start from the (0) adapter.
segment_size = list(map(operator.sub, index_of_3, [-1] + index_of_3[:-1]))

combinations_per_size = [1, 1, 2]
def compute_combination_per_size(n):
    # Jump joltage by 1, 2 or 3.
    return (combinations_per_size[n - 1]
            + combinations_per_size[n - 2]
            + combinations_per_size[n - 3])
for i in range(3, max(segment_size)):
    combinations_per_size.append(compute_combination_per_size(i))

# s - 1 because of 0-based indexing.
combinations_per_segment = [combinations_per_size[s - 1] for s in segment_size]

print(math.prod(combinations_per_segment))
