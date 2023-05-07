#Automating HTTP response header  creation using puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure => 'present',
  }

file_line { 'add_custom_header':
    path => '/etc/nginx/sites-available/default',
    line => "add_header X-Served-By $hostname;",
    match => 'server_name _;',
  }

exec {'run':
  command => '/usr/sbin/service nginx restart',
}
