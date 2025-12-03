
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    # Bar 2: Fm -> Bb -> Ab -> D
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # D2
    # Bar 3: Eb -> C -> Gb -> Bb
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Gb2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # Bb2
    # Bar 4: F -> Ab -> C -> Eb
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # C2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Ab3
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=70, pitch=60, start=1.5, end=1.875),  # D4
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.375),  # G5
    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # C5
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    kick_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)
# Snare on 2 and 4
for bar in [2, 3, 4]:
    snare_start = (bar - 1) * 1.5 + 0.75
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 1.5, end=snare_start + 1.625)
# Hi-hat on every eighth
for bar in [2, 3, 4]:
    for i in range(4):
        start = (bar - 1) * 1.5 + i * 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
