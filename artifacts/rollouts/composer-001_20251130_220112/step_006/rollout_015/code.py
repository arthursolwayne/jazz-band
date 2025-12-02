
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
# Sax motif: D (D4), F# (F#4), A (A4), B (B4) - short, singable, leaves it hanging

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # G3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, resolve on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # D3
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # G3
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif, resolve on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # G3
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
