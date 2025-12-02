
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 48), # F
    (1.875, 49), # Gb
    (2.25, 50), # G
    (2.625, 51), # Ab
    # Bar 3
    (3.0, 52), # A
    (3.375, 53), # Bb
    (3.75, 54), # B
    (4.125, 55), # C
    # Bar 4
    (4.5, 56), # C#
    (4.875, 57), # D
    (5.25, 58), # D#
    (5.625, 59), # E
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 60), (1.5, 64), # F7 (F, Bb, C, E)
    (1.875, 60), (1.875, 64),
    # Bar 3
    (3.0, 60), (3.0, 64),
    (3.375, 60), (3.375, 64),
    # Bar 4
    (4.5, 60), (4.5, 64),
    (4.875, 60), (4.875, 64),
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (1.5, 63), # A
    (1.625, 65), # Bb
    (1.75, 63), # A
    # Bar 3
    (3.0, 63), # A
    (3.125, 65), # Bb
    (3.25, 63), # A
    (3.375, 64), # B
    (3.5, 63), # A
    # Bar 4
    (4.5, 63), # A
    (4.625, 65), # Bb
    (4.75, 63), # A
    (4.875, 64), # B
    (5.0, 63), # A
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
