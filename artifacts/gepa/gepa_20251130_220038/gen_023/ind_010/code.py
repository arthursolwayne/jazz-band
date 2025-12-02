
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D - F# - B - D (motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line in D (D - C - B - A - G - F# - E - D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),  # C
    # D7 again on beat 4 (2.25 - 2.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats the motif but a half-step higher (E - G - C - E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# E7 (E, G#, B, D)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),  # G#
    pretty_midi.Note(velocity=95, pitch=72, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=95, pitch=62, start=3.25, end=3.5),  # D
    # E7 again on beat 4 (3.75 - 4.0s)
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif with a resolution to D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=5.75, end=6.0),  # F#
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=6.25, end=6.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0),  # C
    # D7 again on beat 4 (5.25 - 5.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums continue with same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
