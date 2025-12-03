
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (F2, C3, G3, D3, F3, C3, G3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=81, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=2.25, end=2.625), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=2.625, end=3.0),  # D3
    pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=80, pitch=81, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=3.75, end=4.125), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=4.125, end=4.5),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif (F, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=3.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2, C3, G3, D3, F3, C3, G3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=81, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=3.75, end=4.125), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=4.125, end=4.5),  # D3
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=5.625, end=6.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 3: F7 (F, A, C, E flat)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=4.5),  # E flat
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif (F, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=77, start=4.125, end=4.5),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2, C3, G3, D3, F3, C3, G3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=5.625, end=6.0),  # D3
    pretty_midi.Note(velocity=80, pitch=78, start=6.0, end=6.375),  # F3
    pretty_midi.Note(velocity=80, pitch=81, start=6.375, end=6.75), # C3
    pretty_midi.Note(velocity=80, pitch=84, start=6.75, end=7.125), # G3
    pretty_midi.Note(velocity=80, pitch=87, start=7.125, end=7.5),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif (F, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=77, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick=36, snare=38, hihat=42

# Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
