-- 4.Create a procedure to Convert a number of inches into yards, feet, and inches. For -- example, 124 inches equals 3 yards, 1 foot, and 4 inches.
-- Ans.


DROP PROCEDURE IF EXISTS convert_inches;
DELIMITER $$

CREATE PROCEDURE convert_inches(IN total_inches INT)
BEGIN
    DECLARE yards INT;
    DECLARE feet INT;
    DECLARE inches INT;

    -- 1 yard = 36 inches
    SET yards = total_inches DIV 36;

    -- remaining inches after yards
    SET feet = (total_inches MOD 36) DIV 12;

    -- remaining inches after feet
    SET inches = (total_inches MOD 36) MOD 12;

    SELECT CONCAT(total_inches, ' inches = ', yards, ' yard(s), ', feet, ' foot/feet, ', inches, ' inch(es)') AS Conversion;
END $$

DELIMITER ;

