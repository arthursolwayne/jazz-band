
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
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 48),  # F
    (1.875, 47),  # Eb
    (2.25, 50),  # G
    (2.625, 48),  # F
    # Bar 3
    (2.875, 49),  # Ab
    (3.25, 50),  # G
    (3.625, 48),  # F
    (4.0, 47),  # Eb
    # Bar 4
    (4.375, 50),  # G
    (4.75, 48),  # F
    (5.125, 47),  # Eb
    (5.5, 50)    # G
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp on Bars 2, 3, 4
piano_notes = []
# Bar 2
piano_notes.extend([
    (1.5, 64), (1.5, 69), (1.5, 71), (1.5, 76),  # F7
    (1.875, 64), (1.875, 69), (1.875, 71), (1.875, 76),
    (2.25, 64), (2.25, 69), (2.25, 71), (2.25, 76),
    (2.625, 64), (2.625, 69), (2.625, 71), (2.625, 76)
])
# Bar 3
piano_notes.extend([
    (2.875, 64), (2.875, 67), (2.875, 69), (2.875, 74),  # Ab7
    (3.25, 64), (3.25, 67), (3.25, 69), (3.25, 74),
    (3.625, 64), (3.625, 67), (3.625, 69), (3.625, 74),
    (4.0, 64), (4.0, 67), (4.0, 69), (4.0, 74)
])
# Bar 4
piano_notes.extend([
    (4.375, 64), (4.375, 69), (4.375, 71), (4.375, 76),  # F7
    (4.75, 64), (4.75, 69), (4.75, 71), (4.75, 76),
    (5.125, 64), (5.125, 69), (5.125, 71), (5.125, 76),
    (5.5, 64), (5.5, 69), (5.5, 71), (5.5, 76)
])
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax - Motif: F, Ab, Bb, G, leave it hanging on Bb
sax_notes = [
    (1.5, 84),  # F
    (1.875, 87),  # Ab
    (2.25, 86),  # Bb
    (2.625, 84),  # G
    (3.0, 86),    # Bb
    (3.375, 86),  # Bb
    (3.75, 86),   # Bb
    (4.125, 86),  # Bb
    (4.5, 84),    # F
    (4.875, 87),  # Ab
    (5.25, 86),   # Bb
    (5.625, 84)   # G
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums for Bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
