#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my $north = 0;
my $east = 0;
my $heading = 0;
my $ship_north = 0;
my $ship_east = 0;
my $way_north = 1;
my $way_east = 10;

print("east $ship_east, north $ship_north\, way east $way_east, way north $way_north\n");

while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	chomp($line);
	if ($line =~ /^([NSEWRLF])(\d+)/)
	{
		my ($dir, $steps) = ($1, $2);
		my $movedir = $dir;
		my $rotate = 0;
		my $way_steps = 0;
		if ($dir eq 'L')
		{
			$rotate = $steps;
		}
		elsif ($dir eq 'R')
		{
			$rotate = 360-$steps;
		}
		elsif ($dir eq 'F')
		{
			$movedir = substr('ENWS', $heading/90, 1);
			$ship_north += $way_north * $steps;
			$ship_east += $way_east * $steps;
		}
		else
		{
			$way_steps = $steps;
		}
		if ($rotate)
		{
			$heading = ($heading + $rotate) % 360;
			my $prev_east = $way_east;
			my $prev_north = $way_north;
			if ($rotate == 90)
			{
				$way_east = -$prev_north;
				$way_north = $prev_east;
			}
			elsif ($rotate == 180)
			{
				$way_east = -$prev_east;
				$way_north = -$prev_north;
			}
			elsif ($rotate == 270)
			{
				$way_east = $prev_north;
				$way_north = -$prev_east;
			}
		}
		if ($movedir eq 'N')
		{
			$north += $steps;
			$way_north += $way_steps;
		}
		elsif ($movedir eq 'S')
		{
			$north -= $steps;
			$way_north -= $way_steps;
		}
		elsif ($movedir eq 'E')
		{
			$east += $steps;
			$way_east += $way_steps;
		}
		elsif ($movedir eq 'W')
		{
			$east -= $steps;
			$way_east -= $way_steps;
		}
	}
	print("$line: east $ship_east, north $ship_north\, way east $way_east, way north $way_north\n");
}

printf("Part 1 answer: %d\n", abs($north) + abs($east));
printf("Part 2 answer: %d\n", abs($ship_north) + abs($ship_east));
