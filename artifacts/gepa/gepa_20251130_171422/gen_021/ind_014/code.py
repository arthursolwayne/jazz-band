
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
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Sax enters with a motif in Dm
bar_start = 1.5
# Sax motif: Dm7 -> Bb -> C -> D (Dm7 arpeggio with a chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.5),
    pretty_midi.Note(velocity=100, pitch=59, start=bar_start + 0.5, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=60, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 1.125, end=bar_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=50, start=bar_start, end=bar_start + 0.375),    # D
    pretty_midi.Note(velocity=70, pitch=49, start=bar_start + 0.375, end=bar_start + 0.75),  # C
    pretty_midi.Note(velocity=70, pitch=51, start=bar_start + 0.75, end=bar_start + 1.125),  # Eb
    pretty_midi.Note(velocity=70, pitch=52, start=bar_start + 1.125, end=bar_start + 1.5),   # F
    pretty_midi.Note(velocity=70, pitch=50, start=bar_start + 1.5, end=bar_start + 1.875),   # D
    pretty_midi.Note(velocity=70, pitch=49, start=bar_start + 1.875, end=bar_start + 2.25),  # C
    pretty_midi.Note(velocity=70, pitch=51, start=bar_start + 2.25, end=bar_start + 2.625),  # Eb
    pretty_midi.Note(velocity=70, pitch=52, start=bar_start + 2.625, end=bar_start + 3.0),   # F
    pretty_midi.Note(velocity=70, pitch=50, start=bar_start + 3.0, end=bar_start + 3.375),   # D
    pretty_midi.Note(velocity=70, pitch=49, start=bar_start + 3.375, end=bar_start + 3.75),  # C
    pretty_midi.Note(velocity=70, pitch=51, start=bar_start + 3.75, end=bar_start + 4.125),  # Eb
    pretty_midi.Note(velocity=70, pitch=52, start=bar_start + 4.125, end=bar_start + 4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=bar_start + 0.75, end=bar_start + 1.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 0.75, end=bar_start + 1.125),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=bar_start + 0.75, end=bar_start + 1.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=bar_start + 0.75, end=bar_start + 1.125),  # C
    # Bar 3: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=bar_start + 2.25, end=bar_start + 2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 2.25, end=bar_start + 2.625),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=bar_start + 2.25, end=bar_start + 2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=bar_start + 2.25, end=bar_start + 2.625),  # C
    # Bar 4: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=bar_start + 3.75, end=bar_start + 4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 3.75, end=bar_start + 4.125),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=bar_start + 3.75, end=bar_start + 4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=bar_start + 3.75, end=bar_start + 4.125),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue with same pattern
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
