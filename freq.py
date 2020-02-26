import sys

def frequency_calculation(word_counts,frequency,sentences):
	length = len(sentences)	
# For loop will calculate the frequency values and round it to 3 d.p.
	for keys, values in sorted(word_counts.items()):
		a = values/length
# The frequency values are appended to a list
		frequency.append(round(a,3))

def print_table(word_counts,frequency):
	i = 0
# The name of the output file is the same as the input however .out is concatenated to it
	file_output = open(sys.argv[1]+'.out','w')
# The 'sorted' sorts the dictionary in lexographic order
# This for loop will iterate over every item in both the list and dictionary and print them 
	for keys, items in sorted(word_counts.items()): 
		current_Freq = frequency[i]
		printing = ('{} {} {}\n'.format(keys,items,current_Freq))
		file_output.write(printing)
		i+=1
	file_output.close()

def frequency():
# Opening the user-inputted file (second arguement)
	file_input = open(sys.argv[1],'r')
	frequency = []
	sentences = file_input.read().split()
# Dictionary is generated
	word_counts = dict()
	for word in sentences: 
		if word in word_counts:
# Increments if the word already exists in the dictionary and is repeated  
			word_counts[word] += 1
		else: 
# If the word isnt in the dictionary it will be added
			word_counts[word] = 1
	
	frequency_calculation(word_counts,frequency,sentences)
	print_table(word_counts,frequency)
	file_input.close()


if __name__ == "__main__":
# If and elif statement for error handling 		
	if len(sys.argv) > 2:
		print('Too many arguements, enter only 2')
		exit()
	elif len(sys.argv) < 2:
		print('Too little arguements, enter 2')
		exit()
	else:
		pass


	frequency()