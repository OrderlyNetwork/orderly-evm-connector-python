# -*- coding: utf-8 -*-
"""Admin API endpoints - query user data as admin (user_account or user_address)."""

from orderly_evm_connector.lib.utils import check_required_parameters


def get_admin_client_info(self, user_account: str = None, user_address: str = None):
    """[Admin] Get Account Information

    Limit: 10 requests per 60 seconds

    GET /v1/admin/client/info

    Get account information for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    payload = {"user_account": user_account, "user_address": user_address}
    return self._sign_request("GET", "/v1/admin/client/info", payload=payload)


def get_admin_client_holding(
    self,
    user_account: str = None,
    user_address: str = None,
    all: bool = None,
):
    """[Admin] Get Current Holding

    Limit: 10 requests per 1 second

    GET /v1/admin/client/holding

    Get current token holdings for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        all(boolean): If true, return all tokens even if balance is empty.
    """
    payload = {"user_account": user_account, "user_address": user_address, "all": all}
    return self._sign_request("GET", "/v1/admin/client/holding", payload=payload)


def get_admin_internal_transfer_history(
    self,
    side: str,
    user_account: str = None,
    user_address: str = None,
    status: str = None,
    start_t: str = None,
    end_t: str = None,
    page: int = None,
    size: int = None,
    from_account_id: str = None,
    to_account_id: str = None,
    main_sub_only: bool = None,
):
    """[Admin] Get Internal Transfer History

    Limit: 10 requests per 1 second

    GET /v1/admin/internal_transfer_history

    Get internal transfer history for a target user (admin usage).
    Either user_account or user_address is required.

    Args:
        side(string): `IN` or `OUT`.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        status(string): `CREATED`/`PENDING`/`COMPLETED`/`FAILED`.
        start_t(string): Start timestamp.
        end_t(string): End timestamp.
        page(number): Page number (start from 1).
        size(number): Page size.
        from_account_id(string): From account ID.
        to_account_id(string): To account ID.
        main_sub_only(boolean): If True, only main-sub transfers; if False, only main-main; if empty, all.
    """
    check_required_parameters([[side, "side"]])
    payload = {
        "side": side,
        "user_account": user_account,
        "user_address": user_address,
        "status": status,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "from_account_id": from_account_id,
        "to_account_id": to_account_id,
        "main_sub_only": main_sub_only,
    }
    return self._sign_request(
        "GET", "/v1/admin/internal_transfer_history", payload=payload
    )


def get_admin_asset_history(
    self,
    user_account: str = None,
    user_address: str = None,
    token: str = None,
    side: str = None,
    status: str = None,
    start_t: int = None,
    end_t: int = None,
    page: int = None,
    size: int = None,
):
    """[Admin] Get Asset History

    Limit: 10 requests per 60 seconds

    GET /v1/admin/asset/history

    Get asset history (deposits/withdrawals) for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        token(string): Token name to search.
        side(string): `DEPOSIT`/`WITHDRAW`.
        status(string): `NEW`/`CONFIRM`/`PROCESSING`/`COMPLETED`/`FAILED`/`PENDING_REBALANCE`.
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).
        page(number): Page number (start from 1).
        size(number): Page size.
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "token": token,
        "side": side,
        "status": status,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/admin/asset/history", payload=payload)


def get_admin_asset_convert_history(
    self,
    start_t: int,
    end_t: int,
    page: int = None,
    size: int = None,
    cursor: int = None,
    user_account: str = None,
    user_address: str = None,
):
    """[Admin] Get Asset Conversion History

    GET /v1/admin/asset/convert_history

    Get asset conversion history records for builder admin usage.

    Args:
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).

    Optional Args:
        page(number): Page number (start from 1). Ignored when cursor is provided.
        size(number): Page size.
        cursor(number): Keyset cursor from previous response.
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    check_required_parameters([[start_t, "start_t"], [end_t, "end_t"]])
    payload = {
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "cursor": cursor,
        "user_account": user_account,
        "user_address": user_address,
    }
    return self._sign_request(
        "GET", "/v1/admin/asset/convert_history", payload=payload
    )


def get_admin_client_leverage(
    self,
    symbol: str,
    user_account: str = None,
    user_address: str = None,
):
    """[Admin] Get Leverage Setting

    Limit: 1 request per 1 second per IP address

    GET /v1/admin/client/leverage

    Get leverage setting for a symbol for a target user (admin usage).
    Either user_account or user_address is required.

    Args:
        symbol(string): Symbol (e.g. PERP_BTC_USDC).

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {
        "symbol": symbol,
        "user_account": user_account,
        "user_address": user_address,
    }
    return self._sign_request("GET", "/v1/admin/client/leverage", payload=payload)


def get_admin_orders(
    self,
    user_account: str = None,
    user_address: str = None,
    symbol: str = None,
    side: str = None,
    order_type: str = None,
    status: str = None,
    order_tag: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
    sort_by: str = None,
):
    """[Admin] Get Orders

    Limit: 10 requests per 1 second

    GET /v1/admin/orders

    Get orders for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        symbol(string): Symbol filter.
        side(string): `BUY`/`SELL`.
        order_type(string): `LIMIT`/`MARKET`.
        status(string): `NEW`/`CANCELLED`/`PARTIAL_FILLED`/`FILLED`/`REJECTED`/`INCOMPLETE`/`COMPLETED`.
        order_tag(string): Order tag filter.
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).
        page(number): Page number (start from 1).
        size(number): Page size (max: 500).
        sort_by(string): CREATED_TIME_DESC/CREATED_TIME_ASC/UPDATED_TIME_DESC/UPDATED_TIME_ASC.
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "status": status,
        "order_tag": order_tag,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "sort_by": sort_by,
    }
    return self._sign_request("GET", "/v1/admin/orders", payload=payload)


def get_admin_position(
    self,
    symbol: str,
    user_account: str = None,
    user_address: str = None,
):
    """[Admin] Get One Position Info

    Limit: 30 requests per 10 second per user

    GET /v1/admin/position/{symbol}

    Get single position for a target user (admin usage).
    Either user_account or user_address is required.

    Args:
        symbol(string): Symbol (e.g. PERP_BTC_USDC).

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {"user_account": user_account, "user_address": user_address}
    return self._sign_request(
        "GET", f"/v1/admin/position/{symbol}", payload=payload
    )


def get_admin_positions(
    self,
    user_account: str = None,
    user_address: str = None,
):
    """[Admin] Get All Positions Info

    Limit: 30 requests per 10 second per user

    GET /v1/admin/positions

    Get all positions for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    payload = {"user_account": user_account, "user_address": user_address}
    return self._sign_request("GET", "/v1/admin/positions", payload=payload)


def get_admin_funding_fee_history(
    self,
    user_account: str = None,
    user_address: str = None,
    symbol: str = None,
    start_t: str = None,
    end_t: str = None,
    page: str = None,
    size: str = None,
):
    """[Admin] Get Funding Fee History

    Limit: 20 requests per 60 second per user

    GET /v1/admin/funding_fee/history

    Get funding fee history for a target user (admin usage).
    Either user_account or user_address is required. Omit symbol to get all symbols.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        symbol(string): Symbol (e.g. PERP_ETH_USDC); omit for all symbols.
        start_t(string): Start time (13-digit timestamp).
        end_t(string): End time (13-digit timestamp).
        page(string): Page number (start from 1).
        size(string): Page size (default: 60).
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "symbol": symbol,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
    }
    return self._sign_request(
        "GET", "/v1/admin/funding_fee/history", payload=payload
    )


def get_admin_algo_orders(
    self,
    user_account: str = None,
    user_address: str = None,
    symbol: str = None,
    side: str = None,
    order_type: str = None,
    status: str = None,
    order_tag: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
    algo_type: str = None,
    is_triggered: str = None,
):
    """[Admin] Get Algo Orders

    Limit: 5 requests per 1 second

    GET /v1/admin/algo/orders

    Get algo order details by customized filters for admin usage.
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        symbol(string): Symbol filter.
        side(string): BUY/SELL.
        order_type(string): LIMIT/MARKET.
        status(string): NEW/CANCELLED/PARTIAL_FILLED/FILLED/REJECTED/INCOMPLETE/COMPLETED.
        order_tag(string): Order tag filter.
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).
        page(number): Page number (start from 1).
        size(number): Page size (max: 500).
        algo_type(string): STOP/TPSL/positional_TPSL.
        is_triggered(string): Filter by triggered status.
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "status": status,
        "order_tag": order_tag,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "algo_type": algo_type,
        "is_triggered": is_triggered,
    }
    return self._sign_request("GET", "/v1/admin/algo/orders", payload=payload)


def get_admin_trades(
    self,
    user_account: str = None,
    user_address: str = None,
    symbol: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
):
    """[Admin] Get Trades

    Limit: 10 requests per 1 second

    GET /v1/admin/trades

    Return client's trades history within a time range for admin usage.
    Only returns the latest 500 entries.
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        symbol(string): Symbol filter.
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).
        page(number): Page number (start from 1).
        size(number): Page size (max: 500).
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "symbol": symbol,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/admin/trades", payload=payload)


def get_admin_liquidations(
    self,
    user_account: str = None,
    user_address: str = None,
    symbol: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
    sort_by: str = None,
    liquidation_id: int = None,
):
    """[Admin] Get Liquidated Positions

    Limit: 10 requests per 1 second per IP address

    GET /v1/admin/liquidations

    Get liquidated positions for admin usage.
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
        symbol(string): Symbol filter.
        start_t(number): Start time (13-digit timestamp).
        end_t(number): End time (13-digit timestamp).
        page(number): Page number (start from 1).
        size(number): Page size.
        sort_by(string): liquidation_id or time.
        liquidation_id(number): Return the designated liquidation_id only.
    """
    payload = {
        "user_account": user_account,
        "user_address": user_address,
        "symbol": symbol,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "sort_by": sort_by,
        "liquidation_id": liquidation_id,
    }
    return self._sign_request("GET", "/v1/admin/liquidations", payload=payload)


def get_admin_points_stage(self, stage_id: int = None):
    """[Admin] Get stage parameters

    Limit: 10 requests per 1 second per user per IP address

    GET /v1/admin/points/stage

    Get a specific stage (series of epochs). Only callable by Broker Admin.

    Optional Args:
        stage_id(number): Filter by specific Stage. Returns all if omitted.
    """
    payload = {"stage_id": stage_id}
    return self._sign_request("GET", "/v1/admin/points/stage", payload=payload)


def create_admin_points_stage(self, **kwargs):
    """[Admin] Create/update stage parameters

    Limit: 10 requests per 1 second per user per IP address

    POST /v1/admin/points/stage

    Create a new stage (series of epochs). Only callable by Broker Admin.
    Make sure there is only 1 active stage at any time.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/create-stage
    """
    payload = {**kwargs}
    return self._sign_request("POST", "/v1/admin/points/stage", payload=payload)


def delete_admin_points_stage(self, stage_id: int):
    """[Admin] Delete stage

    Limit: 10 requests per 1 second per user per IP address

    DELETE /v1/admin/points/stage

    Delete a specific stage. Only callable by Broker Admin.

    Args:
        stage_id(number): Stage ID to delete.
    """
    check_required_parameters([[stage_id, "stage_id"]])
    payload = {"stage_id": stage_id}
    return self._sign_request("DELETE", "/v1/admin/points/stage", payload=payload)


def get_admin_volume_user_stats(
    self,
    user_account: str = None,
    user_address: str = None,
):
    """[Admin] Get User Volume Statistics

    Limit: 10 requests per 60 seconds

    GET /v1/admin/volume/user/stats

    Get volume statistics for a target user (admin usage).
    Either user_account or user_address is required.

    Optional Args:
        user_account(string): Target user account to query for admin usage.
        user_address(string): Target user address to query for admin usage.
    """
    payload = {"user_account": user_account, "user_address": user_address}
    return self._sign_request(
        "GET", "/v1/admin/volume/user/stats", payload=payload
    )
