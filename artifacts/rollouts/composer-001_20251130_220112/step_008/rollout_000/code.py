
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (1.5, 55), (1.75, 57), (2.0, 59), (2.25, 60),
    (2.5, 62), (2.75, 63), (3.0, 64), (3.25, 62),
    (3.5, 60), (3.75, 58), (4.0, 57), (4.25, 55),
    (4.5, 53), (4.75, 52), (5.0, 50), (5.25, 48)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (2.0, 62), (2.0, 67), (2.0, 71), (2.0, 74), # D7
    (3.0, 64), (3.0, 69), (3.0, 73), (3.0, 76), # F7
    (4.0, 67), (4.0, 72), (4.0, 76), (4.0, 79), # A7
    (5.0, 69), (5.0, 74), (5.0, 78), (5.0, 81)  # C7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick_times = [start, start + 0.75]
    snare_times = [start + 0.375, start + 1.125]
    hihat_times = [start + i * 0.375 for i in range(4)]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))

# Saxophone (Dante) - short motif, start it, leave it hanging, return and finish
# Motif: F (65) -> Bb (62) -> D (67) -> F (65)
sax_notes = [
    (1.5, 65), (1.75, 62), (2.0, 67), (2.25, 65),
    (3.5, 65), (3.75, 62), (4.0, 67), (4.25, 65),
    (5.0, 65), (5.25, 62), (5.5, 67), (5.75, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
