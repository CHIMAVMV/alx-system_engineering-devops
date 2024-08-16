# Web Stack debugging fix typo in config file
exec { 'fix-wordpress':
  command     => 'sudo sed -i "s/phpp/php/g /var/www/html/wp.settings.php',
  path        => '/usr/bin/:/bin',
}
