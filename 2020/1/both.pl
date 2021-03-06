#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', 'input.txt'));

my @list;
my @arr;

while (my $line = <$fh>)
{
	if ($line =~ /^(\d+)\s*$/) {
		$arr[$1] = 1;
		push @list, $1;
	}
}

my @found = sum_to(\@arr, \@list, 2020);

printf("Part 1 answer: %d\n", $found[0] * $found[1]);

foreach my $val (@list)
{
	my @found2 = sum_to(\@arr, \@list, 2020 - $val);
	if (@found2 != 0)
	{
		@found = ($val, $found2[0], $found2[1]);
		last;
	}
}

printf("Part 2 answer: %d\n", $found[0] * $found[1] * $found[2]);

sub sum_to
{
	my ($arr, $list, $sum) = @_;
	foreach my $val (@$list)
	{
		return ($val, $sum - $val) if (($val < $sum) && $arr[$sum - $val]);
	}
	return ();
}
