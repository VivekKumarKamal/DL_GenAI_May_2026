# Axiom schema

> **Query Topic**: role of axioms in a formal principle (Rank #3 Search Result)
> **Source Queue**: train (Row ID: 198, Frequency: 5)
> **Wikipedia Page**: https://en.wikipedia.org/wiki/Axiom_schema

---

In mathematical logic , an axiom schema (plural: axiom schemata or axiom schemas ) is a rule or template that specifies a family of axioms . A schema contains placeholders together with side conditions saying how those placeholders may be replaced; each permitted replacement is an instance of the schema. Axiom schemata are commonly used to give finite descriptions of theories whose axioms include infinitely many formulas.

## Formal definition

Let $L$ be the object language of a formal theory. An axiom schema is a metalinguistic expression, or schema-template, containing one or more placeholders for expressions of $L$ , together with side conditions specifying the expressions that may replace the placeholders. The resulting object-language formulas are the instances of the schema and are taken as axioms of the theory.

The placeholders in an axiom schema may stand for terms, formulas, predicates, or relations, depending on the formal system. Side conditions often require that a term be free for a variable in a formula, that a variable occur free in a formula, or that a variable not occur free in a specified formula. Such conditions are part of the schema, not additional axioms of the object language.

This distinguishes a schematic letter from an ordinary object-language variable. For example, a schematic letter may be a placeholder for any formula of a language, whereas an object-language variable ranges over objects in the domain of interpretation.

## Examples

### First-order logic

Many Hilbert-style presentations of first-order logic use axiom schemata. For example, the quantifier axiom schema

$\forall x\,\Phi (x)\rightarrow \Phi (t)$

has as instances the formulas obtained by replacing $\Phi$ with an object-language formula and $t$ with a term, subject to the condition that $t$ is free for $x$ in $\Phi$ . Rules or axiom schemata of this kind avoid listing separately every formula obtained by the permitted substitutions.

### Arithmetic

A standard first-order presentation of Peano arithmetic includes the induction schema. For every formula $\varphi (x,{\vec {y}})$ in the language of arithmetic, with possible parameters ${\vec {y}}$ , the schema has an instance of the form

${\bigl (}\varphi (0,{\vec {y}})\land \forall x(\varphi (x,{\vec {y}})\rightarrow \varphi (Sx,{\vec {y}})){\bigr )}\rightarrow \forall x\,\varphi (x,{\vec {y}}).$

Thus the induction principle is not a single first-order axiom but a family of axioms, one for each admissible formula $\varphi$ .

Czesław Ryll-Nardzewski proved that first-order Peano arithmetic is not finitely axiomatizable in its usual language. Consequently, the induction schema cannot be replaced, in that language, by a finite list of axioms with the same deductive consequences.

### Set theory

The standard first-order axiomatization ZFC contains axiom schemata, including the schema of separation and the schema of replacement . In the replacement schema, each formula that defines a functional relation gives an axiom asserting that the image of any set under that definable function is also a set.

Richard Montague proved a non-finite axiomatizability result for ZF-style set theories; in particular, assuming consistency, ZFC is not finitely axiomatizable in its ordinary first-order language. Hence the replacement and separation schemata cannot simply be eliminated from ZFC by replacing them with finitely many axioms in the same language.

## Finite axiomatization

A theory is finitely axiomatizable if there is a finite set of sentences whose deductive closure is exactly the theory. An axiom schema may be finitely describable while still specifying infinitely many axioms, since the schema is a metatheoretic recipe for generating instances rather than a finite set of object-language sentences.

Whether a theory is finitely axiomatizable depends on the language in which the theory is formulated. A theory that is not finitely axiomatizable in one language may have a finitely axiomatized conservative extension in a richer language.

### Finitely axiomatized related theories

Von Neumann–Bernays–Gödel set theory (NBG) extends the language of set theory by adding classes. NBG is a conservative extension of ZFC for statements about sets, but unlike ZFC it can be finitely axiomatized: its class-existence theorem is obtained from finitely many class-existence axioms rather than from a schema.

New Foundations (NF), introduced by W. V. O. Quine , is usually presented with extensionality and a stratified comprehension schema. Theodore Hailperin showed in 1944 that this comprehension principle is equivalent to a finite conjunction of instances, giving a finite axiomatization of NF. Later presentations of NF and related systems may take finite axioms as basic and prove stratified comprehension as a theorem.

## In higher-order logic

Some axiom schemata in first-order theories can be replaced by single axioms in a higher-order language. For example, the first-order induction schema for arithmetic has a second-order analogue in which a variable quantifies over properties or classes directly:

$\forall F{\bigl (}(F(0)\land \forall x(F(x)\rightarrow F(Sx)))\rightarrow \forall x\,F(x){\bigr )}.$

In this second-order sentence, $F$ is a genuine variable ranging over properties or classes, not a metalinguistic placeholder. The second-order induction axiom and the first-order induction schema are therefore formally different, and the second-order axiom is stronger under the standard semantics for second-order logic.

Analogously, some first-order set-theoretic schemata can be represented by quantifying over classes or higher-order objects in an expanded language. This is one reason class theories such as NBG can give finite axiomatizations while remaining conservative over ZFC for set-theoretic sentences.
