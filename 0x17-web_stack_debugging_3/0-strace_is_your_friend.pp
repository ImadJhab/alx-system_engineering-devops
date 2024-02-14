#apache 505 fix

exec { 'wordpressFix':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin:/usr/bin:/usr/local/bin'
}

