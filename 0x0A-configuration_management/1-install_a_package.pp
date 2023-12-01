#installer of flask 2.1.0

#install pip3
package{ 'python3-pip':
  ensure  => 'installed',
}

#using pip3 install flask
package{ 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
