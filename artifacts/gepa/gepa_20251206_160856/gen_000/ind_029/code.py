
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
# Bar 2: F (F2), G (G2), E (E2), A (A2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # E2
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),  # A2
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875), # E
]
# Bar 3: Bm7b5 (B, D, F, A)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=85, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=88, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.625), # A
]
# Bar 4: E7 (E, G#, B, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=91, start=3.0, end=3.375), # G#
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375), # D
]
# Bar 4 resolution: Am7 (A, C, E, G)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875), # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on all eighths
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + (i + 1) * 0.375)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, A, Bb, Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=85, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=85, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=85, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
