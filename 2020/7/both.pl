#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;
my $count1 = 0;
my $count2 = 0;

my %contains;
my %fitsin;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	$line =~ s/(?: bags?| contain| no other bags|[\.,\n])//g;
	my @toks = split(" ", $line);
	my $src = $toks[0]." ".$toks[1];
	my $node = $contains{$src} ||= [];
	for (my $i = 2; $i < @toks; $i += 3)
	{
		my $tp = $toks[$i+1]." ".$toks[$i+2];
		push @$node, [$toks[$i], $tp];
		push @{$fitsin{$tp}}, $src;
	}
}

my %containers;

my @frontier = ('shiny gold');

while (@frontier)
{
	my $head = shift @frontier;
	foreach my $new (@{$fitsin{$head}})
	{
		if (!$containers{$new})
		{
			$containers{$new} = 1;
			push @frontier, $new;
			$count1++;
		}
	}
}

printf("Part 1 answer: %d\n", $count1);

@frontier = ([1, 'shiny gold']);

while (@frontier)
{
	my $head = shift @frontier;
	my ($mult, $type) = @$head;

	foreach my $node (@{$contains{$type}})
	{
		my $new_count = $mult * $node->[0];
		$count2 += $new_count;
		push @frontier, [ $new_count, $node->[1]];
	}
}

printf("Part 2 answer: %d\n", $count2);
