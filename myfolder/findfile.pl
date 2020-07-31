#file finding code

use strict; 
use warnings; 
use File::Find; 


no warnings;
my $dir= 'C:\Users\sudethak';
find(\&wanted, $dir);

sub wanted{
	
	no warnings;

	print "$File::Find::name\n" if (-f $File::Find::name and /Geeks.txt$/); 
	
}