#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my @list;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	chomp($line);
	push @list, $line;
}

@list = sort { $a <=> $b } (@list);

my @hist;
my $last = 0;
my $onediffcount = 0;

my $count = 1;
my @runmult = (1, 1, 2, 4, 7);

foreach my $jolts (@list)
{
	my $diff = $jolts - $last;
	# printf("%d->%d = %d\n", $last, $jolts, $jolts - $last);
	$hist[$diff]++;
	if ($diff == 1) {
		$onediffcount++;
	} elsif ($onediffcount) {
		$count *= $runmult[$onediffcount];
		$onediffcount = 0;
	}
	$last = $jolts;
}

$count *= $runmult[$onediffcount];

$hist[3]++;

printf("Part 1 answer: %d\n", $hist[1]*$hist[3]);
printf("Part 2 answer: %d\n", $count);
