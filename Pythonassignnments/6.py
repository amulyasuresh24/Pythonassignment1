branches = ['EWT', 'ESI', 'BIG DATA', 'VLSI', 'ES']

branches.append('ASI')
print('Appended List is: ', branches)

branches.insert(3, 'IOT')
print('Inserted List is: ',branches)

branches.sort()
print('Sorted list: ', branches)
branches.sort(reverse = True)
print('Sorted list(Descending Order): ', branches)
