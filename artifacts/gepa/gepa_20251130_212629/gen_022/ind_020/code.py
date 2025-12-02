
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # hihat on 1 (next bar)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with motif
# Fm: F, Ab, Bb, Db
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),   # Eb (Ab in Fm)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # F (Bb in Fm)
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.5),   # Eb (Db in Fm)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Bass enters with walking line
# Fm: F, Ab, Bb, Db
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Eb (Ab)
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # F (Bb)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # Eb (Db)
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano enters with comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),    # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax continues with motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Bass continues with walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Piano continues with comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),   # F7
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),    # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # hihat on 1 (next bar)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Sax ends with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # Eb (last note left hanging)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass ends with walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),   # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Piano ends with comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.75),   # F7
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.5),    # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums end
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # hihat on 1
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
