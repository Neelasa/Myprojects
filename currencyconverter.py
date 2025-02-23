import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Your API key from Exchange Rates API
API_KEY = 'fca_live_HWwWapw4OJDQC91ITMOTQVyZH5ZKDmNBkIfdGHpd'

# Supported currencies and their full names
currencies = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "INR": "Indian Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SEK": "Swedish Krona",
    "NZD": "New Zealand Dollar",
    "MXN": "Mexican Peso",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "NOK": "Norwegian Krone",
    "KRW": "South Korean Won",
    "TRY": "Turkish Lira",
    "RUB": "Russian Ruble",
    "BRL": "Brazilian Real",
    "ZAR": "South African Rand",
    "JPY": "Japanese Yen"
}

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get().split(" - ")[0]
        to_currency = to_currency_combobox.get().split(" - ")[0]
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        if to_currency in data['rates']:
            converted_amount = amount * data['rates'][to_currency]
            result_label.config(text=f"{amount} {currencies[from_currency]} is equal to {converted_amount:.2f} {currencies[to_currency]}")
        else:
            messagebox.showerror("Error", f"Currency {to_currency} not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Amount entry
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# From currency dropdown
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=[f"{code} - {name}" for code, name in currencies.items()])
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
from_currency_combobox.set("USD - US Dollar")

# To currency dropdown
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=[f"{code} - {name}" for code, name in currencies.items()])
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
to_currency_combobox.set("INR - Indian Rupee")

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
