# Release privacy

The release contains source references, technical explanations, public credits and local verification tools. Personal screenshots, recordings, chat transcripts, approval messages, account/device details, machine paths and internal session names are not distributed.

The source files are byte-identical to the selected research collection. Public authorship and upstream notices are retained. A business support address in one original game string is preserved as source data; it is not a contributor contact. Function names containing `conversation`, game user-interface code and original asset paths are technical source content.

Internal evidence locations are replaced by anonymous `archived-record-...` IDs. Original evidence hashes and bounded claim limits remain. The private location map and full execution/review records are not included. The public summary does not pretend those private records are independently downloadable.

The release starts with a fresh Git history using a neutral project alias. Earlier private repository history is not part of that history or the ZIP. The ZIP contains only the exact files in [the release manifest](../provenance/release-manifest.json), with fixed timestamps and file permissions.

`python -B tools/check_release.py` checks every present file, including files ignored by Git. It rejects unexpected files, images and other unapproved file types, links to outside folders, mismatched hashes, recognized machine/session/contact/credential patterns and unsafe Git metadata. It also inspects historical files reachable through Git, so deleting a private file in a later commit does not make it safe to publish.

These are bounded automated checks. Review newly added prose and source data before updating the manifest; patterns cannot recognize every possible personal fact or secret. Save execution reports outside the frozen release.
