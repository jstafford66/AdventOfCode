
ex = False

if ex:
	lines = open('Day8ex.txt').read()
else:
	lines = open('Day8in.txt').read()

data = lines.split(' ')

#2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2

def buildNode(data):
	
	node = {'child_count':0, 'children':[], 'metadata_count':0, 'metadata':[], 'value':0, 'meta_sum':0}
	
	node['child_count'] = int(data.pop(0))
	node['metadata_count'] = int(data.pop(0))
	
	sum = 0
	
	if node['child_count'] > 0:
		for n in range(0, node['child_count']):
			child, child_sum = buildNode(data)
			node['children'].append(child)
			sum = sum + child_sum
	
	if node['metadata_count'] > 0:
		for m in range(0, node['metadata_count']):
			meta = int(data.pop(0))
			node['metadata'].append(meta)
			node['meta_sum'] = node['meta_sum'] + meta
			sum = sum + meta
	
	return node, sum

def calcNodeValue(node):
	value = 0
	print(node)
	if node['child_count'] == 0:
		print("Summing Meta Data")
		value = node['meta_sum']
	else:
		print("Summing children:", node['metadata'])
		for m in node['metadata']:
			index = m-1
			print("\tchild:", index)
			print("________________")
			if index < node['child_count']:
				sum_child = node['children'][index]
				child, child_value = calcNodeValue(sum_child)
				value = value + child_value

	node['value'] = value
	return node, value

tree, sum = buildNode(data)


print(tree)
print("---------------")
print(sum)
print("!!!!!!!!!!!!!!!!")
tree, value = calcNodeValue(tree)
print("******************")
print(value)