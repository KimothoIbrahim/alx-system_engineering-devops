#install flask using pip3

# Install pip3
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask using pip3
package { 'Flask':
  ensure   => 'latest',
  provider => 'pip3',
}
