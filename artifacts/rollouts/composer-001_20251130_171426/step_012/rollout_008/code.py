
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

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 62),  # D4
    (1.875, 63), # Eb4
    (2.25, 64),  # E4
    (2.625, 65), # F4
    (3.0, 67),   # G4
    (3.375, 69), # A4
    (3.75, 70),  # Bb4
    (4.125, 71), # B4
    (4.5, 69),   # A4
    (4.875, 67), # G4
    (5.25, 65),  # F4
    (5.625, 64), # E4
    (6.0, 62)    # D4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 74),  # D7 (D, F#, A, C)
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 74),  # D7
    (2.25, 64), (2.25, 69), (2.25, 72), (2.25, 76),  # F#7 (F#, A, C#, E)
    (2.625, 64), (2.625, 69), (2.625, 72), (2.625, 76),  # F#7
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 77),  # A7 (A, C#, E, G)
    (3.375, 67), (3.375, 71), (3.375, 74), (3.375, 77),  # A7
    (3.75, 69), (3.75, 72), (3.75, 76), (3.75, 79),  # B7 (B, D#, F#, A)
    (4.125, 69), (4.125, 72), (4.125, 76), (4.125, 79),  # B7
    (4.5, 67), (4.5, 71), (4.5, 74), (4.5, 77),  # A7
    (4.875, 67), (4.875, 71), (4.875, 74), (4.875, 77),  # A7
    (5.25, 64), (5.25, 69), (5.25, 72), (5.25, 76),  # F#7
    (5.625, 64), (5.625, 69), (5.625, 72), (5.625, 76),  # F#7
    (6.0, 62), (6.0, 67), (6.0, 71), (6.0, 74)  # D7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.5, 67), (1.5, 69),  # D, E, F# (start)
    (1.875, 67), (1.875, 69), (1.875, 71),  # E, F#, G (continue)
    (2.25, 69), (2.25, 71), (2.25, 67),  # F#, G, E (turn)
    (2.625, 69), (2.625, 71), (2.625, 67),  # F#, G, E (repeat)
    (3.0, 65), (3.0, 67), (3.0, 69),  # D, E, F# (return)
    (3.375, 67), (3.375, 69), (3.375, 71),  # E, F#, G (end)
    (3.75, 69), (3.75, 71), (3.75, 67),  # F#, G, E (sway)
    (4.125, 69), (4.125, 71), (4.125, 67),  # F#, G, E (sway)
    (4.5, 65), (4.5, 67), (4.5, 69),  # D, E, F# (return)
    (4.875, 67), (4.875, 69), (4.875, 71),  # E, F#, G (end)
    (5.25, 69), (5.25, 71), (5.25, 67),  # F#, G, E (sway)
    (5.625, 69), (5.625, 71), (5.625, 67),  # F#, G, E (sway)
    (6.0, 65), (6.0, 67), (6.0, 69)  # D, E, F# (resolve)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

# Drums continue for full 6 seconds
for beat in range(4, 12):
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

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
