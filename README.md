pyrif
=====

A python implementation for the RIF W3C standard


# Description 
This is a mapping that parse any of the following standards to RIF and from RIF to anyone in the list.

## Supported list
* RIF
* SPIN SPARQL
* RuleML
* SWRL

## Supported Notations

* OWL 2 
* RDF/XML
* JSON-LD
* rdflib supported formats

# Behavior-Driven Development  (BDD)

This library was developed based on the BDD paradigm and a super cool library implementing just that:
http://lettuce.it/index.html

To run the BDD tests, run 

$ lettuce tests/

# UnitTests

Run them all by simple, run

$ nosetests
