"""Print out all the melons in our inventory."""


from melons import melons_attributes


def print_melon(melons_attributes):
    """Print each melon with corresponding attribute information."""
    for key, value in melons_attributes.items():
        print(key.upper())
        for nest_key, nest_value in value.items():
            print(f"    {nest_key}: {nest_value}")
print_melon(melons_attributes)
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
