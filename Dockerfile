FROM php:8.2-apache

# Instalacja podstawowych rozszerzeń bazy do PHP
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Włącz mod_rewrite (do routingu)
RUN a2enmod rewrite

# Przeniesienie całego folderu z gotowymi plikami strony głównej
COPY ./website/ /var/www/html/

# Instalacja git i unzip 
RUN apt-get update && apt-get install -y git unzip && rm -rf /var/lib/apt/lists/*

# Instalacja Composera z oficjalnego obrazu
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Uruchomienie composer install by wygenerować pakiet /vendor
RUN cd /var/www/html && composer install --no-dev --optimize-autoloader

# Ustaw uprawnienia by Apache mógł czytać pliki
RUN chown -R www-data:www-data /var/www/html/

# Ustaw port nasłuchu na zmienną PORT (Render tego wymaga, inaczej daje 502 Bad Gateway)
ENV PORT=80

# Modyfikacja plików konfiguracyjnych Apache przy starcie kontenera
CMD sed -i "s/80/$PORT/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf && docker-php-entrypoint apache2-foreground
