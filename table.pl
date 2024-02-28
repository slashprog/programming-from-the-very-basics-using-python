#!/usr/bin/env perl
print "Enter a number: ";
chomp($num = <STDIN>);
for ($i=1; $i<=10; $i++) {
	print "$num x $i =", $num*$i, "\n";
}

