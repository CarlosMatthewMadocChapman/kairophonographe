# Kairophonographe

**Version 0.6.0 — public research release**

Kairophonographe is an artistic-research system for translating a situated moment into reproducible musical decisions.

A session can combine weather, time, sound, image-derived observations, materials, geology, season and human traces. The engine does not assign a musical culture to a territory. It extracts forces from the situation and maps those forces to tempo, density, timbre, space, structure, silence and optional vocal behaviour.

> **A place gives forces. The engine turns those forces into musical decisions.**

## What is public here

This repository contains the stable and reproducible layer of the project:

- canonical mappings used by the reference engine;
- JSON Schemas for sessions, evaluations and promotion records;
- a deterministic reference API;
- sensor and Raspberry Pi acquisition contracts;
- reproducible reference examples;
- listening and evaluation protocols;
- publication, citation and contribution rules.

Raw recordings, precise private GPS traces, unpublished prompts, failed experiments and unfinished hypotheses are intentionally excluded from this public repository.

## Core pipeline

```text
situated input
  ↓
provenance + units + confidence
  ↓
anti-recycling gate
  ↓
force extraction
  ↓
weather / time / sound / matter / geology / season mappings
  ↓
kinetic arbitration
  ↓
Music ADN gestures + resonance palettes
  ↓
optional vocal transmutation
  ↓
structured music specification
  ↓
rendering prompt / implementation / listening test
  ↓
evaluation + learned rule candidate
```

The public reference engine stops at a structured **music specification**. It does not claim that weather, geology or animal sound have an inherent musical meaning. The mappings are explicit artistic rules that can be tested, compared, revised and cited.

## Mapping principles

The engine uses weighted influence rather than one-variable determinism:

- **temperature → kinetic/tempo bias + spectral body**;
- **humidity → acoustic fusion + spatial persistence**;
- **wind → spatial motion + modulation + drone behaviour**;
- **precipitation → event density + transient organisation**;
- **pressure → harmonic gravity + stability/tension**;
- **hour / light state → structural mode + register behaviour**;
- **season → orchestration bias**;
- **geology/material → timbral affordances**;
- **sound events → rhythm, microtiming, density and optional transmutation**;
- **place type → eligible palette families, never a presumed local style**.

Final tempo and structure always result from several signals. A hot day alone cannot force a fast track; a wet place alone cannot force ambient music.

## Repository map

```text
kairophonographe/
├── canon/          # machine-readable rules
├── schemas/        # JSON Schema contracts
├── api/            # reference HTTP API + deterministic engine
├── hardware/       # acquisition architecture and sensor contracts
├── examples/       # reproducible, non-governing examples
├── evaluation/     # listening protocol and scoring
├── docs/           # method, ethics, publication, Radio du Futur
├── scripts/        # validation and example runners
├── tests/          # machine tests
└── .github/        # CI
```

## Quick start

Python 3.11+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/validate_repo.py
pytest -q
uvicorn api.app:app --reload
```

Then open:

- `GET /health`
- `GET /v1/manifest`
- `GET /v1/mappings/{name}`
- `POST /v1/translate`

A complete request example is available in `examples/new-terrain/session.json`.

## Reproducibility contract

A reproducible session records:

1. source type for every input (`measured`, `api`, `observed`, `estimated`, `simulated`);
2. units and timestamp;
3. input values used by the engine;
4. mapping version;
5. engine version;
6. deterministic output specification;
7. exclusions and anti-recycling decisions;
8. listening evaluation after rendering.

The same normalized session and the same engine version must produce the same reference specification.

## Anti-recycling

Examples in this repository are **evidence and regression fixtures**, not templates for the next composition. A fresh simulation must renew the situation across place, climate, sound regime, time, kinetic behaviour, Music ADN gestures, resonance palettes and musical structure unless a comparison or reprise is explicitly requested.

## Public research scope

Kairophonographe can support artistic research, generative music, installations, territorial listening, cultural mediation, environmental pedagogy, participatory archives and Radio du Futur formats. Any scientific use must distinguish measured data from artistic interpretation and must not present project mappings as physical causal laws.

## Citation

See `CITATION.cff`. Release archives can be deposited in a DOI-granting repository without changing the internal session format.

## Licensing

- code: MIT — `LICENSE-CODE`;
- documentation and canonical JSON data: CC BY 4.0 — `LICENSE-CONTENT`;
- no source audio, photograph or third-party media rights are granted by this repository.
