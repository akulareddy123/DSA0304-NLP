import re
products = [
    "Apple iPhone 15",
    "Samsung Galaxy S24",
    "OnePlus 12",
    "Apple MacBook Air",
    "Dell Inspiron Laptop",
    "HP Pavilion Laptop",
    "Samsung Galaxy Buds",
    "Sony Headphones",
    "Apple iPad",
    "OnePlus Nord"
]
def search_products(keyword, search_type):
    matches = []

    if search_type == "exact":
        pattern = r"^" + re.escape(keyword) + r"$"

    elif search_type == "prefix":
        pattern = r"^" + re.escape(keyword)

    elif search_type == "suffix":
        pattern = re.escape(keyword) + r"$"

    elif search_type == "partial":
        pattern = re.escape(keyword)

    else:
        print("Invalid search type!")
        return []

    for product in products:
        if re.search(pattern, product, re.IGNORECASE):
            matches.append(product)

    return matches
print("Available Products:")
for product in products:
    print("-", product)
keyword = input("\nEnter search keyword: ")
search_type = input(
    "Enter search type (exact/prefix/suffix/partial): "
).lower()
results = search_products(keyword, search_type)
print("\n----- Search Results -----")

if results:
    for product in results:
        print(product)
else:
    print("No matching products found.")

# Report
print("\n----- Search Report -----")
print("Search Keyword :", keyword)
print("Search Type    :", search_type)
print("Total Matches  :", len(results))