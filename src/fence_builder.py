import sys

class FenceBuilder:
    def __init__(self, min_side_length=1, debug_mode=False):
        self.min_side_length = min_side_length
        self.debug_mode = debug_mode

    def get_optimal_fence_by_total_length_of_three_sides(self, fence_length):
        if fence_length < (3 * self.min_side_length):
            print(f"Unfortunately it's not enough to build a fence. " \
                  f"You need at least {3 * self.min_side_length} meters of availabel fence.")
            sys.exit(0)

        max_a = int((fence_length - self.min_side_length) / 2)

        optimal_a = 0
        optimal_b = 0
        optimal_area = optimal_a * optimal_b

        for a in range(self.min_side_length, max_a + 1, self.min_side_length):
            b = fence_length - (2 * a)
            area = a * b

            if self.debug_mode:
                print(f'possible fence: {a} x {b} = {area}')

            if area < optimal_area:
                break;

            if area > optimal_area:
                optimal_a = a
                optimal_b = b
                optimal_area = area

        return optimal_a, optimal_b
