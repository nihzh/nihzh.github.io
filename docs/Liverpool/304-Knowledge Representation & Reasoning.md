## Logic
Any Logic comes in three parts
- a language, that defined the *well-formed formulas (wffs)*
- semantics, that five meaning to formulas
- a deduction system, that allows us to find valid (guaranteed to be true) formulas

## Reminder Propositional Logic (PL)
- Formal system to precisely describe reasoning
- almost all symbolic reasoning
- uncontroversial & limited in applicability

### Language
Set P of atoms, P = p, q, p1, p2, ...
- represent *basic facts* that we dont analyze further

*Well-formed formulas (wff)*
- Every p ∈ P is a wff
- If A and B are wffs, then (A § B) or (§a) are wffs
- Nothing else if a wff (propositional)

Use brackets if this do cause ambiguity
- negation binds stronger than other connectives

#### Greeks
![](../img/IMG_1326.PNG)

#### Pronunciation
- `¬` negation, usually pronounced: "not"
- `∧` conjunction, "and"
- `∨` disjunction, "or"
- `→` imnplicatoin, "implies" or "if... then.."
- `↔` bi-implicatoin, "if and only if" (异或xor)

### Semantics
Exact meaning of connectives is determined by the *semantics*: *Truth tables*

Truth or falsity of a propositional formula depends on the truth/falsity of the atoms in the formula.

#### Valid formulas
The formulas that are always true
Notation: 
- `|= φ` (valid)
- `|=/`(non-validity)

#### Valid Inference
If (i) p is true and (ii) q is true, then `p ∧ q` is guaranteed to be true as well.
- `{p, q} |=  p ∧ q` where `p` and `q` are the *premises*, `p ∧ q` is the conclusion.
- `Γ |= φ` if the set of *premises* `Γ` guarantee the truth of the conclusion `φ`
- `φ` is valid if the inference from `∅` to `φ` is valid, So `|= φ` if and only if `∅ |= φ`

##### Semantical Valid Inferences
Check whether every row that makes all premises true makes thet conclusion true
- *Counterexamples*: row in a truth table where premises true, conclusion false, exists when an inference is not valid

##### Syntactically Valid Inferences
Use a formal proof system, with *premises* and *axioms*, derive new valid inferences using an inference rule

#### Derivation
Notation: Γ ⊢P φ if φ can be derived Γ in P
Rule (MP): if you have derived φ and φ → ψ, derive ψ.
![](../img/IMG_1328.PNG)

A proof system is only considered useful if it is *sound* and *complete*
- Soundness: If Γ ⊢P φ, then Γ |= φ. So we can only derive valid inferences
- Completeness: If Γ |= φ, then Γ ⊢P φ. So every valid inference can be derived

#### Abbreviations
`⊤` something that is always true
`⊥` something that is always false

#### Abbreviation
- φ ∧ ψ can abbreviate ¬(¬φ ∨ ¬ψ)
- φ → ψ can abbreviate ¬φ ∨ ψ
- φ ↔ ψ can abbreviate (φ → ψ) ∧ (ψ → φ)

So propositional logic can be defined as: `φ ::= p | ¬φ | φ ∨ φ`

## Modal Logic (ML)
- Extension of propositional logic -> *modalities*
- also concerned when, where, to which extent and how something is true
- the basis for EL and DL

Language of modal logic: `φ ::= p | ¬φ | φ ∨ φ | □φ  `
- Also `♢φ` abbreviation for `¬□¬φ`

- Alethic □φ means: “φ is necessarily true.”
- Epistemic □φ means: “I know that φ is true.”
- Doxastic □φ means: “I believe that φ is true.”
- Temporal □φ means: “At every time in the future, φ will be true.”
- Deontic □φ means: “φ should be true.”
- Legal □φ means: “φ is legally required to be true.”

- Alethic ♢φ means: “φ is possibly true.”
- Epistemic ♢φ means: “as far as I know, φ might be true.”
- Doxastic ♢φ means: “I believe that φ might be true.”
- Temporal ♢φ means: “At some time in the future, φ will be true.”
- Deontic ♢φ means: “φ is allowed to be true.”
- Legal ♢φ means: “it is legal for φ to be true.”

- Temporal: □♢p.
At every point in the future, p will be true some later time.
- Deontic: □p → ♢p.
If p is mandatory then it is also permitted.
- Legal: ¬♢□¬p.
It is not permitted to forbid p.
- Epistemic: □p → □□p.
If I know p, then I know that I know p.

![[Pasted image 20241028220320.png]]

![[Pasted image 20241028220352.png]]

## Epidemic Logic (EL)

## Description Logic (DL)
