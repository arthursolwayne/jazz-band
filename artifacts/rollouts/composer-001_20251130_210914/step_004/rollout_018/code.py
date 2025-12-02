
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
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (1.5, 60),  # F3
    (1.875, 61), # G3
    (2.25, 59),  # E3
    (2.625, 58), # D3
    (3.0, 60),   # F3
    (3.375, 61), # G3
    (3.75, 59),  # E3
    (4.125, 62), # A3
    (4.5, 60),   # F3
    (4.875, 61), # G3
    (5.25, 59),  # E3
    (5.625, 58)  # D3
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (2.25, 64), (67, 0.1), (69, 0.1), (71, 0.1),  # Dm7 at 2.25
    (3.75, 64), (67, 0.1), (69, 0.1), (71, 0.1),  # Dm7 at 3.75
    (5.25, 64), (67, 0.1), (69, 0.1), (71, 0.1)   # Dm7 at 5.25
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Sax (Dante) - motif
sax_notes = [
    (1.5, 64), (1.5 + 0.375, 66), (1.5 + 0.75, 65),  # F, G, F#
    (1.5 + 1.125, 64), (1.5 + 1.5, 66), (1.5 + 1.875, 65),  # F, G, F#
    (1.5 + 2.25, 64)  # F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
