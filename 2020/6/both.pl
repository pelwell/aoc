#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my $present_bits1 = 0;
my $present_num1 = 0;
my $count1 = 0;
my $present_bits2 = ~0;
my $count2 = 0;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	if ($line =~ /^\s*$/)
	{
		$count1 += $present_num1;
		$present_num1 = 0;
		$present_bits1 = 0;
		$count2 += count_bits($present_bits2);
		$present_bits2 = ~0;
		last if (!$line);
		next;
	}
	my $user_bits = 0;
	while ($line =~ /([a-z])/g)
	{
		my $bit = (1 << (ord($1) - ord('a')));
		if (!($present_bits1 & $bit))
		{
			$present_bits1 |= $bit;
			$present_num1++;
		}
		$user_bits |= $bit;
	}
	$present_bits2 &= $user_bits;
}

printf("Part 1 answer: %d\n", $count1);
printf("Part 2 answer: %d\n", $count2);

sub count_bits
{
	my ($num) = @_;
	my $count = 0;

	for (my $i = 1; $num; $i <<= 1)
	{
		if ($num & $i)
		{
			$num &= ~$i;
			$count++;
		}
	}
	return $count;
}
