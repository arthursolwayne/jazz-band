
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),  # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm9 (D F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # Eb4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Eb4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # Bb2
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5),   # Eb3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),   # G4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),   # Bb4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5),   # D5
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=4.5),   # F5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # Eb4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.875),  # Eb3
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # E3
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # A3
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # C4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),   # C5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),   # E5
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=6.0),   # G5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0),   # Bb5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # Eb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
