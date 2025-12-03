
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # C3 (fifth of Fm)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Short motif that sings, start it, leave it hanging, come back and finish it
# Motif: F - Ab - C - F (melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=53, start=2.5, end=2.75),  # F (leaving it hanging)
    pretty_midi.Note(velocity=110, pitch=51, start=2.75, end=3.0),  # Ab (continuation)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # C3 (fifth of Fm)
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Ab (MIDI 51)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=4.5),  # Gb
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, build tension
# Motif: F - Ab - C - F (continuation)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=53, start=4.0, end=4.25),  # F (leaving it hanging)
    pretty_midi.Note(velocity=110, pitch=51, start=4.25, end=4.5),  # Ab (continuation)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # C3 (fifth of Fm)
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # C (MIDI 55)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve
# Motif: F - Ab - C - F (resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=5.75, end=6.0),  # F (resolution)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and Bar 4
for bar in [3.0, 4.5]:
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=90, pitch=36, start=bar + 0.0, end=bar + 0.375),
        pretty_midi.Note(velocity=90, pitch=36, start=bar + 1.125, end=bar + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0),
        # Hi-hats on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.0, end=bar + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.1875, end=bar + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.375, end=bar + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.5625, end=bar + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.75, end=bar + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.9375, end=bar + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.125, end=bar + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.3125, end=bar + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
