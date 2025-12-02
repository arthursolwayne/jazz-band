
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 70),  # F3
    (1.875, 69),  # E3
    (2.25, 71),  # G3
    (2.625, 72),  # G#3
    # Bar 3
    (3.0, 72),  # G3
    (3.375, 71),  # G#3
    (3.75, 69),  # E3
    (4.125, 68),  # D3
    # Bar 4
    (4.5, 68),  # D3
    (4.875, 69),  # E3
    (5.25, 71),  # G3
    (5.625, 72),  # G#3
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (1.875, 72),  # F7 - F, A, C, E
    (1.875, 77),  # A
    (1.875, 79),  # C
    (1.875, 82),  # E
    # Bar 3
    (3.375, 72),  # F7
    (3.375, 77),
    (3.375, 79),
    (3.375, 82),
    # Bar 4
    (4.875, 72),  # F7
    (4.875, 77),
    (4.875, 79),
    (4.875, 82),
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F6 (F in the upper register), then a chromatic walk up to G6, then back to F6
sax_notes = [
    # Bar 2, measure 1
    (1.5, 87),  # F6
    (1.75, 88),  # F#6
    (2.0, 89),  # G6
    # Bar 3, measure 1
    (3.0, 89),  # G6
    (3.25, 88),  # F#6
    (3.5, 87),  # F6
    # Bar 4, measure 1
    (4.5, 87),  # F6
    (4.75, 88),  # F#6
    (5.0, 89),  # G6
    (5.25, 87),  # F6
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
