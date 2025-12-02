
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
        hihat_time = time + 0.1875
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 65),  # D
    (1.875, 66), # Eb
    (2.25, 67),  # E
    (2.625, 69), # G
    (2.875, 70), # G#
    (3.25, 71),  # A
    (3.625, 72), # A#
    (4.0, 74),   # C
    (4.375, 75), # C#
    (4.75, 76),  # D
    (5.125, 77), # D#
    (5.5, 79),   # F
    (5.875, 80), # F#
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67),  # E7 (E, G#, B, D)
    (1.875, 72), # C7 (C, E, G, B)
    (2.25, 67),  # E7
    (2.625, 72), # C7
    (3.0, 71),   # B7 (B, D#, F#, A)
    (3.375, 72), # C7
    (3.75, 71),  # B7
    (4.125, 72), # C7
    (4.5, 67),   # E7
    (4.875, 72), # C7
    (5.25, 71),  # B7
    (5.625, 72), # C7
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (65), F# (67), A (69), D (65)
sax_notes = [
    (1.5, 65),  # D
    (1.625, 67), # F#
    (1.75, 69),  # A
    (1.875, 65), # D
    (2.25, 65),  # D
    (2.375, 67), # F#
    (2.5, 69),   # A
    (2.625, 65), # D
    (3.0, 65),   # D
    (3.125, 67), # F#
    (3.25, 69),  # A
    (3.375, 65), # D
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
