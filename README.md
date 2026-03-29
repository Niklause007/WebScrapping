Clinikally Product Scraper
Project Overview

This project is designed to scrape the Clinikally website and collect product-related information from all available product listings.

The main goal of this scraper is to fetch and store important product details such as:

Product Name
MRP (Maximum Retail Price)
Selling Price
SKU
Product Link

This project can be useful for:

E-commerce product analysis
Price monitoring
Competitor research
Inventory and catalog tracking
Data collection for further analysis
Features
Scrapes product data from the Clinikally website
Extracts:
Product MRP
Product Selling Price
Product SKU
Product URL / Link
Can be extended to collect:
Product Name
Brand Name
Category
Discounts
Stock Availability
Data Fields Collected

The scraper collects the following information for each product:

Field	Description
Product Name	Name of the product
MRP	Original listed price
Selling Price	Discounted / current selling price
SKU	Unique stock keeping unit of the product
Product Link	Direct URL to the product page
Project Objective

The purpose of this project is to automate the process of collecting product data from the Clinikally website instead of manually copying information product by product.

This helps save time and enables structured data extraction for analysis or reporting.

Tech Stack

This project can be built using:

Python
Requests
BeautifulSoup
Selenium (if needed for dynamic pages)
Pandas (for storing/exporting data)
Possible Output

The scraped data can be exported into formats such as:

CSV
Excel
JSON

Example output:

Product Name,MRP,Selling Price,SKU,Product Link
Product A,999,799,SKU123,https://www.clinikally.com/product-a
Product B,1299,999,SKU456,https://www.clinikally.com/product-b
Use Cases
Product catalog creation
Price comparison analysis
Discount tracking
Market research
E-commerce analytics
Important Note

This project is created for educational and learning purposes only.

Before scraping any website, always make sure to:

Check the website’s robots.txt
Read the website’s Terms of Service
Respect rate limits and website policies
Future Improvements

Possible enhancements for this project:

Add pagination support
Scrape all product categories
Add retry logic
Save data directly to database
Schedule scraper to run automatically
Add logging and error handling
Author

Abhishek Pratap Singh
