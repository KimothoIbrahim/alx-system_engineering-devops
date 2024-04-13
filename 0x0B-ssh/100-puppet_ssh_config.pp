$str = "Host *\n\tHostName 100.25.158.57\n\tUser ubuntu\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school"

file { '/home/kimotho/.ssh/config':
  content => $str,
}
