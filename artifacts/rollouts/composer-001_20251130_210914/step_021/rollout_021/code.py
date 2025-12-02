
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
# F minor walking bass line: F, Gb, G, Ab, A, Bb, B, C, C#, D, Eb, E, F#, G, G#, A, Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=75, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=73, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab
piano_notes = [
    # Bar 2 - F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # Eb
    # Bar 3 - Bb7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=78, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=78, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 motif: F, Ab, Bb, C, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.1875),  # C
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.1875),  # F (return)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start+0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start+1.125, end=bar_start+1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start+0.75, end=bar_start+0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start+1.875, end=bar_start+2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start+0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+0.1875, end=bar_start+0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+0.375, end=bar_start+0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+0.5625, end=bar_start+0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+0.75, end=bar_start+0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+0.9375, end=bar_start+1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+1.125, end=bar_start+1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start+1.3125, end=bar_start+1.5),
    drums.notes.extend([

    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
