CREATE DATABASE gasilin_litres;
USE gasilin_litres;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  login VARCHAR(25) COMMENT 'Логин пользователя',
  pwd CHAR(60) COMMENT 'Хэш пароля', 
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)COMMENT = 'Пользователи';

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
  id SERIAL PRIMARY KEY COMMENT 'Внутренний идентификатор',
  user_id BIGINT UNSIGNED NOT NULL COMMENT 'Связь с таблицей пользователей', 
  name VARCHAR(255) COMMENT 'Имя пользователя',
  birthday DATE COMMENT 'Дата рождения',
  email VARCHAR(150) COMMENT 'e-mail',
  phone VARCHAR(50) COMMENT 'Телефон',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT profiles_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
  KEY name_fk (name),
  KEY email (email),
  KEY phone (phone)  
)COMMENT = 'Профили пользователей. Содержит пользовательские данные, которые заполняются самим пользователем';

DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY COMMENT 'Внутренний идентификатор',
  user_id BIGINT UNSIGNED NOT NULL COMMENT 'Связь с таблицей пользователей', 
  balance NUMERIC(15, 2) COMMENT 'Баланс на счету пользователя',
  ball_balance  NUMERIC(10) COMMENT 'Баланс баллов, программа лояльности',
  CONSTRAINT accounts_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)COMMENT = 'Профили пользователей, в которых находится системная, важная для работы сервиса информация';

DROP TABLE IF EXISTS ganres;
CREATE TABLE ganres (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  level INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Уровень иерархии, нужен для более гибкой иерархии жанров',
  parent INT UNSIGNED DEFAULT 0 COMMENT 'Родительская группа, если текущий уровень больше 0',
  name VARCHAR(255) COMMENT 'Название жанра',
  comment TINYTEXT COMMENT 'Описание жанра',
  KEY name_fk (name),
  KEY parent_fk (parent, level, id)
)COMMENT = 'Таблица жанров книг';

DROP TABLE IF EXISTS authors;
CREATE TABLE authors (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  name VARCHAR(255) COMMENT 'Имя автора',
  comment TEXT COMMENT 'Описание',
  small_photo_filename VARCHAR(255) COMMENT 'Маленькая фоторграфия автора', 
  photo_filename VARCHAR(255) COMMENT 'Большая фоторграфия автора',
  KEY name_fk (name)
)COMMENT = 'Таблица авторов';

DROP TABLE IF EXISTS publishing_house;
DROP TABLE IF EXISTS publishing_houses;
CREATE TABLE publishing_houses (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  name VARCHAR(255) COMMENT 'Название излательства',
  comment TEXT COMMENT 'Описание',
  KEY name_fk (name)
)COMMENT = 'Таблица издательств';

DROP TABLE IF EXISTS books;
CREATE TABLE books (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  name VARCHAR(255) COMMENT 'Название книги',
  comment TEXT COMMENT 'Описание',
  publishing_house_id INT UNSIGNED COMMENT 'Идентификатор издалтельского дома',
  year NUMERIC(4) COMMENT 'Год выпуска',
  ISBN  CHAR(13) COMMENT 'ISBN', 
  small_photo_filename VARCHAR(255) COMMENT 'Маленькая фоторграфия обложки', 
  photo_filename VARCHAR(255) COMMENT 'Большая фоторграфия обложки',
  src_filename VARCHAR(255) COMMENT 'Местоположение файла с исходными данными книги. Текст, иллюстрации, прочие материалы.',
  characteristics TINYTEXT COMMENT 'Физические характеристики книги',
  KEY name_fk (name),
  KEY ISBN_fk (ISBN),
  CONSTRAINT publishing_house_id_fk FOREIGN KEY (publishing_house_id) REFERENCES publishing_houses (id) ON DELETE CASCADE
)COMMENT = 'Таблица книг';

DROP TABLE IF EXISTS authors_of_the_books;
CREATE TABLE authors_of_the_books (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  author_id INT UNSIGNED COMMENT 'Идентификатор автора',
  book_id INT UNSIGNED COMMENT 'Идентификатор книги',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  KEY books_id_fk (book_id),
  KEY authors_id_fk (author_id, book_id),
  CONSTRAINT autors_id_fk FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE,
  CONSTRAINT books_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
)COMMENT = 'Связь авторов и книг';

DROP TABLE IF EXISTS books_series;
CREATE TABLE books_series (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  name VARCHAR(255) COMMENT 'Название серии',
  comment TEXT COMMENT 'Описание',
  KEY name_fk (name)
)COMMENT = 'Таблица книжных серий';

DROP TABLE IF EXISTS books_in_series;
CREATE TABLE books_in_series (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  series_id INT UNSIGNED COMMENT 'Идентификатор серии',
  book_id INT UNSIGNED COMMENT 'Идентификатор книги',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  KEY book_fk (book_id),
  KEY series_fk (series_id, book_id),
  CONSTRAINT series_id_fk FOREIGN KEY (series_id) REFERENCES books_series (id) ON DELETE CASCADE,
  CONSTRAINT books_series_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE  
)COMMENT = 'Набор книг в сериях';

DROP TABLE IF EXISTS ganres_of_the_books;
CREATE TABLE ganres_of_the_books (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  ganre_id INT UNSIGNED COMMENT 'Идентификатор жанра',
  book_id INT UNSIGNED COMMENT 'Идентификатор книги',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  KEY books_id_fk (book_id),
  KEY authors_id_fk (ganre_id, book_id),
  CONSTRAINT ganre_id_fk FOREIGN KEY (ganre_id) REFERENCES ganres (id) ON DELETE CASCADE,
  CONSTRAINT books_ganres_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
)COMMENT = 'Связь жанров и книг';

DROP TABLE IF EXISTS books_on_hands;
CREATE TABLE books_on_hands (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  book_id INT UNSIGNED COMMENT 'Идентификатор книги',
  user_id BIGINT UNSIGNED COMMENT 'Идентификатор пользователя',
  loan_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Дата выдачи книги',
  borrow_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Дата возврата книги. Плановая или фактическая, в зависимости от текущей даты',
  KEY books_id_fk (book_id),
  KEY user_id (user_id, book_id),
  CONSTRAINT books_on_hands_books_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE,
  CONSTRAINT books_on_hands_users_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)COMMENT = 'Таблица выданных книг. Текущих и прошлых';

DROP TABLE IF EXISTS individual_rating;
CREATE TABLE individual_rating (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Внутренний идентификатор',
  book_id INT UNSIGNED COMMENT 'Идентификатор книги',
  user_id BIGINT UNSIGNED COMMENT 'Идентификатор пользователя',
  rating TINYINT UNSIGNED COMMENT 'Оценка книги пользователем',
  feedback TEXT COMMENT 'Отзыв',
  last_changing DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Дата последней корректировки оценки или отзыва',
  KEY books_id_fk (book_id),
  KEY user_id (user_id, book_id),
  CONSTRAINT individual_rating_books_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE,
  CONSTRAINT individual_rating_users_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)COMMENT = 'Таблица в которой хранится индивидуальная оценка и отзыв о каждой книге. Оставленные пользователями';

DROP TABLE IF EXISTS common_books_rating;
CREATE TABLE common_books_rating (
  book_id INT UNSIGNED NOT NULL PRIMARY KEY COMMENT 'Идентификатор книги',
  rating TINYINT UNSIGNED DEFAULT 0 COMMENT 'Средняя оценка книги пользователями',
  count_of_verification INT UNSIGNED DEFAULT 0 COMMENT 'Количество оценвших',
  count_of_reading INT UNSIGNED DEFAULT 0 COMMENT 'Количество прочитавших',
  CONSTRAINT common_books_rating_books_id_fk FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
)COMMENT = 'Таблица в которой хранятся обобщенные оценки книг.';

DROP TABLE IF EXISTS common_users_rating;
CREATE TABLE common_users_rating (
  user_id BIGINT UNSIGNED NOT NULL COMMENT 'Идентификатор книги',
  ganre_id INT UNSIGNED NOT NULL COMMENT 'Идентификатор жанра',
  rating TINYINT UNSIGNED DEFAULT 0 COMMENT 'Средняя оценка книги пользователем',
  count_of_verification INT UNSIGNED DEFAULT 0 COMMENT 'Количество оценок',
  count_of_reading INT UNSIGNED DEFAULT 0 COMMENT 'Количество прочитанных',
  PRIMARY KEY (user_id, ganre_id) COMMENT 'Основной ключ для таблицы',
  CONSTRAINT common_users_rating_ganres_id_fk FOREIGN KEY (ganre_id) REFERENCES ganres (id) ON DELETE CASCADE,
  CONSTRAINT common_users_rating_users_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)COMMENT = 'Таблица в которой хранится статистика по пользователю.';
