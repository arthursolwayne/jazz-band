
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # Eb
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: motif (Bar 2)
# F, G, Bb, F (played over 2 bars)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Same pattern, shifted
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

# Bar 3: Bass continues (add fourth bar)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # C#
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues (add fourth bar)
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # Eb
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # Eb
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues
# Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
