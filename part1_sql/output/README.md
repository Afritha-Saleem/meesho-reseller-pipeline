# Part 1 SQL — COUNT(*) vs COUNT(order_id)

For the reseller with no matching orders (RS024), the LEFT JOIN
still produces one row containing NULL values from the orders table.

Therefore:

- COUNT(*) = 1 because COUNT(*) counts the unmatched LEFT JOIN row.
- COUNT(order_id) = 0 because order_id is NULL in that unmatched row,
  and COUNT(column) does not count NULL values.

Therefore COUNT(*) is the wrong way to detect a zero-match LEFT JOIN.
To detect the reseller with no orders, we use:

WHERE o.order_id IS NULL

or COUNT(o.order_id) = 0.
