# MERRILL – Micromagnetic Modelling

MERRILL (Micromagnetic Earth Related Robust Interpreted Language Laboratory) is an open source 3D micromagnetics software package with a simple scripting user interface for modelling complex, inhomogeneous domain structures in magnetic materials.

MERRILL uses a finite-element/boundary-element approach well suited to irregular grain geometries of interest to the rock and palaeomagnetic community, and can simulate magnetic characteristics of both single grains and small assemblies of interacting grains. The open source nature of the code encourages future development by the scientific community.

## Running the site locally

```bash
uvicorn app.main:app --reload
```

Then open `http://localhost:8000` in your browser.

## Changes on 2026‑03‑19

-   Added shared layout in `base.html` with navigation, header band, and footer.
-   Moved styles and scripts into `app/static/css/main.css` and `app/static/js/main.js`.
-   Created `home.html` with an overview of MERRILL and links to key sections.
-   Added Tutorials section (`tutorials.html`) and Tutorial 1 page (`tutorial_1.html`) with embedded video.
-   Registered `tutorial_1_controller.py` in the FastAPI application.

## Git workflow (for future me and collaborators)

Basic rule: work in small steps and sync often.

### Starting work

```bash
git pull origin main
git status
```

This makes sure you have the latest changes before editing.

### While working

- Make small, logical changes that keep the code running.
- When a small piece is done (e.g. new page, layout tweak, bug fix):

```bash
git status                # see what changed
git add <files you changed>
git commit -m "Short description of this change"
```

Examples:
- `git commit -m "Add Tutorial 1 page and controller"`
- `git commit -m "Improve base layout and move CSS to static file"`

### Pushing changes

Push after one or three commits or whenever you stop working:

```bash
git push origin main
```

### Stopping for the day

```bash
git status        # should say 'working tree clean'
git push origin main
```

This keeps Bitbucket up to date so another machine (or collaborator) can safely run `git pull origin main` next time.