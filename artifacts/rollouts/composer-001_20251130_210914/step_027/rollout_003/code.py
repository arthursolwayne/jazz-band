
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (D7)
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # C
    # Bar 2, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=78, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=80, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=3.0),  # F#
    # Bar 3, beat 2 (C7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # B
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=4.125, end=4.5),  # D
    # Bar 4, beat 2 (B7)
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=83, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=86, start=4.875, end=5.25),  # G
    # Bar 4, beat 4 (D7)
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), E (64), B (60), D (62) — leave it hanging on B
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0625), # B
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.6875),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.6875, end=2.875), # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0625), # B
    pretty_midi.Note(velocity=110, pitch=62, start=3.0625, end=3.25),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare on 4
]
for i in range(4):
    for j in range(8):
        start = 1.5 + i*1.5 + j*0.1875
        if j % 2 == 0:
            pretty_midi.Note(velocity=80, pitch=42, start=start, end=start+0.1875)
# Bar 3
for i in range(4):
    for j in range(8):
        start = 3.0 + i*1.5 + j*0.1875
        if j % 2 == 0:
            pretty_midi.Note(velocity=80, pitch=42, start=start, end=start+0.1875)
# Bar 4
for i in range(4):
    for j in range(8):
        start = 4.5 + i*1.5 + j*0.1875
        if j % 2 == 0:
            pretty_midi.Note(velocity=80, pitch=42, start=start, end=start+0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
