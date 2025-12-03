
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
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.125),
    # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=57, start=2.125, end=2.5),
    # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=56, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (Fm harmony)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Bb2 (root)
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),
    # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.625),
    # D2 (fifth)
    pretty_midi.Note(velocity=90, pitch=50, start=3.625, end=4.0),
    # C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=51, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbm7 (Bb, Db, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Bb - Db - Eb - Bb (Bbm harmony)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=68, start=4.0, end=4.25),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Eb2 (root)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.125),
    # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=52, start=5.125, end=5.5),
    # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Ebm7 (Eb, Gb, Bb, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Eb - Gb - Ab - Eb (Ebm harmony)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=59, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=110, pitch=61, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=5.5, end=5.75),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
for i in range(2):
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5 + 1.125, end=1.5 + i*1.5 + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 1.875, end=1.5 + i*1.5 + 2.0),
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 0.1875, end=1.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 0.375, end=1.5 + i*1.5 + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 0.5625, end=1.5 + i*1.5 + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 0.9375, end=1.5 + i*1.5 + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 1.125, end=1.5 + i*1.5 + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*1.5 + 1.3125, end=1.5 + i*1.5 + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
