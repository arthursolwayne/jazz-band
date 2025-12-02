
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in C, chromatic approaches
bass_notes = [
    (1.5, 60),    # C4
    (1.875, 61),  # C#4
    (2.25, 62),   # D4
    (2.625, 60),  # C4
    (3.0, 62),    # D4
    (3.375, 63),  # D#4
    (3.75, 64),   # E4
    (4.125, 62),  # D4
    (4.5, 64),    # E4
    (4.875, 65),  # F4
    (5.25, 67),   # G4
    (5.625, 64),  # E4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 64, 67, 71),  # Cmaj7 (C, E, G, B)
    (1.875, 60, 64, 67, 71),  # Cmaj7
    (2.25, 60, 64, 67, 71),  # Cmaj7
    (2.625, 60, 64, 67, 71),  # Cmaj7
    (3.0, 62, 65, 69, 73),  # D7 (D, F#, A, C)
    (3.375, 62, 65, 69, 73),  # D7
    (3.75, 62, 65, 69, 73),  # D7
    (4.125, 62, 65, 69, 73),  # D7
    (4.5, 64, 67, 71, 74),  # E7 (E, G#, B, D)
    (4.875, 64, 67, 71, 74),  # E7
    (5.25, 64, 67, 71, 74),  # E7
    (5.625, 64, 67, 71, 74),  # E7
]
for time, root, third, fifth, seventh in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=root, start=time, end=time + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=third, start=time, end=time + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=fifth, start=time, end=time + 0.375)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=seventh, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Melody, one short motif, make it sing
sax_notes = [
    (1.5, 65),        # E5
    (1.875, 67),      # G5
    (2.25, 69),       # A5
    (2.625, 67),      # G5
    (3.0, 65),        # E5
    (3.375, 64),      # D5
    (3.75, 62),       # C5
    (4.125, 64),      # D5
    (4.5, 65),        # E5
    (4.875, 67),      # G5
    (5.25, 69),       # A5
    (5.625, 67),      # G5
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
