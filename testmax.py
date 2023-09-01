import fzmax

pyfzf = fzmax.FzfPrompt('fzf-tmux', ('--reverse', '-p 50%'))

print(pyfzf.options)

a = [x for x in range(10)]

multi_choice = pyfzf.prompt(a, '--multi')

assert type(multi_choice) == list, f"TypeError: expected list, got {type(multi_choice)}"

for x in multi_choice:
    print(x)

single = pyfzf.prompt(a)

assert type(single) == int, "TypeError: `single` should be `int`"
