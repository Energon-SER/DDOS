<?php
/**
 * Основные параметры WordPress.
 *
 * Скрипт для создания wp-config.php использует этот файл в процессе установки.
 * Необязательно использовать веб-интерфейс, можно скопировать файл в "wp-config.php"
 * и заполнить значения вручную.
 *
 * Этот файл содержит следующие параметры:
 *
 * * Настройки базы данных
 * * Секретные ключи
 * * Префикс таблиц базы данных
 * * ABSPATH
 *
 * @link https://ru.wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Параметры базы данных: Эту информацию можно получить у вашего хостинг-провайдера ** //
/** Имя базы данных для WordPress */
define( 'DB_NAME', 'ddos_test' );

/** Имя пользователя базы данных */
define( 'DB_USER', 'admin' );

/** Пароль к базе данных */
define( 'DB_PASSWORD', 'admin' );

/** Имя сервера базы данных */
define( 'DB_HOST', 'localhost' );

/** Кодировка базы данных для создания таблиц. */
define( 'DB_CHARSET', 'utf8mb4' );

/** Схема сопоставления. Не меняйте, если не уверены. */
define( 'DB_COLLATE', '' );

/**#@+
 * Уникальные ключи и соли для аутентификации.
 *
 * Смените значение каждой константы на уникальную фразу. Можно сгенерировать их с помощью
 * {@link https://api.wordpress.org/secret-key/1.1/salt/ сервиса ключей на WordPress.org}.
 *
 * Можно изменить их, чтобы сделать существующие файлы cookies недействительными.
 * Пользователям потребуется авторизоваться снова.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '#$BX(}0N>%{Ml,;l`}$X+:a@Lc<=Twb*}O]tk8YCctco#D]=b0;vKjgr71xmS2aE' );
define( 'SECURE_AUTH_KEY',  'ioC<.9C.lC>3p^]nax[^]UkycrooP-7+H=~|t6Cls.(c!fg-+!0G,|!D_#H2f5mf' );
define( 'LOGGED_IN_KEY',    'GJL)PI@1xRM#F]ZZPw.w?*MOqI|,}g+Q8+INbKmnIwHrv#KDZl.B*[hEL[49DJC~' );
define( 'NONCE_KEY',        'X2pY-4y# V#nIyrxm0bdJ)93IiVLyk>[HZC4UyC2k#ZJiOv6 C_43KcQNZ[]Zr4j' );
define( 'AUTH_SALT',        '}-~4?^##to[>Ir9d,{_^vry|/=:B&r-]HW7p;5/Le@u1Qfqr<=P(jA G=>IFQn}7' );
define( 'SECURE_AUTH_SALT', 'EW[w(JYlc|xJ[oruU2;]<o4lR05m#hZUNudn[0(RC5T+b-1_$vRGtpI(hJFb|EiA' );
define( 'LOGGED_IN_SALT',   'zKo=bvMp7&arN[G}Cp$#{I3SwD9}N<+:nEakmLz[RUmDn|+$>>f3*EK^uw<a=>Yq' );
define( 'NONCE_SALT',       '77VU#R3~&SQ<A)O >sm7Uvv:;j+f2(q$Sz }Q4VN?X)%/3)-Hf67)S0+Lskl_;<]' );

/**#@-*/

/**
 * Префикс таблиц в базе данных WordPress.
 *
 * Можно установить несколько сайтов в одну базу данных, если использовать
 * разные префиксы. Пожалуйста, указывайте только цифры, буквы и знак подчеркивания.
 */
$table_prefix = 'wp_';

/**
 * Для разработчиков: Режим отладки WordPress.
 *
 * Измените это значение на true, чтобы включить отображение уведомлений при разработке.
 * Разработчикам плагинов и тем настоятельно рекомендуется использовать WP_DEBUG
 * в своём рабочем окружении.
 *
 * Информацию о других отладочных константах можно найти в документации.
 *
 * @link https://ru.wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Произвольные значения добавляйте между этой строкой и надписью "дальше не редактируем". */



/* Это всё, дальше не редактируем. Успехов! */

/** Абсолютный путь к директории WordPress. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Инициализирует переменные WordPress и подключает файлы. */
require_once ABSPATH . 'wp-settings.php';
