
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.375, 0.125),   # Hihat on 1&2
    (42, 0.5, 0.125),     # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 1.125, 0.125),   # Hihat on 3&4
    (42, 1.25, 0.125),    # Hihat on 4
    (38, 1.5, 0.125)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# D major: D, E, F#, G, A, B, C#
# Sax melody - short motif, D to B, with a twist

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    (62, 1.5, 0.375),     # D
    (65, 1.875, 0.375),   # F#
    (67, 2.25, 0.375),    # A
    (69, 2.625, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking in D)
bass_notes = [
    (62, 1.5, 0.375),     # D
    (64, 1.875, 0.375),   # E
    (65, 2.25, 0.375),    # F#
    (67, 2.625, 0.375),   # A
    (69, 3.0, 0.375),     # B
    (67, 3.375, 0.375),   # A
    (65, 3.75, 0.375),    # F#
    (64, 4.125, 0.375)    # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chord (D7 on 2 and 4)
piano_notes = [
    (62, 1.5, 0.375),     # D
    (67, 1.5, 0.375),     # A
    (69, 1.5, 0.375),     # B
    (64, 1.5, 0.375),     # E
    (62, 3.0, 0.375),     # D
    (67, 3.0, 0.375),     # A
    (69, 3.0, 0.375),     # B
    (64, 3.0, 0.375)      # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0 - 4.5s)
# Drums
drum_notes = [
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.375, 0.125),   # Hihat on 1&2
    (42, 3.5, 0.125),     # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 4.125, 0.125),   # Hihat on 3&4
    (42, 4.25, 0.125),    # Hihat on 4
    (38, 4.5, 0.125)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: repeat motif with variation
sax_notes = [
    (62, 3.0, 0.375),     # D
    (65, 3.375, 0.375),   # F#
    (67, 3.75, 0.375),    # A
    (69, 4.125, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking in D)
bass_notes = [
    (62, 3.0, 0.375),     # D
    (64, 3.375, 0.375),   # E
    (65, 3.75, 0.375),    # F#
    (67, 4.125, 0.375),   # A
    (69, 4.5, 0.375),     # B
    (67, 4.875, 0.375),   # A
    (65, 5.25, 0.375),    # F#
    (64, 5.625, 0.375)    # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chord (D7 on 2 and 4)
piano_notes = [
    (62, 3.0, 0.375),     # D
    (67, 3.0, 0.375),     # A
    (69, 3.0, 0.375),     # B
    (64, 3.0, 0.375),     # E
    (62, 4.5, 0.375),     # D
    (67, 4.5, 0.375),     # A
    (69, 4.5, 0.375),     # B
    (64, 4.5, 0.375)      # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4 (4.5 - 6.0s)
# Drums
drum_notes = [
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.875, 0.125),   # Hihat on 1&2
    (42, 5.0, 0.125),     # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.625, 0.125),   # Hihat on 3&4
    (42, 5.75, 0.125),    # Hihat on 4
    (38, 6.0, 0.125)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: resolution
sax_notes = [
    (69, 4.5, 0.375),     # B
    (67, 4.875, 0.375),   # A
    (65, 5.25, 0.375),    # F#
    (62, 5.625, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking in D)
bass_notes = [
    (62, 4.5, 0.375),     # D
    (64, 4.875, 0.375),   # E
    (65, 5.25, 0.375),    # F#
    (67, 5.625, 0.375),   # A
    (69, 6.0, 0.375),     # B
    (67, 6.375, 0.375),   # A
    (65, 6.75, 0.375),    # F#
    (64, 7.125, 0.375)    # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chord (D7 on 2 and 4)
piano_notes = [
    (62, 4.5, 0.375),     # D
    (67, 4.5, 0.375),     # A
    (69, 4.5, 0.375),     # B
    (64, 4.5, 0.375),     # E
    (62, 6.0, 0.375),     # D
    (67, 6.0, 0.375),     # A
    (69, 6.0, 0.375),     # B
    (64, 6.0, 0.375)      # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
