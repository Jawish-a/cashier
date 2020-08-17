def main():
	# write code here
	items = []
	while True:
		item_name = input("Item (enter \"done\" when finished): ")
		if item_name == "done":
			break
		item_price = int(input("Price: "))
		item_qty = int(input("Quantity: "))
		items.append({"name":item_name, "price": item_price, "quantity": item_qty})

	print("-------------------")
	print("receipt")
	print("-------------------")
	total = 0
	for item in items:
		print(str(item["quantity"]) + item["name"] + str(item["price"]*item["quantity"]) + "KD" )
		total += item["price"]*item["quantity"]
	print("-------------------")
	print("Total Price: " + str(total) + "KD")


if __name__ == '__main__':
	main()