FROM php:8.2-apache

# Instalacja podstawowych rozszerzeń bazy do PHP
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Włącz mod_rewrite (do routingu)
RUN a2enmod rewrite

# Przeniesienie całego folderu z gotowymi plikami strony głównej
COPY ./website/ /var/www/html/

# Kopiowanie dawnego API w czystym PHP prosto do /api/ (Aplikacja desktopowa od teraz wejdzie pod /api/)
# (Przeniesiono do folderu website, wiec osobne kopiowanie nie jest juz potrzebne)

# Ustaw uprawnienia by Apache mógł czytać pliki
RUN chown -R www-data:www-data /var/www/html/

EXPOSE 80
