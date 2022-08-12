# Using puppet this code is for creating a file
file { '/tmp/school':
ensure   => 'file',
path     => '/tmp/school',
mode     => '0744',
owner    => 'www-data',
group    => 'www-data',
contains => 'I love Puppet',
}
