USE gasilin_litres;

DROP TRIGGER IF EXISTS Fill_borrow_date;

delimiter //
CREATE TRIGGER Fill_borrow_date BEFORE INSERT ON books_on_hands
FOR EACH ROW
BEGIN
	SET NEW.borrow_date = NEW.loan_date + INTERVAL 14 DAY;
END //
delimiter ;


DROP PROCEDURE IF EXISTS fill_book_statistic;

delimiter //
CREATE PROCEDURE fill_book_statistic()
BEGIN

	UPDATE common_books_rating LEFT JOIN  
		(SELECT ir.book_id AS book_id_1, COUNT(ir.user_id) AS count_of_verification_1, SUM(ir.rating) / COUNT(ir.user_id) AS rating_1 
		FROM individual_rating AS ir
			JOIN common_books_rating AS cbr
				ON cbr.book_id = ir.book_id
		GROUP BY ir.book_id) AS tt
		ON common_books_rating.book_id = tt.book_id_1
	SET common_books_rating.count_of_verification = tt.count_of_verification_1, common_books_rating.rating = tt.rating_1    
	WHERE tt.book_id_1 IS NOT NULL;

	INSERT INTO common_books_rating (book_id, rating, count_of_verification, count_of_reading)
	SELECT ir.book_id AS book_id, COUNT(ir.user_id) AS count_of_verification, SUM(ir.rating) / COUNT(ir.user_id) AS rating, 0 AS count_of_reading
	FROM individual_rating AS ir
		LEFT JOIN common_books_rating AS cbr
			ON cbr.book_id = ir.book_id
	WHERE cbr.book_id IS NULL        
	GROUP BY ir.book_id;
		
	UPDATE common_books_rating LEFT JOIN  
		(SELECT bh.book_id AS book_id_1, COUNT(bh.user_id) AS count_of_reading_1 
		FROM books_on_hands AS bh
			JOIN common_books_rating AS cbr
				ON cbr.book_id = bh.book_id
		GROUP BY bh.book_id) AS tt
		ON common_books_rating.book_id = tt.book_id_1
	SET common_books_rating.count_of_reading = tt.count_of_reading_1    
	WHERE tt.book_id_1 IS NOT NULL;

	INSERT INTO common_books_rating (book_id, rating, count_of_verification, count_of_reading)
	SELECT bh.book_id AS book_id, 0 AS count_of_verification, 0 AS rating, COUNT(bh.user_id) AS count_of_reading
	FROM books_on_hands AS bh
		LEFT JOIN common_books_rating AS cbr
			ON cbr.book_id = bh.book_id
	WHERE cbr.book_id IS NULL        
	GROUP BY bh.book_id;

END //
delimiter ;

CALL fill_book_statistic();

DROP PROCEDURE IF EXISTS fill_user_statistic;

delimiter //
CREATE PROCEDURE fill_user_statistic()
BEGIN

	UPDATE common_users_rating LEFT JOIN  
			(SELECT ir.user_id AS user_id_1, gb.ganre_id AS ganre_id_1, COUNT(DISTINCT ir.book_id) AS count_of_verification_1, SUM(ir.rating) / COUNT(gb.ganre_id) AS rating_1 
			FROM individual_rating AS ir
				LEFt JOIN ganres_of_the_books AS gb
					ON gb.book_id = ir.book_id
				JOIN common_users_rating AS cur
					ON cur.user_id = ir.user_id
					   AND cur.ganre_id = gb.ganre_id
			GROUP BY ir.user_id,  gb.ganre_id) AS tt
			ON common_users_rating.user_id = tt.user_id_1 AND common_users_rating.ganre_id = tt.ganre_id_1
		SET common_users_rating.count_of_verification = tt.count_of_verification_1, common_users_rating.rating = tt.rating_1    
		WHERE tt.user_id_1 IS NOT NULL AND tt.ganre_id_1 IS NOT NULL;


	INSERT INTO common_users_rating (user_id, ganre_id, rating, count_of_verification, count_of_reading)
	SELECT ir.user_id AS user_id, gb.ganre_id AS ganre_id, COUNT(DISTINCT ir.book_id) AS count_of_verification, SUM(ir.rating) / COUNT(gb.ganre_id) AS rating, 0 AS count_of_reading 
	FROM individual_rating AS ir
		LEFT JOIN ganres_of_the_books AS gb
			ON gb.book_id = ir.book_id
		LEFT JOIN common_users_rating AS cur
			ON cur.user_id = ir.user_id
			   AND cur.ganre_id = gb.ganre_id
	WHERE cur.user_id IS NULL
	GROUP BY ir.user_id,  gb.ganre_id;

	UPDATE common_users_rating LEFT JOIN  
 		(SELECT bh.user_id AS user_id_1,  gb.ganre_id AS ganre_id_1,  COUNT(DISTINCT bh.book_id) AS count_of_reading_1
		FROM books_on_hands AS bh
			LEFT JOIN ganres_of_the_books AS gb
				ON bh.book_id = gb.book_id
			LEFT JOIN common_users_rating AS cur
				ON cur.user_id = bh.user_id AND cur.ganre_id = gb.ganre_id
		GROUP BY bh.user_id,  gb.ganre_id) AS tt
		ON common_users_rating.user_id = tt.user_id_1 AND common_users_rating.ganre_id = tt.ganre_id_1
	SET common_users_rating.count_of_reading = tt.count_of_reading_1    
	WHERE tt.user_id_1 IS NOT NULL AND tt.ganre_id_1 IS NOT NULL;

	INSERT INTO common_users_rating (user_id, ganre_id, rating, count_of_verification, count_of_reading)
	SELECT bh.user_id AS user_id,  gb.ganre_id AS ganre_id, 0 AS count_of_verification, 0 AS rating, COUNT(DISTINCT bh.book_id) AS count_of_reading
	FROM books_on_hands AS bh
		LEFT JOIN ganres_of_the_books AS gb
			ON bh.book_id = gb.book_id
		LEFT JOIN common_users_rating AS cur
			ON cur.user_id = bh.user_id AND cur.ganre_id = gb.ganre_id
	WHERE cur.user_id IS NULL        
	GROUP BY bh.user_id,  gb.ganre_id;
	END //
delimiter ;

CALL fill_user_statistic();

-- Представленияalte
-- 1) При входе пользователя показать ему рекомендуемые книги. Т.е. те, которые он не читал, но жанр этих книг такой-же, как его любыем жанры, а рейтинги высоки.

CREATE OR REPLACE VIEW Recommened_books_for_user AS
SELECT cur.user_id AS user_id, b.name AS book, a.name AS author, cbr.rating AS book_rating
FROM common_users_rating AS cur
	LEFT JOIN ganres_of_the_books AS gb
		ON cur.ganre_id = gb.ganre_id
	LEFT JOIN books_on_hands AS bh
		ON bh.book_id = gb.book_id AND bh.user_id = cur.user_id
	LEFT JOIN common_books_rating AS cbr
		ON cbr.book_id = gb.book_id
	LEFT JOIN books AS b
		ON cbr.book_id = b.id
	LEFT JOIN authors_of_the_books AS ab
		ON cbr.book_id = ab.id
	LEFT JOIN authors AS a
		ON ab.author_id = a.id
WHERE bh.book_id IS NULL
ORDER BY cur.rating DESC, cbr.rating DESC
LIMIT 5;

SELECT * FROM Recommened_books_for_user WHERE user_id = 3;   

-- Список наиболее популярных книг
CREATE OR REPLACE VIEW Most_popular_books_for_user AS
SELECT cbr.book_id AS book_id, b.name AS book, a.name AS author, cbr.rating AS book_rating
FROM common_books_rating AS cbr
	LEFT JOIN books AS b
		ON cbr.book_id = b.id
	LEFT JOIN authors_of_the_books AS ab
		ON cbr.book_id = ab.id
	LEFT JOIN authors AS a
		ON ab.author_id = a.id
ORDER BY cbr.rating DESC
LIMIT 30;

SELECT * FROM Most_popular_books_for_user;

-- Список самых интересных авторов
SELECT a.name AS author, cbr.rating AS book_rating
FROM common_books_rating AS cbr
	LEFT JOIN books AS b
		ON cbr.book_id = b.id
	LEFT JOIN authors_of_the_books AS ab
		ON cbr.book_id = ab.id
	LEFT JOIN authors AS a
		ON ab.author_id = a.id
ORDER BY cbr.rating DESC
LIMIT 5;

-- Список самых читаемых авторов
SELECT a.name AS author, SUM(cbr.count_of_reading) AS count_of_reading
FROM common_books_rating AS cbr
	LEFT JOIN books AS b
		ON cbr.book_id = b.id
	LEFT JOIN authors_of_the_books AS ab
		ON cbr.book_id = ab.id
	LEFT JOIN authors AS a
		ON ab.author_id = a.id
GROUP BY a.name        
ORDER BY count_of_reading DESC
LIMIT 5;

-- Список книг, которые должны быть возвращены в конкретную дату.
SELECT user_id, book_id FROM books_on_hands
WHERE borrow_date = DATE(NOW());

-- Список самых читаемых издательств
SELECT ph.id, COUNT(bh.id) AS quantity
FROM books_on_hands AS bh
	LEFT JOIN books AS b
		ON bh.book_id = b.id
	LEFT JOIN publishing_houses AS ph
		ON b.publishing_house_id = ph.id
GROUP BY ph.id
ORDER BY quantity DESC;