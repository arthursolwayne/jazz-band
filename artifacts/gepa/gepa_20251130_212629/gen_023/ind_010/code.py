
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody, bass line, piano comp, drums continue
# Sax: F, C, Bb, G (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # Db
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=60, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=60, pitch=42, start=2.8125, end=3.0),
])

# Bar 4: Keep the tension. Sax holds the last note, then lifts
# Sax: Bb, G (holding)
sax_notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),
])

# Bass: Continue walking line
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75),  # A
])

# Piano: 7th chord on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # Db
])

# Drums: continue
drum_notes.extend([
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.3125, end=4.5),
])

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("jazz_intro.mid")
