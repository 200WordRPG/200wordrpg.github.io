---
layout: post
title: 'v4: Social Media Impocalypse'
tags: [hyde]
description: >
  This release adds *a lot* of social media icons and introduces a new default layout. It also breaks things, hence a new major release number.
---

## Breaking
* Structure of `_config.yml` has changed
  * Social media usernames are now located under `author: social: <platform>: <username>`.
  * `disqus` is now a top-level entry (moved from `author`).
  * Now has `font`, `font_accent` and `google_fonts` fields that are mandatory.
* Now defaults to the `blog` layout, old style is available via `blog-by-tag` layout, see `archive.html`.

## New features
* Added *a lot* of social media icons, configurable via `_config.yml`.
* New `blog` layout. Classic, paginated.
* Fonts are configurable via `_config.yml`.

## Design
* Link underlines are now fixed-sized for all font sizes (no thicker lines for headlines, etc)

## Fixes
* Correctly set the meta description field using either the `description` field or `post.excerpt` as a fallback (used to contain the unmodified markdown).
* Fixed various URL bugs relating to `site.baseurl`.

## Internal
* Refactoring, preventing code duplications, heavier usage of `includes`.
