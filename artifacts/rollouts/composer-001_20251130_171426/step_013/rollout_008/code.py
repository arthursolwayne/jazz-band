
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line with chromatic approaches
bass_notes = [
    (1.5, 37),   # D (F7 chord root)
    (1.875, 36), # C# (chromatic approach)
    (2.25, 38),  # E (F7 chord)
    (2.625, 40), # G (F7 chord)
    (2.625, 39), # F# (chromatic approach)
    (3.0, 41),   # A (F7 chord)
    (3.375, 43), # C (F7 chord)
    (3.75, 42),  # Bb (chromatic approach)
    (3.75, 40),  # G (F7 chord)
    (4.125, 38), # E (F7 chord)
    (4.5, 37),   # D (F7 chord)
    (4.875, 36), # C# (chromatic approach)
    (5.25, 38),  # E (F7 chord)
    (5.625, 40), # G (F7 chord)
    (5.625, 39), # F# (chromatic approach)
    (6.0, 37)    # D (F7 chord)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 76),  # F7 chord
    (2.25, 62), (2.25, 67), (2.25, 71), (2.25, 76),  # F7 chord
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76),  # F7 chord
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 76),  # F7 chord
    (4.5, 62), (4.5, 67), (4.5, 71), (4.5, 76),  # F7 chord
    (5.25, 62), (5.25, 67), (5.25, 71), (5.25, 76)  # F7 chord
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    start_time = 1.5 + bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Sax - Dante: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F Ab Bb F (1.5s) then rest, then repeat and resolve
sax_notes = [
    (1.5, 66),  # F (tenor sax)
    (1.625, 69), # Ab
    (1.75, 67),  # Bb
    (2.0, 66),  # F
    (2.75, 66),  # F again
    (2.875, 69), # Ab
    (3.0, 67),   # Bb
    (3.25, 66),  # F
    (3.75, 66),  # F
    (3.875, 69), # Ab
    (4.0, 67),   # Bb
    (4.25, 66),  # F
    (4.75, 66),  # F
    (4.875, 69), # Ab
    (5.0, 67),   # Bb
    (5.25, 66)   # F
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
