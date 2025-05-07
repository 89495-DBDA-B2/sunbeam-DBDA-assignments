--  1. Write a procedure that computes the perimeter and the area of a
--  rectangle. Define your own values for the length and width. (Assuming
--  that L and W are the length and width of the rectangle, Perimeter =
--  2*(L+W) and Area = L*W.

DROP PROCEDURE IF EXISTS rect;
DELIMITER $$

CREATE PROCEDURE rect()
BEGIN 	
	DECLARE L FLOAT DEFAULT 10;
	DECLARE W FLOAT DEFAULT 5;

	DECLARE area FLOAT;
	DECLARE perimeter FLOAT;

	SET area = L * W;
	SET perimeter = 2 * (L + W);

	SELECT CONCAT('Length = ', L, ' Width = ', W) AS Dimensions;
	SELECT CONCAT('Area = ', area) AS Area;
	SELECT CONCAT('Perimeter = ', perimeter) AS Perimeter;
END $$

DELIMITER ;


