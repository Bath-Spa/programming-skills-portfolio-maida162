class VendingMachine:
    # ... (rest of the class remains the same)

    def vend_item(self, item, payment_method):
        selected_item_price = self.select_item(item)

        if selected_item_price is not None:
            print(f"Selected item: {item}")
            print(f"Item price: ${selected_item_price:.2f}")

            while True:
                if payment_method == 'cash':
                    cash_amount = float(input("Insert cash amount: $"))
                    self.process_cash_payment(cash_amount)
                elif payment_method == 'card':
                    card_amount = float(input("Enter card amount: $"))
                    self.process_card_payment(card_amount)
                else:
                    print("Invalid payment method.")
                    return

                if self.balance >= selected_item_price:
                    change = self.balance - selected_item_price
                    print(f"Thank you for your purchase! Enjoy your {item}.")
                    if change > 0:
                        print(f"Change: ${change:.2f}")
                    return  # Return to the main loop after a successful purchase
                else:
                    print("Insufficient funds. Please insert more money.")

# Example usage
vending_machine = VendingMachine()

while True:
    vending_machine.display_items()
    selected_item = input("Enter the item you want to purchase (or 'exit' to quit): ")

    if selected_item.lower() == 'exit':
        break

    payment_method = input("Select payment method ('cash' or 'card'): ")

    vending_machine.vend_item(selected_item, payment_method)

    # Add a line to reset the balance after each purchase
    vending_machine.balance = 0.0

print("Exiting the vending machine program.")
