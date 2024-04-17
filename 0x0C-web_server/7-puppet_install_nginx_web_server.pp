exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
  before  => Exec['ufw'],
}

exec { 'ufw':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
}

exec { 'echo files':
  command => '/usr/bin/echo "Hello World!" > /var/www/html/index.html',
}

exec { 'echo files2':
  command => '/usr/bin/echo "Ceci n\'est pas une page" > /usr/share/nginx/html/404.html',
}

exec { 'sed1':
  command => '/usr/bin/sed -i /try_files/i\ \'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default',
}

exec { 'sed2':
  command => '/usr/bin/sed -i /"server_name _;"/a\ "error_page 404 /404.html;\n\n\tlocation /404.html {\n\t\troot /usr/share/nginx/html/;\n\t\tinternal;\n}" /etc/nginx/sites-available/default',
  require => Exec['sed1'],
}

service {'nginx':
  ensure    => running,
  require   => Package['nginx'],
  subscribe => Exec['sed2'],
}
