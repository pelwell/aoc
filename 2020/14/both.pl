#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my @memory;
my $mask_set = 0;
my $mask_clr = 0;

while (my $line = <$fh>)
{
	if ($line =~ /^mask = ([01X]{36})/)
	{
		my $mask_val = $1;
		$mask_set = 0;
		$mask_clr = 0;
		for (my $i = 0; $i < 36; $i++)
		{
			my $c = substr($mask_val, $i, 1);
			$mask_set |= (1 << (35 - $i)) if ($c eq '1');
			$mask_clr |= (1 << (35 - $i)) if ($c eq '0');
		}
	}
	elsif ($line =~ /^mem\[(\d+)\] = (\d+)/)
	{
		$memory[$1] = ($2 & ~$mask_clr) | $mask_set;
	}
	else
	{
		die "* Bad line\n"
	}
}

my $answer1 = 0;
foreach my $val (@memory)
{
	$answer1 += $val;
}

printf("Part 1 answer: %d\n", $answer1);
