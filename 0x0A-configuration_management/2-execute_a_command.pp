# Create a manifest file

exec { 'killmenow':
  command     => 'pkill -f killmenowe', # Replace 'my_process_name' with the actual process name or pattern
  path        => ['/bin', '/usr/bin'],        # Adjust the path as needed
  onlyif      => 'pgrep -f killmenow',  # Check if the process is running before attempting to kill it
  refreshonly => true,
}
