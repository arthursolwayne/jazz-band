
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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
# Sax: Motif - D (D4), F# (F#4), A (A4), B (B4), D (D5) - start on beat 1, end on beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line starting on D (D2), chromatic approach to F# (F#2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s) - D7 on beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=72, start=1.875, end=2.25),
    # Bar 3 (2.5 - 3.0s) - F#7 on beat 4
    pretty_midi.Note(velocity=85, pitch=66, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=73, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=76, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
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

# Bar 4: Bass, Piano, Sax (4.5 - 6.0s)
# Sax: Rest and then return to motif, but start on beat 3
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line starting on D (D2), chromatic approach to F# (F#2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=55, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=53, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=51, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=50, start=7.125, end=7.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s) - D7 on beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=72, start=4.875, end=5.25),
    # Bar 4 (5.5 - 6.0s) - F#7 on beat 4
    pretty_midi.Note(velocity=85, pitch=66, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=73, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=76, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
