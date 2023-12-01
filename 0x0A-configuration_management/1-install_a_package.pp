#installer of flask 2.1.0

#using pip3 install flask
package{ 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
