def read_file_flags():
	file_flag = open('bandeiras.txt', 'r')
	return file_flag


def get_propertie_flag(name):
	
	file_flag = read_file_flags()
	for line in file_flag:
		line = line.split(",")
		if line[0].startswith(name):
			line[1] = format_value(line[1])
			line[2] = format_value(line[2])
			return line[1],line[2]
	return 0

def list_flags():
	flags = []
	file_flag = read_file_flags()
	for line in file_flag:
		line = line.split(",")
		flags.append(line[0])
	return flags[1:]


def format_value(value):
	if value.find("ou") != -1:
		value = value.replace("ou"," ").strip().split(" ")
	elif value.find("-") != -1:
		value = value.replace("-"," ").strip().split(" ")
		value = [ int(n) for n in xrange(int(value[1][0]),int(value[1][-1])+1)]
	else:
		value = [int(value)]
	return value