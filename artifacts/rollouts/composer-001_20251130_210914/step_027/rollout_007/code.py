
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

# Bass line: Walking in Dm
# Dm chord: D F A C
# Chromatic approach to each note
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F (chromatic approach from E)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # A (chromatic approach from G#)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # C (chromatic approach from B)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C (chromatic approach from B)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # A (chromatic approach from G#)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # F (chromatic approach from E)
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # D (chromatic approach from C#)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F (chromatic approach from E)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # A (chromatic approach from G#)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # C (chromatic approach from B)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # C
    # Bar 2, beat 4
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # C
    # Bar 3, beat 2
    pretty_midi.Note(velocity=95, pitch=60, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),  # C
    # Bar 3, beat 4
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, E, F, G, A, B, C, D
# Motif: D - F - A - C
# Play D on beat 1, then leave it hanging on beat 2
# Then play F and A on beat 3, and resolve to C on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # D (beat 1)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125),  # F (beat 3)
    pretty_midi.Note(velocity=110, pitch=64, start=2.8125, end=3.0),  # A (beat 3)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # C (beat 4)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dm_intro.mid")
