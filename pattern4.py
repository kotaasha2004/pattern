def print_reverse_n_number_crown(N):
    for i in range(1, N + 1):
        # Generate first half numbers as a string
        first_half = ' '.join(map(str, range(1, i + 1)))
        
        # Generate spaces
        spaces = ' ' * (2 * (N - i))
        
        # Generate second half numbers as a string
        second_half = ' '.join(map(str, range(i, 0, -1)))
        
        # Combine and print the row
        print(f"{first_half}{spaces}{second_half}"))
