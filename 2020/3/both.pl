#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;
my @map;

while (my $line = <$fh>)
{
	$linenum++;
	if ($line =~ /^([\.#]+)\s*$/)
	{
		push @map, $1;
	}
}

my $answer = count_trees(\@map, 3, 1);

printf("Part 1 answer: %d\n", $answer);

$answer *= count_trees(\@map, 1, 1);
$answer *= count_trees(\@map, 5, 1);
$answer *= count_trees(\@map, 7, 1);
$answer *= count_trees(\@map, 1, 2);

printf("Part 2 answer: %d\n", $answer);

sub count_trees
{
	my ($map, $dx, $dy) = @_;
	my $width = length($map->[0]);
	my $height = @$map;
	my $trees = 0;
	my $x = 0;
	my $y = 0;

	while ($y < $height)
	{
		$x += $dx;
		$y += $dy;
		$trees++ if (substr($map->[$y], $x % $width, 1) eq '#');
	}

	return $trees;
}
