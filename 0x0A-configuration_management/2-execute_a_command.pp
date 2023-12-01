# Create a manifest file killing the process killmenow

exec { 'name':
  command => '/usr/bin/pkill killmenow'
}
