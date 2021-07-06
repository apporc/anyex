from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_assets = publicGetAssets = Entry('assets', 'public', 'GET', {})
    public_get_indices = publicGetIndices = Entry('indices', 'public', 'GET', {})
    public_get_products = publicGetProducts = Entry('products', 'public', 'GET', {})
    public_get_products_symbol = publicGetProductsSymbol = Entry('products/{symbol}', 'public', 'GET', {})
    public_get_tickers = publicGetTickers = Entry('tickers', 'public', 'GET', {})
    public_get_tickers_symbol = publicGetTickersSymbol = Entry('tickers/{symbol}', 'public', 'GET', {})
    public_get_l2orderbook_symbol = publicGetL2orderbookSymbol = Entry('l2orderbook/{symbol}', 'public', 'GET', {})
    public_get_trades_symbol = publicGetTradesSymbol = Entry('trades/{symbol}', 'public', 'GET', {})
    public_get_stats = publicGetStats = Entry('stats', 'public', 'GET', {})
    public_get_history_candles = publicGetHistoryCandles = Entry('history/candles', 'public', 'GET', {})
    public_get_history_sparklines = publicGetHistorySparklines = Entry('history/sparklines', 'public', 'GET', {})
    public_get_settings = publicGetSettings = Entry('settings', 'public', 'GET', {})
    private_get_orders = privateGetOrders = Entry('orders', 'private', 'GET', {})
    private_get_products_product_id_orders_leverage = privateGetProductsProductIdOrdersLeverage = Entry('products/{product_id}/orders/leverage', 'private', 'GET', {})
    private_get_positions_margined = privateGetPositionsMargined = Entry('positions/margined', 'private', 'GET', {})
    private_get_positions = privateGetPositions = Entry('positions', 'private', 'GET', {})
    private_get_orders_history = privateGetOrdersHistory = Entry('orders/history', 'private', 'GET', {})
    private_get_fills = privateGetFills = Entry('fills', 'private', 'GET', {})
    private_get_fills_history_download_csv = privateGetFillsHistoryDownloadCsv = Entry('fills/history/download/csv', 'private', 'GET', {})
    private_get_wallet_balances = privateGetWalletBalances = Entry('wallet/balances', 'private', 'GET', {})
    private_get_wallet_transactions = privateGetWalletTransactions = Entry('wallet/transactions', 'private', 'GET', {})
    private_get_wallet_transactions_download = privateGetWalletTransactionsDownload = Entry('wallet/transactions/download', 'private', 'GET', {})
    private_get_wallets_sub_accounts_transfer_history = privateGetWalletsSubAccountsTransferHistory = Entry('wallets/sub_accounts_transfer_history', 'private', 'GET', {})
    private_get_users_trading_preferences = privateGetUsersTradingPreferences = Entry('users/trading_preferences', 'private', 'GET', {})
    private_get_sub_accounts = privateGetSubAccounts = Entry('sub_accounts', 'private', 'GET', {})
    private_get_profile = privateGetProfile = Entry('profile', 'private', 'GET', {})
    private_get_deposits_address = privateGetDepositsAddress = Entry('deposits/address', 'private', 'GET', {})
    private_get_orders_leverage = privateGetOrdersLeverage = Entry('orders/leverage', 'private', 'GET', {})
    private_post_orders = privatePostOrders = Entry('orders', 'private', 'POST', {})
    private_post_orders_bracket = privatePostOrdersBracket = Entry('orders/bracket', 'private', 'POST', {})
    private_post_orders_batch = privatePostOrdersBatch = Entry('orders/batch', 'private', 'POST', {})
    private_post_products_product_id_orders_leverage = privatePostProductsProductIdOrdersLeverage = Entry('products/{product_id}/orders/leverage', 'private', 'POST', {})
    private_post_positions_change_margin = privatePostPositionsChangeMargin = Entry('positions/change_margin', 'private', 'POST', {})
    private_post_positions_close_all = privatePostPositionsCloseAll = Entry('positions/close_all', 'private', 'POST', {})
    private_post_wallets_sub_account_balance_transfer = privatePostWalletsSubAccountBalanceTransfer = Entry('wallets/sub_account_balance_transfer', 'private', 'POST', {})
    private_post_orders_cancel_after = privatePostOrdersCancelAfter = Entry('orders/cancel_after', 'private', 'POST', {})
    private_post_orders_leverage = privatePostOrdersLeverage = Entry('orders/leverage', 'private', 'POST', {})
    private_put_orders = privatePutOrders = Entry('orders', 'private', 'PUT', {})
    private_put_orders_bracket = privatePutOrdersBracket = Entry('orders/bracket', 'private', 'PUT', {})
    private_put_orders_batch = privatePutOrdersBatch = Entry('orders/batch', 'private', 'PUT', {})
    private_put_positions_auto_topup = privatePutPositionsAutoTopup = Entry('positions/auto_topup', 'private', 'PUT', {})
    private_put_users_update_mmp = privatePutUsersUpdateMmp = Entry('users/update_mmp', 'private', 'PUT', {})
    private_put_users_reset_mmp = privatePutUsersResetMmp = Entry('users/reset_mmp', 'private', 'PUT', {})
    private_delete_orders = privateDeleteOrders = Entry('orders', 'private', 'DELETE', {})
    private_delete_orders_all = privateDeleteOrdersAll = Entry('orders/all', 'private', 'DELETE', {})
    private_delete_orders_batch = privateDeleteOrdersBatch = Entry('orders/batch', 'private', 'DELETE', {})
