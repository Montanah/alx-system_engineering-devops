"Editing the config file"
file { '/var/www/html/wp-settings.php':
  ensure => file,
}

exec { 'replace_line_in_config':
  command     => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path        => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
  require     => File['/var/www/html/wp-settings.php'],
}