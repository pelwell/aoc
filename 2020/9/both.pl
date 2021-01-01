#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my @list;
my $preamble_len = 25;
$preamble_len = 5 if (@ARGV);
my $answer1;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	chomp($line);
	if (@list >= $preamble_len)
	{
		if (!find_pair_with_sum($line, @list[(@list - $preamble_len)..(@list - 1)]))
		{
			$answer1 = $line;
			last;
		}
	}
	push @list, $line;
}

printf("Part 1 answer: %d\n", $answer1);

my $answer2;
my $i = 0;
my $j = 1;
my $sum = $list[0] + $list[1];

while ($i < (@list - 1))
{
	if ($sum == $answer1)
	{
		my @sublist = sort { $a <=> $b } @list[$i..$j];
		$answer2 = $sublist[0] + $sublist[@sublist - 1];
		last;
	}
	elsif ($sum > $answer1)
	{
		$sum -= $list[$i];
		$i++;
	}
	else
	{
		$j++;
		$sum += $list[$j];
	}
}

printf("Part 2 answer: %d\n", $answer2);

sub find_pair_with_sum
{
	my ($sum, @arr) = @_;
	@arr = sort { $a <=> $b } @arr;
	my $i = 0;
	my $j = @arr - 1;
	while ($i < $j)
	{
		my $pairsum = $arr[$i] + $arr[$j];
		return 1 if ($pairsum == $sum);
		if ($pairsum > $sum)
		{
			$j--;
		}
		else
		{
			$i++;
		}
	}
	return 0;
}
