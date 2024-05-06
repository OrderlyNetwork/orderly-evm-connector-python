from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class OrderType(AutoName):
    LIMIT = auto()
    MARKET = auto()
    IOC = auto()
    FOK = auto()
    POST_ONLY = auto()
    ASK = auto()
    BID = auto()


class OrderSide(AutoName):
    SELL = auto()
    BUY = auto()


class OrderStatus(AutoName):
    NEW = auto()
    CANCELLED = auto()
    PARTIAL_FILLED = auto()
    FILLED = auto()
    REJECTED = auto()
    INCOMPLETE = auto()
    COMPLETED = auto()


class TimeType(AutoName):
    _5m = auto()
    _15m = auto()
    _30m = auto()
    _1h = auto()
    _4h = auto()
    _12h = auto()
    _1d = auto()
    _1w = auto()
    _1mon = auto()
    _1y = auto()


class WalletSide(AutoName):
    DEPOSIT = auto()
    WITHDRAW = auto()

class AssetStatus(AutoName):
    NEW = auto()
    CONFIRM = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()

class AlgoType(AutoName):
    STOP = auto()
    TAKE_PROFIT = auto()
    STOP_LOSS = auto()
    TP_SL = auto()
    POSITIONAL_TP_SL = auto()
    BRACKET = auto()