#!/usr/bin/env python

a="ATGTATCTAGATCGATCGACGATCGATCGGATCGATCGGGATCGATCGAGAGAGCTAGCTTAGAGAGAGCTAGAGCTAGCATCGATTATCGATCG"
A1=a.count("A")
A2=a.count("T")
A3=a.count("G")
A4=a.count("C")
p1=p2=p3=p4=0
if A1+A2+A3+A4==len(a):
    print float(A1+A3)/len(a)
    print(len(a))
    p1=a.count("CTA")
    p2=a.count("CTG")
    p3=a.count("CTC")
    p4=a.count("CTT")
if p1>0:
    print "found"
if p2>0:
    print "found"
if p3>0:
    print "found"
if p4>0:
    print "found"




