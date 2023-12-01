#installer of flask 2.1.0

exec {'apt-get update':
  command => '/usr/bin/apt-get update'
}

#install pip3
package{ 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

#using pip3 install flask
package{ 'Flask':
  ensure  => '2.1.0',
  provider => 'pip3'
}
