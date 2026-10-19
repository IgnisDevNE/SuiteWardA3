# SuiteWardA3

Acceptance repository for SuiteWard M1.9 (scope discovery). It holds on purpose:

- `AGENTS.md`, a symbolic link to `CLAUDE.md`;
- `libs/shared`, a git submodule;
- `package.json`, a file that may hold test settings;
- a Python test with no pytest configuration;
- no `.suiteward.yml`.

The Ruby spec in `spec/` exercises the same function.

Jest reads `jest.config.js` at the repository root.

The link `spec_link` points to the `app` directory.
