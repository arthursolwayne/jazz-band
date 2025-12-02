
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line, chromatic approaches, no repeated notes
# Dmin7 (D F A C) - Dm7 in D
# Walking bass line: D - Eb - F - G (chromatic approach to F)
# Then C - B - A - G (chromatic approach to A)
# Then D - Eb - F - G (loop)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
# Dmin7 (D F A C)
# Bar 2: Dmin7 on 2 and 4
# Bar 3: Dmin7 on 2 and 4
# Bar 4: Dmin7 on 2 and 4
# Chords on beats 2 and 4 (0.375s and 1.125s after bar start)
# Each chord = 0.375s duration
for bar in range(2, 5):
    start = bar * 1.5
    # Dmin7 on beat 2
    d = pretty_midi.Note(velocity=90, pitch=62, start=start + 0.375, end=start + 0.75)
    f = pretty_midi.Note(velocity=90, pitch=64, start=start + 0.375, end=start + 0.75)
    a = pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75)
    c = pretty_midi.Note(velocity=90, pitch=60, start=start + 0.375, end=start + 0.75)
    # Dmin7 on beat 4
    d2 = pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5)
    f2 = pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5)
    a2 = pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5)
    c2 = pretty_midi.Note(velocity=90, pitch=60, start=start + 1.125, end=start + 1.5)
    piano.notes.extend([d, f, a, c, d2, f2, a2, c2])

# Drums: same pattern for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Sax - Dante: Motif
# D (62), F (64), G (65), Bb (66) — one short motif, make it sing
# Start on bar 2, play the motif on 1 and 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=6.0, end=6.375),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=6.75, end=7.125),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
