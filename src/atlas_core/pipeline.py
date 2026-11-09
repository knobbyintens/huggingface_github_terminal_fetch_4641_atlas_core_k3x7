"""Minimal dataset pipeline used by Atlas experiments."""


def iter_batches(records, batch_size=32):
    for start in range(0, len(records), batch_size):
        yield records[start:start + batch_size]
