
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
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass): walking line, chromatic approaches, never the same note twice
# Dm7 -> G7 -> Cm7 -> F7 -> Dm7
bass_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0), # F
    # Bar 3: G7
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5), # Bb
    # Bar 4: Cm7
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625), # Db
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0), # Eb
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords, comp on 2 and 4
# Dm7 -> G7 -> Cm7 -> F7
# Dm7: D, F, A, C
# G7: G, Bb, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 - comp on 2 and 4
        chord = [62, 64, 67, 69]  # D, F, A, C
    elif bar == 3:
        # G7
        chord = [67, 70, 72, 74]  # G, Bb, D, F
    elif bar == 4:
        # Cm7
        chord = [60, 64, 67, 70]  # C, Eb, G, Bb
    # Comp on 2 and 4
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 0.375, end=start + 0.75))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 1.125, end=start + 1.5))

# Little Ray (drums): same as bar 1, but now with full rhythm
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Dante (sax): one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 -> G7 -> Cm7 -> F7
# D, Bb, C#, F -> G, Bb, D, F -> C, Eb, G, Bb -> F, A, C, Eb
# Use Dm scale: D, Eb, F, G, A, Bb, C
# D (62), Eb (64), F (65), G (67), A (69), Bb (70), C (72)
# Motif: D, Bb, F, G
# Start on D, leave it hanging on Bb, come back with F and G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
