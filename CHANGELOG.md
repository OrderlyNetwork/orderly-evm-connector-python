### 2024-03-18 S23
#### Added
Given Orderly’s growth of supported chains, we understand some projects choose to only focus on certain chains, thus brokers can now choose which chain they want to operate on.

Supported brokers for each chain can be retrieved through GET /v1/public/chain_info

We are excited to announce a new feature to our trading platform: the Max Slippage Setting for Market Orders. This functionality allows traders to set a maximum slippage for their market orders, giving unprecedented control over order execution relative to the market’s mid-price.

For buy market orders, this means your order will be fully or partially filled at price levels greater than the order book’s mid-price adjusted by your specified slippage. Conversely, sell market orders will be executed at price levels less than the mid-price, also adjusted by your chosen slippage. This ensures that your orders are executed within your comfort zone of market price movement, enhancing predictability and control over your trading outcomes.

For example, if the mid-price for MATIC is $1 and you place a buy market order with a 0.02% slippage, only portions of the order that meet the slippage criteria will be executed, with any remaining quantity being canceled. This precision ensures that you achieve the best possible price, according to your specified tolerance for slippage.

#### Updated

Orders with an order_tag can now be retrieved qvia GET /v1/orders & GET /v1/algo/orders APIs with the new order_tag parameter.

Enhancements to GET /v1/referral/info API, adding the following data in response:

- For referrers:

    - 1d_referrer_rebate
    - 7d_referrer_rebate
    - 30d_referrer_rebate
    - total_referrer_rebate

- For referees:

    - 1d_referee_rebate
    - 7d_referee_rebate
    - 30d_referee_rebate
    - total_referee_rebate

Adding volume and fees of all referrees for the refferal code in response for GET ```/v1/referral/rebate_summary```

Adding maker and taker volume breakdown in GET /v1/volume/broker/daily API

Brokers can now retrieve total fees collected under the criteria (given broker_id, aggregate logic, order_tag filter, and etc.) + broker rebate viaGET ```/v1/volume/broker/daily``` API

New query parameters in GET /v1/referral/admin_info API:

- New query parameter user_address, to filter all codes of the matching user_address only (should only match 1 account since the broker_id has to match the broker admin one)

- New query parameter account_id, to filter all codes of the matching account_id only

- NOTE: Only user_address or account_id can be provided

Ability to change the referral code’s rebate split via POST /v1/referral/edit_split

Additional response fields in GET /v1/referral/admin_info API:

- total_referrer_rebate = Lifetime total referrer rebate on this code

- total_referee_rebate = Lifetime total referee rebate on this code

Additional responses in `GET /v1/public/campaign/ranking` and `GET /v1/public/campaign/user` APIs:

- total_deposit_amount

- total_withdrawal_amount

- start_account_value

- end_account_value (which is current_account_value)

Increased update frequency of `GET /v1/volume/broker/daily` API to hourly from daily

Added address in the response for `GET /v1/volume/broker/daily`

---
