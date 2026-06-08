stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGL": 140,
    "AMAZON": 160,
    "MSFT": 330
}

portfolio = {}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER     ")
print("===================================")

print()

print("Available Stocks:")
print("APPLE")
print("TESLA")
print("GOOGL")
print("AMAZON")
print("MSFT")

print()

num_stocks = int(
    input("How many stocks do you want to add? ")
)

print()

for i in range(num_stocks):

    print("Stock Number:", i + 1)

    stock_name = input(
        "Enter Stock Name: "
    ).upper()

    print()

    if stock_name in stock_prices:

        quantity = input(
            "Enter Quantity: "
        )

        print()

        if quantity == "":
            print(
                "Quantity cannot be empty!"
            )

        elif quantity.isdigit():

            quantity = int(quantity)

            portfolio[stock_name] = quantity

            print(
                stock_name,
                "Added Successfully"
            )

        else:

            print(
                "Invalid Quantity! Enter numbers only."
            )

    else:

        print(
            "Stock is not available!"
        )

        print(
            "Available Stocks Are:"
        )

        print(
            "APPLE, TESLA, GOOGL, AMAZON, MSFT"
        )

    print(
        "------------------------"
    )

print()

print(
    "==================================="
)

print(
    "        PORTFOLIO SUMMARY         "
)

print(
    "==================================="
)

print()

for stock in portfolio:

    quantity = portfolio[stock]

    price = stock_prices[stock]

    investment = quantity * price

    total_investment = (
        total_investment
        + investment
    )

    print(
        "Stock Name:",
        stock
    )

    print(
        "Quantity:",
        quantity
    )

    print(
        "Price: $",
        price
    )

    print(
        "Investment: $",
        investment
    )

    print()

with open(
    "portfolio.txt",
    "w"
) as file:

    file.write(
        "STOCK PORTFOLIO TRACKER\n"
    )

    file.write(
        "========================\n\n"
    )

    for stock in portfolio:

        quantity = portfolio[stock]

        price = stock_prices[stock]

        investment = quantity * price

        file.write(
            "Stock Name: "
            + stock
            + "\n"
        )

        file.write(
            "Quantity: "
            + str(quantity)
            + "\n"
        )

        file.write(
            "Price: $"
            + str(price)
            + "\n"
        )

        file.write(
            "Investment: $"
            + str(investment)
            + "\n\n"
        )

    file.write(
        "========================\n"
    )

    file.write(
        "Total Investment: $"
        + str(total_investment)
    )

print(
    "Total Investment Value: $",
    total_investment
)

print()

print(
    "Portfolio Saved Successfully"
)

print(
    "File Name: portfolio.txt"
)

print()

print(
    "Thank You For Using"
)

print(
    "Stock Portfolio Tracker"
)