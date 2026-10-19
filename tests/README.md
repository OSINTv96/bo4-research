# Tests

Run `python -B -m unittest discover -s tests -p 'test_*.py'`.
The checker tests exercise meaningful failure paths using temporary copies:
unregistered source, a broken local link, source identity tampering, a stray
binary input, a private home path and a path escaping the repository. These are repository checks,
not game tests.

Add future behavior tests only for an actual supported contract. Record the
source/build assumptions and distinguish a local model from a real game result.
