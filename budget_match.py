# budget_match.py
# E-commerce Budget Match Project

def find_two_products(products, budget):
    seen = {}  # price -> product_id
    for pid, price in products.items():
        needed = budget - price
        if needed in seen:
            return seen[needed], pid
        seen[price] = pid
    return None  # no match found


def main():
    print(" Welcome to the E-Commerce Budget Match System \n")

    # Step 1: Define product list
    products = {
        101: 250,
        102: 750,
        103: 500,
        104: 300,
        105: 700,
        106: 450,
        107: 550
    }

    # Step 2: Get user input
    budget = int(input("Enter your budget (₹): "))

    # Step 3: Find best match
    result = find_two_products(products, budget)

    # Step 4: Display result
    if result:
        pid1, pid2 = result
        total = products[pid1] + products[pid2]
        print(f"\n✅ Match Found!")
        print(f"Product {pid1} (₹{products[pid1]}) + Product {pid2} (₹{products[pid2]}) = ₹{total}")
    else:
        print("\n❌ No combination found within budget.")


if __name__ == "__main__":
    main()
