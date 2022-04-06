# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import BadRequest
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import InvalidNonce
from ccxt.base.decimal_to_precision import TICK_SIZE
from ccxt.base.precise import Precise


class bitso(Exchange):

    def describe(self):
        return self.deep_extend(super(bitso, self).describe(), {
            'id': 'bitso',
            'name': 'Bitso',
            'countries': ['MX'],  # Mexico
            'rateLimit': 2000,  # 30 requests per minute
            'version': 'v3',
            'has': {
                'CORS': None,
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'addMargin': False,
                'cancelOrder': True,
                'createOrder': True,
                'createReduceOnlyOrder': False,
                'fetchBalance': True,
                'fetchBorrowRate': False,
                'fetchBorrowRateHistories': False,
                'fetchBorrowRateHistory': False,
                'fetchBorrowRates': False,
                'fetchBorrowRatesPerSymbol': False,
                'fetchDepositAddress': True,
                'fetchFundingFee': False,
                'fetchFundingFees': True,
                'fetchFundingHistory': False,
                'fetchFundingRate': False,
                'fetchFundingRateHistory': False,
                'fetchFundingRates': False,
                'fetchIndexOHLCV': False,
                'fetchLeverage': False,
                'fetchMarkets': True,
                'fetchMarkOHLCV': False,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrderTrades': True,
                'fetchPosition': False,
                'fetchPositions': False,
                'fetchPositionsRisk': False,
                'fetchPremiumIndexOHLCV': False,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': True,
                'fetchTransfer': False,
                'fetchTransfers': False,
                'reduceMargin': False,
                'setLeverage': False,
                'setMarginMode': False,
                'setPositionMode': False,
                'transfer': False,
                'withdraw': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87295554-11f98280-c50e-11ea-80d6-15b3bafa8cbf.jpg',
                'api': 'https://api.bitso.com',
                'www': 'https://bitso.com',
                'doc': 'https://bitso.com/api_info',
                'fees': 'https://bitso.com/fees',
                'referral': 'https://bitso.com/?ref=itej',
            },
            'precisionMode': TICK_SIZE,
            'options': {
                'precision': {
                    'XRP': 0.000001,
                    'MXN': 0.01,
                    'TUSD': 0.01,
                },
                'defaultPrecision': 0.00000001,
            },
            'timeframes': {
                '1m': '60',
                '5m': '300',
                '15m': '900',
                '30m': '1800',
                '1h': '3600',
                '4h': '14400',
                '12h': '43200',
                '1d': '86400',
                '1w': '604800',
            },
            'api': {
                'public': {
                    'get': [
                        'available_books',
                        'ticker',
                        'order_book',
                        'trades',
                        'ohlc',
                    ],
                },
                'private': {
                    'get': [
                        'account_status',
                        'balance',
                        'fees',
                        'fundings',
                        'fundings/{fid}',
                        'funding_destination',
                        'kyc_documents',
                        'ledger',
                        'ledger/trades',
                        'ledger/fees',
                        'ledger/fundings',
                        'ledger/withdrawals',
                        'mx_bank_codes',
                        'open_orders',
                        'order_trades/{oid}',
                        'orders/{oid}',
                        'user_trades',
                        'user_trades/{tid}',
                        'withdrawals/',
                        'withdrawals/{wid}',
                    ],
                    'post': [
                        'bitcoin_withdrawal',
                        'debit_card_withdrawal',
                        'ether_withdrawal',
                        'ripple_withdrawal',
                        'bcash_withdrawal',
                        'litecoin_withdrawal',
                        'orders',
                        'phone_number',
                        'phone_verification',
                        'phone_withdrawal',
                        'spei_withdrawal',
                        'ripple_withdrawal',
                        'bcash_withdrawal',
                        'litecoin_withdrawal',
                    ],
                    'delete': [
                        'orders/{oid}',
                        'orders/all',
                    ],
                },
            },
            'exceptions': {
                '0201': AuthenticationError,  # Invalid Nonce or Invalid Credentials
                '104': InvalidNonce,  # Cannot perform request - nonce must be higher than 1520307203724237
                '0304': BadRequest,  # {"success":false,"error":{"code":"0304","message":"The field time_bucket() is either invalid or missing"}}
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetAvailableBooks(params)
        #
        #     {
        #         "success":true,
        #         "payload":[
        #             {
        #                 "book":"btc_mxn",
        #                 "minimum_price":"500",
        #                 "maximum_price":"10000000",
        #                 "minimum_amount":"0.00005",
        #                 "maximum_amount":"500",
        #                 "minimum_value":"5",
        #                 "maximum_value":"10000000",
        #                 "tick_size":"0.01",
        #                 "fees":{
        #                     "flat_rate":{"maker":"0.500","taker":"0.650"},
        #                     "structure":[
        #                         {"volume":"1500000","maker":"0.00500","taker":"0.00650"},
        #                         {"volume":"2000000","maker":"0.00490","taker":"0.00637"},
        #                         {"volume":"5000000","maker":"0.00480","taker":"0.00624"},
        #                         {"volume":"7000000","maker":"0.00440","taker":"0.00572"},
        #                         {"volume":"10000000","maker":"0.00420","taker":"0.00546"},
        #                         {"volume":"15000000","maker":"0.00400","taker":"0.00520"},
        #                         {"volume":"35000000","maker":"0.00370","taker":"0.00481"},
        #                         {"volume":"50000000","maker":"0.00300","taker":"0.00390"},
        #                         {"volume":"150000000","maker":"0.00200","taker":"0.00260"},
        #                         {"volume":"250000000","maker":"0.00100","taker":"0.00130"},
        #                         {"volume":"9999999999","maker":"0.00000","taker":"0.00130"},
        #                     ]
        #                 }
        #             },
        #         ]
        #     }
        markets = self.safe_value(response, 'payload')
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = self.safe_string(market, 'book')
            baseId, quoteId = id.split('_')
            base = baseId.upper()
            quote = quoteId.upper()
            base = self.safe_currency_code(base)
            quote = self.safe_currency_code(quote)
            fees = self.safe_value(market, 'fees', {})
            flatRate = self.safe_value(fees, 'flat_rate', {})
            takerString = self.safe_string(flatRate, 'taker')
            makerString = self.safe_string(flatRate, 'maker')
            taker = self.parse_number(Precise.string_div(takerString, '100'))
            maker = self.parse_number(Precise.string_div(makerString, '100'))
            feeTiers = self.safe_value(fees, 'structure', [])
            fee = {
                'taker': taker,
                'maker': maker,
                'percentage': True,
                'tierBased': True,
            }
            takerFees = []
            makerFees = []
            for j in range(0, len(feeTiers)):
                tier = feeTiers[j]
                volume = self.safe_number(tier, 'volume')
                takerFee = self.safe_number(tier, 'taker')
                makerFee = self.safe_number(tier, 'maker')
                takerFees.append([volume, takerFee])
                makerFees.append([volume, makerFee])
                if j == 0:
                    fee['taker'] = takerFee
                    fee['maker'] = makerFee
            tiers = {
                'taker': takerFees,
                'maker': makerFees,
            }
            fee['tiers'] = tiers
            defaultPricePrecision = self.safe_number(self.options['precision'], quote, self.options['defaultPrecision'])
            result.append(self.extend({
                'id': id,
                'symbol': base + '/' + quote,
                'base': base,
                'quote': quote,
                'settle': None,
                'baseId': baseId,
                'quoteId': quoteId,
                'settleId': None,
                'type': 'spot',
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'active': None,
                'contract': False,
                'linear': None,
                'inverse': None,
                'taker': taker,
                'maker': maker,
                'contractSize': None,
                'expiry': None,
                'expiryDatetime': None,
                'strike': None,
                'optionType': None,
                'precision': {
                    'amount': self.safe_number(self.options['precision'], base, self.options['defaultPrecision']),
                    'price': self.safe_number(market, 'tick_size', defaultPricePrecision),
                },
                'limits': {
                    'leverage': {
                        'min': None,
                        'max': None,
                    },
                    'amount': {
                        'min': self.safe_number(market, 'minimum_amount'),
                        'max': self.safe_number(market, 'maximum_amount'),
                    },
                    'price': {
                        'min': self.safe_number(market, 'minimum_price'),
                        'max': self.safe_number(market, 'maximum_price'),
                    },
                    'cost': {
                        'min': self.safe_number(market, 'minimum_value'),
                        'max': self.safe_number(market, 'maximum_value'),
                    },
                },
                'info': market,
            }, fee))
        return result

    def parse_balance(self, response):
        payload = self.safe_value(response, 'payload', {})
        balances = self.safe_value(payload, 'balances')
        result = {
            'info': response,
            'timestamp': None,
            'datetime': None,
        }
        for i in range(0, len(balances)):
            balance = balances[i]
            currencyId = self.safe_string(balance, 'currency')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_string(balance, 'available')
            account['used'] = self.safe_string(balance, 'locked')
            account['total'] = self.safe_string(balance, 'total')
            result[code] = account
        return self.safe_balance(result)

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetBalance(params)
        #
        #     {
        #       "success": True,
        #       "payload": {
        #         "balances": [
        #           {
        #             "currency": "bat",
        #             "available": "0.00000000",
        #             "locked": "0.00000000",
        #             "total": "0.00000000",
        #             "pending_deposit": "0.00000000",
        #             "pending_withdrawal": "0.00000000"
        #           },
        #           {
        #             "currency": "bch",
        #             "available": "0.00000000",
        #             "locked": "0.00000000",
        #             "total": "0.00000000",
        #             "pending_deposit": "0.00000000",
        #             "pending_withdrawal": "0.00000000"
        #           },
        #         ],
        #       },
        #     }
        #
        return self.parse_balance(response)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'book': self.market_id(symbol),
        }
        response = self.publicGetOrderBook(self.extend(request, params))
        orderbook = self.safe_value(response, 'payload')
        timestamp = self.parse8601(self.safe_string(orderbook, 'updated_at'))
        return self.parse_order_book(orderbook, symbol, timestamp, 'bids', 'asks', 'price', 'amount')

    def parse_ticker(self, ticker, market=None):
        #
        #     {
        #         "high":"37446.85",
        #         "last":"36599.54",
        #         "created_at":"2022-01-28T12:06:11+00:00",
        #         "book":"btc_usdt",
        #         "volume":"7.29075419",
        #         "vwap":"36579.1564400307",
        #         "low":"35578.52",
        #         "ask":"36574.76",
        #         "bid":"36538.22",
        #         "change_24":"-105.64"
        #     }
        #
        symbol = self.safe_symbol(None, market)
        timestamp = self.parse8601(self.safe_string(ticker, 'created_at'))
        vwap = self.safe_string(ticker, 'vwap')
        baseVolume = self.safe_string(ticker, 'volume')
        quoteVolume = Precise.string_mul(baseVolume, vwap)
        last = self.safe_string(ticker, 'last')
        return self.safe_ticker({
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_string(ticker, 'high'),
            'low': self.safe_string(ticker, 'low'),
            'bid': self.safe_string(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_string(ticker, 'ask'),
            'askVolume': None,
            'vwap': vwap,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }, market, False)

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'book': market['id'],
        }
        response = self.publicGetTicker(self.extend(request, params))
        ticker = self.safe_value(response, 'payload')
        #
        #     {
        #         "success":true,
        #         "payload":{
        #             "high":"37446.85",
        #             "last":"37051.96",
        #             "created_at":"2022-01-28T17:03:29+00:00",
        #             "book":"btc_usdt",
        #             "volume":"6.16176186",
        #             "vwap":"36582.6293169472",
        #             "low":"35578.52",
        #             "ask":"37083.62",
        #             "bid":"37039.66",
        #             "change_24":"478.45"
        #         }
        #     }
        #
        return self.parse_ticker(ticker, market)

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'book': market['id'],
            'time_bucket': self.timeframes[timeframe],
        }
        if since is not None:
            request['start'] = since
            if limit is not None:
                duration = self.parse_timeframe(timeframe)
                request['end'] = self.sum(since, duration * limit * 1000)
        elif limit is not None:
            now = self.milliseconds()
            request['end'] = now
            request['start'] = now - self.parse_timeframe(timeframe) * 1000 * limit
        response = self.publicGetOhlc(self.extend(request, params))
        #
        #     {
        #         "success":true,
        #         "payload": [
        #             {
        #                 "bucket_start_time":1648219140000,
        #                 "first_trade_time":1648219154990,
        #                 "last_trade_time":1648219189441,
        #                 "first_rate":"44958.60",
        #                 "last_rate":"44979.88",
        #                 "min_rate":"44957.33",
        #                 "max_rate":"44979.88",
        #                 "trade_count":8,
        #                 "volume":"0.00082814",
        #                 "vwap":"44965.02"
        #             },
        #         ]
        #     }
        #
        payload = self.safe_value(response, 'payload', [])
        return self.parse_ohlcvs(payload, market, timeframe, since, limit)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m'):
        #
        #     {
        #         "bucket_start_time":1648219140000,
        #         "first_trade_time":1648219154990,
        #         "last_trade_time":1648219189441,
        #         "first_rate":"44958.60",
        #         "last_rate":"44979.88",
        #         "min_rate":"44957.33",
        #         "max_rate":"44979.88",
        #         "trade_count":8,
        #         "volume":"0.00082814",
        #         "vwap":"44965.02"
        #     },
        #
        return [
            self.safe_integer(ohlcv, 'bucket_start_time'),
            self.safe_number(ohlcv, 'first_rate'),
            self.safe_number(ohlcv, 'max_rate'),
            self.safe_number(ohlcv, 'min_rate'),
            self.safe_number(ohlcv, 'last_rate'),
            self.safe_number(ohlcv, 'volume'),
        ]

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #
        #      {
        #          "book": "btc_usdt",
        #          "created_at": "2021-11-24T12:14:53+0000",
        #          "amount": "0.00026562",
        #          "maker_side": "sell",
        #          "price": "56471.55",
        #          "tid": "52557338"
        #      }
        #
        # fetchMyTrades(private)
        #
        #      {
        #          "book": "btc_usdt",
        #          "created_at": "2021-11-24T12:31:03+0000",
        #          "minor": "11.30356000",
        #          "major": "-0.00020000",
        #          "fees_amount": "0.01119052",
        #          "fees_currency": "usdt",
        #          "minor_currency": "usdt",
        #          "major_currency": "btc",
        #          "oid": "djTzMIWx2Vi3iMjl",
        #          "tid": "52559051",
        #          "price": "56517.80",
        #          "side": "sell",
        #          "maker_side": "buy"
        #      }
        #
        # fetchOrderTrades(private)
        #
        #      {
        #          "book": "btc_usdt",
        #          "created_at": "2021-11-24T12:30:52+0000",
        #          "minor": "-11.33047916",
        #          "major": "0.00020020",
        #          "fees_amount": "0.00000020",
        #          "fees_currency": "btc",
        #          "minor_currency": "usdt",
        #          "major_currency": "btc",
        #          "oid": "O0D2zcljjjQF5xlG",
        #          "tid": "52559030",
        #          "price": "56595.80",
        #          "side": "buy",
        #          "maker_side": "sell"
        #      }
        #
        timestamp = self.parse8601(self.safe_string(trade, 'created_at'))
        marketId = self.safe_string(trade, 'book')
        symbol = self.safe_symbol(marketId, market, '_')
        side = self.safe_string_2(trade, 'side', 'maker_side')
        makerSide = self.safe_string(trade, 'maker_side')
        takerOrMaker = None
        if side == makerSide:
            takerOrMaker = 'maker'
        else:
            takerOrMaker = 'taker'
        amount = self.safe_string_2(trade, 'amount', 'major')
        if amount is not None:
            amount = Precise.string_abs(amount)
        fee = None
        feeCost = self.safe_string(trade, 'fees_amount')
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'fees_currency')
            feeCurrency = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrency,
            }
        cost = self.safe_string(trade, 'minor')
        if cost is not None:
            cost = Precise.string_abs(cost)
        price = self.safe_string(trade, 'price')
        orderId = self.safe_string(trade, 'oid')
        id = self.safe_string(trade, 'tid')
        return self.safe_trade({
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': orderId,
            'type': None,
            'side': side,
            'takerOrMaker': takerOrMaker,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }, market)

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'book': market['id'],
        }
        response = self.publicGetTrades(self.extend(request, params))
        return self.parse_trades(response['payload'], market, since, limit)

    def fetch_trading_fees(self, params={}):
        self.load_markets()
        response = self.privateGetFees(params)
        #
        #    {
        #        success: True,
        #        payload: {
        #            fees: [
        #                {
        #                    book: 'btc_mxn',
        #                    fee_percent: '0.6500',
        #                    fee_decimal: '0.00650000',
        #                    taker_fee_percent: '0.6500',
        #                    taker_fee_decimal: '0.00650000',
        #                    maker_fee_percent: '0.5000',
        #                    maker_fee_decimal: '0.00500000',
        #                    volume_currency: 'mxn',
        #                    current_volume: '0.00',
        #                    next_volume: '1500000.00',
        #                    next_maker_fee_percent: '0.490',
        #                    next_taker_fee_percent: '0.637',
        #                    nextVolume: '1500000.00',
        #                    nextFee: '0.490',
        #                    nextTakerFee: '0.637'
        #                },
        #                ...
        #            ],
        #            deposit_fees: [
        #                {
        #                    currency: 'btc',
        #                    method: 'rewards',
        #                    fee: '0.00',
        #                    is_fixed: False
        #                },
        #                ...
        #            ],
        #            withdrawal_fees: {
        #                ada: '0.20958100',
        #                bch: '0.00009437',
        #                ars: '0',
        #                btc: '0.00001209',
        #                ...
        #            }
        #        }
        #    }
        #
        payload = self.safe_value(response, 'payload', {})
        fees = self.safe_value(payload, 'fees', [])
        result = {}
        for i in range(0, len(fees)):
            fee = fees[i]
            marketId = self.safe_string(fee, 'book')
            symbol = self.safe_symbol(marketId, None, '_')
            result[symbol] = {
                'info': fee,
                'symbol': symbol,
                'maker': self.safe_number(fee, 'maker_fee_decimal'),
                'taker': self.safe_number(fee, 'taker_fee_decimal'),
                'percentage': True,
                'tierBased': True,
            }
        return result

    def fetch_my_trades(self, symbol=None, since=None, limit=25, params={}):
        self.load_markets()
        market = self.market(symbol)
        # the don't support fetching trades starting from a date yet
        # use the `marker` extra param for that
        # self is not a typo, the variable name is 'marker'(don't confuse with 'market')
        markerInParams = ('marker' in params)
        # warn the user with an exception if the user wants to filter
        # starting from since timestamp, but does not set the trade id with an extra 'marker' param
        if (since is not None) and not markerInParams:
            raise ExchangeError(self.id + ' fetchMyTrades does not support fetching trades starting from a timestamp with the `since` argument, use the `marker` extra param to filter starting from an integer trade id')
        # convert it to an integer unconditionally
        if markerInParams:
            params = self.extend(params, {
                'marker': int(params['marker']),
            })
        request = {
            'book': market['id'],
            'limit': limit,  # default = 25, max = 100
            # 'sort': 'desc',  # default = desc
            # 'marker': id,  # integer id to start from
        }
        response = self.privateGetUserTrades(self.extend(request, params))
        return self.parse_trades(response['payload'], market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'book': self.market_id(symbol),
            'side': side,
            'type': type,
            'major': self.amount_to_precision(symbol, amount),
        }
        if type == 'limit':
            request['price'] = self.price_to_precision(symbol, price)
        response = self.privatePostOrders(self.extend(request, params))
        id = self.safe_string(response['payload'], 'oid')
        return {
            'info': response,
            'id': id,
        }

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'oid': id,
        }
        return self.privateDeleteOrdersOid(self.extend(request, params))

    def parse_order_status(self, status):
        statuses = {
            'partial-fill': 'open',  # self is a common substitution in ccxt
            'completed': 'closed',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'oid')
        side = self.safe_string(order, 'side')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        marketId = self.safe_string(order, 'book')
        symbol = self.safe_symbol(marketId, market, '_')
        orderType = self.safe_string(order, 'type')
        timestamp = self.parse8601(self.safe_string(order, 'created_at'))
        price = self.safe_string(order, 'price')
        amount = self.safe_string(order, 'original_amount')
        remaining = self.safe_string(order, 'unfilled_amount')
        clientOrderId = self.safe_string(order, 'client_id')
        return self.safe_order({
            'info': order,
            'id': id,
            'clientOrderId': clientOrderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': orderType,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'amount': amount,
            'cost': None,
            'remaining': remaining,
            'filled': None,
            'status': status,
            'fee': None,
            'average': None,
            'trades': None,
        }, market)

    def fetch_open_orders(self, symbol=None, since=None, limit=25, params={}):
        self.load_markets()
        market = self.market(symbol)
        # the don't support fetching trades starting from a date yet
        # use the `marker` extra param for that
        # self is not a typo, the variable name is 'marker'(don't confuse with 'market')
        markerInParams = ('marker' in params)
        # warn the user with an exception if the user wants to filter
        # starting from since timestamp, but does not set the trade id with an extra 'marker' param
        if (since is not None) and not markerInParams:
            raise ExchangeError(self.id + ' fetchOpenOrders does not support fetching orders starting from a timestamp with the `since` argument, use the `marker` extra param to filter starting from an integer trade id')
        # convert it to an integer unconditionally
        if markerInParams:
            params = self.extend(params, {
                'marker': int(params['marker']),
            })
        request = {
            'book': market['id'],
            'limit': limit,  # default = 25, max = 100
            # 'sort': 'desc',  # default = desc
            # 'marker': id,  # integer id to start from
        }
        response = self.privateGetOpenOrders(self.extend(request, params))
        orders = self.parse_orders(response['payload'], market, since, limit)
        return orders

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        response = self.privateGetOrdersOid({
            'oid': id,
        })
        payload = self.safe_value(response, 'payload')
        if isinstance(payload, list):
            numOrders = len(response['payload'])
            if numOrders == 1:
                return self.parse_order(payload[0])
        raise OrderNotFound(self.id + ': The order ' + id + ' not found.')

    def fetch_order_trades(self, id, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'oid': id,
        }
        response = self.privateGetOrderTradesOid(self.extend(request, params))
        return self.parse_trades(response['payload'], market)

    def fetch_deposit_address(self, code, params={}):
        self.load_markets()
        currency = self.currency(code)
        request = {
            'fund_currency': currency['id'],
        }
        response = self.privateGetFundingDestination(self.extend(request, params))
        address = self.safe_string(response['payload'], 'account_identifier')
        tag = None
        if address.find('?dt=') >= 0:
            parts = address.split('?dt=')
            address = self.safe_string(parts, 0)
            tag = self.safe_string(parts, 1)
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': tag,
            'network': None,
            'info': response,
        }

    def fetch_funding_fees(self, params={}):
        self.load_markets()
        response = self.privateGetFees(params)
        #
        #    {
        #        success: True,
        #        payload: {
        #            fees: [
        #                {
        #                    book: 'btc_mxn',
        #                    fee_percent: '0.6500',
        #                    fee_decimal: '0.00650000',
        #                    taker_fee_percent: '0.6500',
        #                    taker_fee_decimal: '0.00650000',
        #                    maker_fee_percent: '0.5000',
        #                    maker_fee_decimal: '0.00500000',
        #                    volume_currency: 'mxn',
        #                    current_volume: '0.00',
        #                    next_volume: '1500000.00',
        #                    next_maker_fee_percent: '0.490',
        #                    next_taker_fee_percent: '0.637',
        #                    nextVolume: '1500000.00',
        #                    nextFee: '0.490',
        #                    nextTakerFee: '0.637'
        #                },
        #                ...
        #            ],
        #            deposit_fees: [
        #                {
        #                    currency: 'btc',
        #                    method: 'rewards',
        #                    fee: '0.00',
        #                    is_fixed: False
        #                },
        #                ...
        #            ],
        #            withdrawal_fees: {
        #                ada: '0.20958100',
        #                bch: '0.00009437',
        #                ars: '0',
        #                btc: '0.00001209',
        #                ...
        #            }
        #        }
        #    }
        #
        payload = self.safe_value(response, 'payload', {})
        depositFees = self.safe_value(payload, 'deposit_fees', [])
        deposit = {}
        for i in range(0, len(depositFees)):
            depositFee = depositFees[i]
            currencyId = self.safe_string(depositFee, 'currency')
            code = self.safe_currency_code(currencyId)
            deposit[code] = self.safe_number(depositFee, 'fee')
        withdraw = {}
        withdrawalFees = self.safe_value(payload, 'withdrawal_fees', [])
        currencyIds = list(withdrawalFees.keys())
        for i in range(0, len(currencyIds)):
            currencyId = currencyIds[i]
            code = self.safe_currency_code(currencyId)
            withdraw[code] = self.safe_number(withdrawalFees, currencyId)
        return {
            'info': response,
            'deposit': deposit,
            'withdraw': withdraw,
        }

    def withdraw(self, code, amount, address, tag=None, params={}):
        tag, params = self.handle_withdraw_tag_and_params(tag, params)
        self.check_address(address)
        self.load_markets()
        methods = {
            'BTC': 'Bitcoin',
            'ETH': 'Ether',
            'XRP': 'Ripple',
            'BCH': 'Bcash',
            'LTC': 'Litecoin',
        }
        method = methods[code] if (code in methods) else None
        if method is None:
            raise ExchangeError(self.id + ' not valid withdraw coin: ' + code)
        request = {
            'amount': amount,
            'address': address,
            'destination_tag': tag,
        }
        classMethod = 'privatePost' + method + 'Withdrawal'
        response = getattr(self, classMethod)(self.extend(request, params))
        return {
            'info': response,
            'id': self.safe_string(response['payload'], 'wid'),
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        endpoint = '/' + self.version + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if method == 'GET':
            if query:
                endpoint += '?' + self.urlencode(query)
        url = self.urls['api'] + endpoint
        if api == 'private':
            self.check_required_credentials()
            nonce = str(self.nonce())
            request = ''.join([nonce, method, endpoint])
            if method != 'GET':
                if query:
                    body = self.json(query)
                    request += body
            signature = self.hmac(self.encode(request), self.encode(self.secret))
            auth = self.apiKey + ':' + nonce + ':' + signature
            headers = {
                'Authorization': 'Bitso ' + auth,
                'Content-Type': 'application/json',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        if 'success' in response:
            #
            #     {"success":false,"error":{"code":104,"message":"Cannot perform request - nonce must be higher than 1520307203724237"}}
            #
            success = self.safe_value(response, 'success', False)
            if isinstance(success, str):
                if (success == 'true') or (success == '1'):
                    success = True
                else:
                    success = False
            if not success:
                feedback = self.id + ' ' + self.json(response)
                error = self.safe_value(response, 'error')
                if error is None:
                    raise ExchangeError(feedback)
                code = self.safe_string(error, 'code')
                self.throw_exactly_matched_exception(self.exceptions, code, feedback)
                raise ExchangeError(feedback)
