# Unit 1: Domain Entities

## 1. User Entity

The `User` object maintains the simulated PII and Demographics.

### User Attributes

- `user_id` (String/UUID): Primary unique identifier.
- `first_name` (String): Synthetic first name.
- `last_name` (String): Synthetic last name.
- `email` (String): Synthetic email address (target for Column-Level Security).
- `ssn` (String): Social Security Number format (target for Dynamic Data Masking).
- `country` (String): ISO Country Code (target for Row-Level Security).

## 2. Transaction Entity

The `Transaction` object reflects a simulated trading event.

### Transaction Attributes

- `transaction_id` (String/UUID): Primary unique identifier for the trade.
- `user_id` (String/UUID): Foreign key linking to the `User` entity.
- `trade_date` (Date): The date the transaction occurred (derived from AAPL dataset `Date`).
- `trade_type` (String): Synthetic value ("BUY" or "SELL") mocking a user's action on that day.
- `quantity` (Integer): A randomly assigned volume of shares for the user's specific trade.
- `market_open` (Float): AAPL Open price for the day.
- `market_high` (Float): AAPL High price for the day.
- `market_low` (Float): AAPL Low price for the day.
- `market_close` (Float): AAPL Close/Last price for the day.
- `market_volume` (Long): The total number of AAPL shares traded during the trading day.
