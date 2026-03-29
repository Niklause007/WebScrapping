import requests
import pandas as pd
from tqdm import tqdm

BASE_URL = "https://www.clinikally.com"
API_URL = BASE_URL + "/products.json"

results = []
page = 1
limit = 250   # Shopify max per page

headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:

    url = f"{API_URL}?limit={limit}&page={page}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        break

    data = response.json()

    products = data.get("products", [])

    if len(products) == 0:
        break

    print(f"Processing page {page} | {len(products)} products")

    for product in tqdm(products):

        title = product.get("title")
        handle = product.get("handle")

        product_url = f"{BASE_URL}/products/{handle}"

        for variant in product.get("variants", []):

            size = variant.get("title")
            price = variant.get("price")
            mrp = variant.get("compare_at_price")
            sku = variant.get("sku")

            results.append({
                "Product Name": title,
                "Variant / Size": size,
                "Selling Price": price,
                "MRP": mrp,
                "SKU": sku,
                "Product URL": product_url
            })

    page += 1

# Convert to DataFrame
df = pd.DataFrame(results)

# Save Excel
df.to_excel("clinikally_all_products.xlsx", index=False)

print("Scraping completed!")
print(f"Total variants collected: {len(df)}")