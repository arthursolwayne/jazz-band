
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: Short motif, start it, leave it hanging, come back and finish it
# Dm = D, F, A, C

# Bar 2 (1.5 - 3.0s)
# Sax motif: D (beat 1), F (beat 2), A (beat 3), leave it on beat 4
note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note_2 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)
note_3 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
sax.notes.extend([note_1, note_2, note_3])

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking bass line in Dm, chromatic approaches
# Dm root motion: D, C, Bb, A, G, F, E, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D, F, A, C
# Bar 2 (1.5 - 3.0s): comp on beat 2
chord_2 = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625)
chord_2_2 = pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625)
chord_2_3 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625)
chord_2_4 = pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625)
piano.notes.extend([chord_2, chord_2_2, chord_2_3, chord_2_4])

# Bar 3 (3.0 - 4.5s): comp on beat 4
chord_3 = pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5)
chord_3_2 = pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5)
chord_3_3 = pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5)
chord_3_4 = pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5)
piano.notes.extend([chord_3, chord_3_2, chord_3_3, chord_3_4])

# Bar 4 (4.5 - 6.0s): complete the sax motif
note_4 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note_5 = pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625)
note_6 = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)
sax.notes.extend([note_4, note_5, note_6])

# Drums: Bar 2 (1.5 - 3.0s) and Bar 3 (3.0 - 4.5s)
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
