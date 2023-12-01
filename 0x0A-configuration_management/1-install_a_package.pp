#installer of flask 2.1.0

exec {'apt-get update':
  command => '/usr/bin/apt-get update'
}

package{ 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

package{ 'Flask':
  ensure  => '2.1.0',
  provider => 'pip3'
}
