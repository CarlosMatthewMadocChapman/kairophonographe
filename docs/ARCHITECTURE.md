# Architecture

```text
[ACQUISITION]
weather / sound / image / time / material observations
        │
        ▼
[NORMALIZATION]
units + provenance + privacy reduction
        │
        ▼
[SESSION JSON]
        │
        ├── validation
        ├── anti-recycling gate
        ▼
[REFERENCE TRANSLATOR]
weather + time + season + geology + sound + place
        │
        ├── kinetic arbitration
        ├── palette selection
        ├── vocality eligibility
        ▼
[MUSIC SPEC]
        │
        ├── score / synthesis
        ├── live engine
        └── prompt renderer
        ▼
[LISTENING EVALUATION]
        │
        └── promotion candidate → tested public mapping change
```

## Boundary rule

The acquisition layer may change hardware. The rendering layer may change music models or software. A canonical session remains interpretable because normalized inputs and mapping version are preserved.

## Determinism

The public translator contains no random choice. Random or generative renderers may exist downstream, but their seed/configuration should be archived when reproducibility matters.
