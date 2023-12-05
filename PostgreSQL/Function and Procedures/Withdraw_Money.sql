CREATE PROCEDURE sp_withdraw_money(account_id INT, money_amount FLOAT)
LANGUAGE plpgsql
AS
$$
    DECLARE
        account_balance FLOAT;
    BEGIN
        account_balance := (SELECT balance FROM accounts WHERE id = account_id);

        IF account_balance < money_amount THEN
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
            RETURN;
        ELSE
            UPDATE accounts
            SET balance = balance - money_amount
            WHERE id = account_id;

        END IF;
    END;
$$;