from src.user_input_helper import UserInputHelper
from src.fence_builder import FenceBuilder

debug_mode = True
inp = UserInputHelper()
fence_builder = FenceBuilder(min_side_length=3, debug_mode=debug_mode)

# main()
print('Welcome to Fence Builder!')
print('Enter "RUN" or "run" to start building your fence.')
print('Enter "exit" or "exit()" to stop and exit.')

user_input = inp.get_user_input(valid_inputs=['run'], ask_again=True)

if user_input.lower() == 'run':
    prompt = 'Please enter the available length of the fence in meters (a positive integer number)'
    available_fence_length = inp.get_positive_integer(prompt)
    optimal_a, optimal_b = fence_builder.get_optimal_fence_by_total_length_of_three_sides(available_fence_length)
    print(f'The most optimal fence is {optimal_a}х{optimal_b} meters (sides: a={optimal_a}m, b={optimal_b}m). ' \
          f'It encloses {optimal_a * optimal_b} square meters.')
