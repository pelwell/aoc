#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $line = <$fh>;

chomp($line);

my @starters = split(',', $line);

my @last_seen;
my $last = 0;
my $turn = 0;

foreach my $num (@starters)
{
	$last_seen[$last] = $turn;
	$turn++;
	$last = $num;
}

my $print_at = 1000;
while ($turn < 30000000)
{
	my $next = 0;
	my $when = $last_seen[$last];
	$next = $turn - $when if ($when);
	$last_seen[$last] = $turn;
	$turn++;
	$last = $next;
	printf("Part 1 answer: %d\n", $last) if ($turn == $2020);
	if ($turn == $print_at)
	{
		printf("%d: %d\n", $turn, $last);
		$print_at *= 2
	}
}

printf("Part 2 answer: %d\n", $last)
