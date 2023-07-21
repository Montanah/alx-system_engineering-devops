# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "s/holberton hard .*/holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "s/holberton soft .*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
