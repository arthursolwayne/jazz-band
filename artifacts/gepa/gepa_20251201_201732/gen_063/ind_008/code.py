
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (F2 - Bb2 - Bb2 - Ab2 - Ab2 - G2 - G2 - F2)
bass_notes = [
    (1.5, 38),  # F2
    (1.875, 43),  # Bb2
    (2.25, 43),  # Bb2
    (2.625, 41),  # Ab2
    (2.625, 41),  # Ab2
    (3.0, 38),  # G2
    (3.375, 38),  # G2
    (3.75, 38),  # F2
    (3.75, 38),  # F2
    (4.125, 43),  # Bb2
    (4.5, 43),  # Bb2
    (4.875, 41),  # Ab2
    (4.875, 41),  # Ab2
    (5.25, 38),  # G2
    (5.625, 38),  # G2
    (6.0, 38)  # F2
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 53), (1.5, 60), (1.5, 64), (1.5, 62),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.25, 58), (2.25, 62), (2.25, 64), (2.25, 60),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.0, 60), (3.0, 63), (3.0, 67), (3.0, 65),
    # Resolutions
    (4.125, 60), (4.125, 64), (4.125, 67), (4.125, 65)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motive: F, Ab, G, F
sax_notes = [
    (1.5, 65), (1.5, 68), (1.5, 67), (1.5, 65),  # F, Ab, G, F
    (2.25, 65), (2.25, 68), (2.25, 67), (2.25, 65),  # F, Ab, G, F
    (3.0, 65), (3.0, 68), (3.0, 67), (3.0, 65)    # F, Ab, G, F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
