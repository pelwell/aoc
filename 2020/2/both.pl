#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', 'input.txt'));

my $count1 = 0;
my $count2 = 0;

while (my $line = <$fh>)
{
	if ($line =~ /^(\d+)-(\d+) ([a-z]): ([a-z]+)/) {
		my ($a, $b, $letter, $password) = ($1, $2, $3, $4);
		my $num = () = $password =~ /$letter/g;
		$count1++ if ($num >= $a && $num <= $b);
		my $c = substr($password, $a - 1, 1);
		my $d = substr($password, $b - 1, 1);
		$count2++ if (($c eq $letter) != ($d eq $letter));
	}
}

printf("Answer to part 1: %d\n", $count1);
printf("Answer to part 2: %d\n", $count2);
