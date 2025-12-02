
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2 (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) to Bb2 (MIDI 45), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # C2 (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75),  # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Bb2 (MIDI 45) to D2 (MIDI 38), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # B2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # Eb2 (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.25),  # Bb4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
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
