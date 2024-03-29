# changes ulimit in nginx config file
exec { 'replaces config file':
  command => 'echo \'ULIMIT="-n 2001"\' | sudo tee /etc/default/nginx > /dev/null ; sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /etc/default/nginx'
}

