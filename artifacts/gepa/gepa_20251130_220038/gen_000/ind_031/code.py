
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
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (1.5, 43),  # F
    (1.875, 44), # Gb
    (2.25, 45),  # G
    (2.625, 46), # Ab
    (2.875, 47), # A
    (3.25, 48),  # Bb
    (3.625, 49), # B
    (4.0, 50),   # C
    (4.375, 48), # Bb
    (4.75, 47),  # A
    (5.125, 46), # Ab
    (5.5, 45),   # G
    (5.875, 44), # Gb
    (6.25, 43)   # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: F7
piano_notes = [
    (1.5, 62),  # F
    (1.5, 66),  # A
    (1.5, 67),  # Bb
    (1.5, 71),  # D
    (1.875, 62),  # F
    (1.875, 66),  # A
    (1.875, 67),  # Bb
    (1.875, 71),  # D
    (2.25, 62),  # F
    (2.25, 66),  # A
    (2.25, 67),  # Bb
    (2.25, 71),  # D
    (2.625, 62),  # F
    (2.625, 66),  # A
    (2.625, 67),  # Bb
    (2.625, 71),  # D
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing
# F, G#, A, F (bar 2)
# F, G#, A, Bb (bar 3)
# F, G#, A, Bb (bar 4)
sax_notes = [
    (1.5, 62),  # F
    (1.625, 65), # G#
    (1.75, 66),  # A
    (1.875, 62), # F
    (2.25, 62),  # F
    (2.375, 65), # G#
    (2.5, 66),   # A
    (2.625, 67), # Bb
    (3.0, 62),   # F
    (3.125, 65), # G#
    (3.25, 66),  # A
    (3.375, 67), # Bb
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_introduction.mid')
