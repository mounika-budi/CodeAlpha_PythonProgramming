import csv

# Hardcoded stock price dictionary
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.00,
    "MSFT": 410.20,
    "AMZN": 175.80,
    "GOOGL": 140.30
}

def run_portfolio_tracker():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for ticker, price in STOCK_PRICES.items():
        print(f" - {ticker}: ${price:.2f}")
    
    portfolio = []
    total_investment = 0.0

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break
        
        if symbol not in STOCK_PRICES:
            print("Stock symbol not found in predefined list. Please try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol} shares: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid input! Please enter a whole number for quantity.")
            continue

        price = STOCK_PRICES[symbol]
        subtotal = price * quantity
        total_investment += subtotal
        
        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "subtotal": subtotal
        })
        print(f"Added {quantity} shares of {symbol} (${subtotal:.2f})")

    # Display results
    print("\n" + "="*35)
    print("      PORTFOLIO SUMMARY      ")
    print("="*35)
    if not portfolio:
        print("No stocks added to portfolio.")
        return

    for item in portfolio:
        print(f"{item['symbol']}: {item['quantity']} shares @ ${item['price']:.2f} = ${item['subtotal']:.2f}")
    
    print("-" * 35)
    print(f"Total Investment Value: ${total_investment:.2f}")
    print("=" * 35)

    # Save output to CSV file
    filename = "portfolio_summary.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Quantity", "Price per Share ($)", "Subtotal Value ($)"])
        for item in portfolio:
            writer.writerow([item["symbol"], item["quantity"], item["price"], item["subtotal"]])
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"${total_investment:.2f}"])

    print(f"\nPortfolio saved successfully to '{filename}'!")

if __name__ == "__main__":
    run_portfolio_tracker()