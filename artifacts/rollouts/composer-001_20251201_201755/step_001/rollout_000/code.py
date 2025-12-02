
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
    # Hi-Hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
]

# Bar 3: Bb7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # F5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # A5
])

# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # Bb5
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 -> F4 -> Eb4 -> D4 (D F Eb D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4 (resolve)
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_moment.mid")
