# Promotion workflow

Experimental work enters the stable public layer only through an explicit promotion record.

Required fields:

```yaml
element:
source:
location:
claim_class:
tests:
limitations:
target_version:
publication_decision:
```

Promotion requires:

1. at least one reproducible test;
2. an explicit claim class;
3. limitations stated in plain language;
4. no private data or uncleared media;
5. a regression test when the change affects machine output;
6. a decision of `promote` before inclusion in `canon/`.

The experimental source remains conceptually separate from the public rule. Promotion copies a tested claim, not an entire private working history.
