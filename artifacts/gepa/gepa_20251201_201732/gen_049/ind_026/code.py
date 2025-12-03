
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
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
# Roots and fifths with chromatic approaches
# Bar 2: F -> Ab -> D -> Eb
# Bar 3: Eb -> Gb -> C -> D
# Bar 4: D -> F -> Bb -> C
bass_notes = [
    (1.5, 53, 100), (1.75, 55, 100), (2.0, 57, 100), (2.25, 52, 100),
    (2.5, 52, 100), (2.75, 54, 100), (3.0, 57, 100), (3.25, 55, 100),
    (3.5, 55, 100), (3.75, 53, 100), (4.0, 50, 100), (4.25, 53, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Eb7 (Eb, Gb, Bb, D)
# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2
    (1.5, 53, 100), (1.5, 55, 100), (1.5, 60, 100), (1.5, 62, 100),
    # Bar 3
    (2.5, 50, 100), (2.5, 52, 100), (2.5, 55, 100), (2.5, 62, 100),
    # Bar 4
    (3.5, 55, 100), (3.5, 57, 100), (3.5, 62, 100), (3.5, 64, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    for beat in range(4):
        time = bar_start + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - D - F
# Play on beats 1 and 3 of bar 2, leave the rest open
sax_notes = [
    (1.5, 53, 110), (1.75, 55, 110), (2.0, 57, 110), (2.25, 53, 110),
    (3.0, 53, 110), (3.25, 55, 110), (3.5, 57, 110), (3.75, 53, 110)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
