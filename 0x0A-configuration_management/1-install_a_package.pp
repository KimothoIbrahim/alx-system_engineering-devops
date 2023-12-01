#installer of flask 2.1.0

package{ 'python3':
  ensure => 'installed'
}

package{ 'python3-pip':
  ensure  => 'installed',
  require => Package['python3']
}

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
