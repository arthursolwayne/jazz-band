
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Start of sax melody
# Dorian mode, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D (G4)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F# (A4)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A (B4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F# (A4)
]

# Bass: walking line in D Dorian
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # Ab
]

# Piano: open voicings with tension
piano_notes = [
    # Bar 2: D7#9 (D, F#, A, C, E flat)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),   # Eb
    # Bar 3: G7#9 (G, B, D, F#, A flat)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),   # F#
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),   # Ab
    # Bar 4: C7#9 (C, E, G, B, D flat)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),   # Db
]

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
