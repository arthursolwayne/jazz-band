
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on &
]

for note in drums_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody starts, bass walks, piano comps, drums continue

# Sax (Dante) - motif: Fm7 -> Bb -> D -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),   # F (1st beat)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),   # Bb (2nd beat)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # D (3rd beat)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),   # F (4th beat)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),   # F7 (root)
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),   # A (7th)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),   # Bb7 (root)
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),   # D (7th)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums continue (Bar 2)
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25),   # Snare on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),    # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),    # Hihat on &
]

for note in drums_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),   # Db
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),   # F7 (root)
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),   # A (7th)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),   # Bb7 (root)
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),   # D (7th)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums continue (Bar 3)
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),   # Snare on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.75),    # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),    # Hihat on &
]

for note in drums_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves with a rest, then returns with a hint of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # F (4th beat)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),   # F7 (root)
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),   # A (7th)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums continue (Bar 4)
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.75),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),    # Hihat on 2
]

for note in drums_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
