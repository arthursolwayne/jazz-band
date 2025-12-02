
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bar_start = 1.5
for bar in range(2, 5):
    start = bar_start + (bar - 2) * 1.5
    # Dm7 walking bass line: D, F, G, Bb, C, Eb, F, Ab
    bass_notes = [
        pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=64, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=65, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=60, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=62, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=80, pitch=64, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=80, pitch=65, start=start + 2.25, end=start + 2.625),
        pretty_midi.Note(velocity=80, pitch=60, start=start + 2.625, end=start + 3.0)
    ]
    bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar_start + (bar - 2) * 1.5
    # Dm7 = D, F, A, C
    # Comp on 2 and 4
    for beat in [0.375, 1.125]:
        note1 = pretty_midi.Note(velocity=90, pitch=62, start=start + beat, end=start + beat + 0.375)
        note2 = pretty_midi.Note(velocity=90, pitch=64, start=start + beat, end=start + beat + 0.375)
        note3 = pretty_midi.Note(velocity=90, pitch=67, start=start + beat, end=start + beat + 0.375)
        note4 = pretty_midi.Note(velocity=90, pitch=69, start=start + beat, end=start + beat + 0.375)
        piano.notes.extend([note1, note2, note3, note4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar_start + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 - F7 - Bb7 - Dm7
# Start in Bar 2, first two beats
# D (62), F (64), B (67), D (62), G (65), Bb (62), C (67)
bar_start = 1.5
# First phrase: D, F, B, D
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start, end=bar_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 0.375, end=bar_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 0.75, end=bar_start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start + 1.125, end=bar_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Second phrase: G, Bb, C, D (half a bar later, at 3.0)
note5 = pretty_midi.Note(velocity=110, pitch=65, start=bar_start + 1.5, end=bar_start + 1.875)
note6 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start + 1.875, end=bar_start + 2.25)
note7 = pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 2.25, end=bar_start + 2.625)
note8 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start + 2.625, end=bar_start + 3.0)
sax.notes.extend([note5, note6, note7, note8])

# Third phrase: F, B, D (at 3.0)
note9 = pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 3.0, end=bar_start + 3.375)
note10 = pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 3.375, end=bar_start + 3.75)
note11 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start + 3.75, end=bar_start + 4.125)
note12 = pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 4.125, end=bar_start + 4.5)
note13 = pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 4.5, end=bar_start + 4.875)
note14 = pretty_midi.Note(velocity=110, pitch=62, start=bar_start + 4.875, end=bar_start + 5.25)
note15 = pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 5.25, end=bar_start + 5.625)
note16 = pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 5.625, end=bar_start + 6.0)
sax.notes.extend([note9, note10, note11, note12, note13, note14, note15, note16])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
