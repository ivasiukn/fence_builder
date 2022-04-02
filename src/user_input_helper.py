import sys

class UserInputHelper:
    def get_user_input(self, prompt='> ', valid_inputs=[], ask_again=False):
        # convert to lovercase all valid inputs (if there are any)
        if valid_inputs:
            valid_inputs = [x.lower() for x in valid_inputs]

        user_input = input(prompt)

        if user_input.lower() in ('exit', 'exit()'):
            sys.exit(0)

        if valid_inputs and user_input.lower() not in valid_inputs:
            if ask_again:
                # recursive call to get the user input again
                return self.get_user_input(prompt, valid_inputs, ask_again)
            else:
                raise ValueError(f'Wrong user input: "{user_input}".')

        return user_input

    def get_positive_integer(
            self,
            prompt='Please enter a positive integer number',
            wrong_input_message='is not a positive integer number',
            ask_again=True):

        # do not use recursive feature of get_user_input() here
        user_input = self.get_user_input(f'{prompt} > ')

        if user_input.isnumeric():
            return int(user_input)
        else:
            short_message = f'"{user_input}" {wrong_input_message}.'

            if ask_again:
                print(short_message)
                # recursive call to get the user input again
                return self.get_positive_integer(prompt, wrong_input_message)
            else:
                raise ValueError(f'Wrong user input, {short_message}')
