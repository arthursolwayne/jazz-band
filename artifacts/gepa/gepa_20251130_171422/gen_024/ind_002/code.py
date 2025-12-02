
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, tension, variation
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    # Bar 1 - 0.0 to 1.5s
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# One short, emotionally resonant motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Bass enters with active, melodic line (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=85, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=85, pitch=47, start=2.75, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano enters with emotional comping (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax repeats motif
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
])

for note in sax_notes:
    sax.notes.append(note)

# Bass continues with active, chromatic line
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=85, pitch=50, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=85, pitch=53, start=3.75, end=4.0),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=85, pitch=50, start=4.25, end=4.5),  # G
])

for note in bass_notes:
    bass.notes.append(note)

# Piano continues with emotional comping
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue with kick on 1 and 3, snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
])

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax resolves motif with a slight variation
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
])

for note in sax_notes:
    sax.notes.append(note)

# Bass continues with melodic, chromatic line
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=85, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # G#
    pretty_midi.Note(velocity=85, pitch=53, start=5.25, end=5.5),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=85, pitch=50, start=5.75, end=6.0),  # G
])

for note in bass_notes:
    bass.notes.append(note)

# Piano resolves with emotional comping
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # D7
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums continue with kick on 1 and 3, snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("4_bar_intro.mid")
