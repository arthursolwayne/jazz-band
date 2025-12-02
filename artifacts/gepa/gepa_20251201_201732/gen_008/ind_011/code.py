
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

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875), # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Dm, short and singable
# Start on D, bend to Eb, resolve to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875), # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation, resolve to Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375), # Bb4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution, end on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875), # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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

midi.write('dante_intro.mid')
