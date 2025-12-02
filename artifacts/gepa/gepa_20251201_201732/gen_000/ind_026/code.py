
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
# Bass: walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=90, pitch=58, start=2.625, end=3.0),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bm7 (B, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve on the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # C3
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif, sing it out
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0),  # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hi-hat on every eighth
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

midi.write("dante_intro.mid")
