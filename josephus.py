
class Node:
	def __init__(self, val):
		self.val = val;
		self.nxt = None;

def get_list():
	#total = 40;

	total = int(input("Total number of people: "))
	rg = int(input("Interval of elimination: "))

	head = Node(1);
	temp = head;

	for i in range(total - 1):
		node = Node(i + 1);
		head.nxt = node;
		head = head.nxt;
	
	head.nxt = temp;
	return temp, rg;

def print_list(node):
	temp = node;
	for i in range(40):
		print(temp.val);
		temp = temp.nxt;

def eliminate(node, rng):
	incrementer = 0;	

	while(True):
		if (incrementer + 1 == rng):
			print(node.nxt.val),
			print(" was eliminated.");
			node.nxt = node.nxt.nxt;
			incrementer = 0;
		incrementer += 1;
		if (node.nxt == node):
			print("Survivor is number "),
			print(node.val);
			break;
		node = node.nxt;
			
def does_nothing():
	print("I do nothing");

head_node, rg = get_list();
#print_list(head_node);
eliminate(head_node, rg);
