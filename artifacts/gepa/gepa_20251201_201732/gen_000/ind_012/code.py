
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625), # A (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # Bb (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on last beat
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=3.0),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
