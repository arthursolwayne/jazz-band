
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (D4) at start, then G (G4) at 0.75s, then B (B4) at 1.125s, then D (D4) at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C4
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # B3
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),  # A3
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2, beat 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # C5
    # Bar 2, beat 4: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # F#4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif with a slight variation, ending on G (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # B3
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # A3
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3, beat 2: A7 (A, C#, E, G)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # C#5
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # E5
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # G4
    # Bar 3, beat 4: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.875),  # D#5
    pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.875),  # F#5
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif with variation, ending on B (B4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C4
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # B3
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),  # A3
    pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375),  # G4
    pretty_midi.Note(velocity=80, pitch=65, start=6.375, end=6.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=64, start=6.75, end=7.125),  # E4
    pretty_midi.Note(velocity=80, pitch=62, start=7.125, end=7.5),  # D4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4, beat 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # C5
    # Bar 4, beat 4: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.375),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=6.0, end=6.375),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375),  # F#4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
