
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=1.875 + 0.375),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.25 + 0.375),  # G2
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=2.625 + 0.375),  # E2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=2.625 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625 + 0.375 * 2, end=2.625 + 0.375 * 3),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625 + 0.375 * 4, end=2.625 + 0.375 * 5),  # G2
    pretty_midi.Note(velocity=80, pitch=40, start=2.625 + 0.375 * 6, end=2.625 + 0.375 * 7),  # E2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=2.625 + 0.375 * 6, end=2.625 + 0.375 * 7),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625 + 0.375 * 8, end=2.625 + 0.375 * 9),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625 + 0.375 * 10, end=2.625 + 0.375 * 11),  # G2
    pretty_midi.Note(velocity=80, pitch=40, start=2.625 + 0.375 * 12, end=2.625 + 0.375 * 13),  # E2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375))

# Bar 3: Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=1.875 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.375))

# Bar 4: Am7 (A, C, E, G)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D - Eb - F - G (on 1, 2, 3, 4 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.25 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.625 + 0.375),
    # Leave it hanging, then come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.75 + 0.375),
    pretty_midi.Note(velocity=110, pitch=63, start=4.125, end=4.125 + 0.375),
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=4.875 + 0.375)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
