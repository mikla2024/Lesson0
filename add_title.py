titles = []

title = input('Enter the first title: ')
titles.append(title)

while True:

	stop_ = input('\nDo you want to add another title Yes/No ').lower()
	if stop_ in ['y', 'yes']:
		title = input('\nEnter the title: ')
		titles.append(title)
	elif stop_ in ['n', 'no']:
		break
	else:
		print('\nUnknown command. Try one more time')
		continue
print('\nTitles are:')
for t in titles:
	print(f'{t}')
