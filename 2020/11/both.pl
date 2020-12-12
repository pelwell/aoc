#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my $map;
my $stride;
my $rows;
while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	chomp($line);
	$map .= " $line";
	$rows++;
	$stride = length($map) if (!$stride);
}

my $blank = " " x $stride;
$map = $blank . $map . $blank . ' ';

my $map2 = $map;

while (1) {
	my $newmap = generation($map);
	last if ($newmap eq $map);
	$map = $newmap;
}

my $answer1 = $map =~ tr/#//;

printf("Part 1 answer: %d\n", $answer1);

while (1) {
	my $newmap = generation2($map2);
	last if ($newmap eq $map2);
	$map2 = $newmap;
}

my $answer2 = $map2 =~ tr/#//;

printf("Part 2 answer: %d\n", $answer2);

sub generation
{
	my ($map) = @_;
	my $newmap = $map;
	my $end = length($map) - $stride - 1;

	for (my $pos = $stride + 1; $pos <= $end; $pos++)
	{
		my $near = substr($map, $pos - $stride - 1, 3) .
			   substr($map, $pos - 1, 3) .
			   substr($map, $pos + $stride - 1, 3);
		if ((substr($near, 4, 1) eq 'L') && ($near !~ /#/))
		{
			substr($newmap, $pos, 1) = '#';
		}
		elsif ((substr($near, 4, 1) eq '#') && ($near =~ tr/#// >= 5))
		{
			substr($newmap, $pos, 1) = 'L';
		}
	}
	return $newmap;
}

sub generation2
{
	my ($map) = @_;
	my $newmap = $map;
	my $end = length($map) - $stride - 1;
	my @dirs =
	(
		-$stride - 1,
		-$stride,
		-$stride + 1,
		-1,
		1,
		$stride - 1,
		$stride,
		$stride + 1,
	);

	for (my $pos = $stride + 1; $pos <= $end; $pos++)
	{
		my $count = 0;
		my $atpos;
		foreach my $dir (@dirs)
		{
			my $scanpos = $pos;
			do
			{
				$scanpos += $dir;
				$atpos = substr($map, $scanpos, 1);
			} while ($atpos eq '.');
			$count++ if ($atpos eq '#');
		}
		$atpos = substr($map, $pos, 1);
		if (($atpos eq 'L') && ($count == 0))
		{
			substr($newmap, $pos, 1) = '#';
		}
		elsif (($atpos eq '#') && ($count >= 5))
		{
			substr($newmap, $pos, 1) = 'L';
		}
	}
	return $newmap;
}

sub print_map
{
	my ($map) = @_;

	print(join("\n", split(/ +/, $map)), "\n");
}
