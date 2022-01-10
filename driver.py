# This entrypoint file to be used in development. Start by reading README.md

from unittest import main
from wallet import *


wallet = Wallet('Sample')
wallet.read_from_excel('myWallet.csv')

wallet.print_ledger()
wallet.plot_categories()

