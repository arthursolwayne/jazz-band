
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),    # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),    # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),    # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),    # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),    # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),    # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),    # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),    # F
    # Bar 3: Rest
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),    # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),    # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),    # F
    # Bar 4: D7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),    # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),    # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),    # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), B (69), D (62) — start on 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),    # D
    # Repeat the motif, an octave lower
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),    # D (octave lower)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625),   # B
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),    # D
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar.mid")
