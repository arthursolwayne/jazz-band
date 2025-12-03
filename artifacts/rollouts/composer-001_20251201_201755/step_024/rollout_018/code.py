
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2, MIDI 53 - 57)
bass_notes = [
    # Bar 2: F2, Ab2, Bb2, D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2
    # Bar 3: Eb2, F2, Gb2, A2
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125), # Gb2
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # A2
    # Bar 4: Bb2, C2, D2, F2
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.5),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes[0:12] + drum_notes[12:24] + drum_notes[24:36])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm - F, Ab, C, Eb
# Motif: F (Ab), C (Eb) - then repeat with a twist
sax_notes = [
    # Bar 2: F (Ab), C (Eb)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # Eb
    # Bar 3: F (Ab), C (Bb) - twist
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb
    # Bar 4: F (Ab), C (Eb) - resolution
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
