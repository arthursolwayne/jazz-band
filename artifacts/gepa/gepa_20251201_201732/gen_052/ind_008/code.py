
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

# Drums Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass Bar 2: Walking line, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # D2 (F7 root)
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # E2 (F7 5th)
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # D2 (F7 root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano Bar 2: Open voicing, Cm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax Bar 2: Melody, haunting and incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # E4 (start of motif)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # A4 (half a bar later)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass Bar 3: Walking line, chromatic approach to Gm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G2 (Gm7 root)
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # A2 (Gm7 5th)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G2 (Gm7 root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano Bar 3: Open voicing, Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax Bar 3: Melody, continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # A4 (continuing motif)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass Bar 4: Walking line, chromatic approach to Cm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # D2 (Cm7 root)
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # E2 (Cm7 5th)
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),  # D2 (Cm7 root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano Bar 4: Open voicing, Cm7 with resolution
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax Bar 4: Melody, resolution to C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=5.25),  # C4 (resolution)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
