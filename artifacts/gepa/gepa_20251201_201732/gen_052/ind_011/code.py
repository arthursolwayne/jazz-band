
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
    (0.0, 36, 110), (0.375, 42, 100), (0.75, 38, 110), (1.125, 42, 100),
    (1.5, 36, 110), (1.875, 42, 100), (2.25, 38, 110), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 70, 70), (1.875, 72, 70), (2.25, 70, 70), (2.625, 72, 70),
    (3.0, 74, 70), (3.375, 72, 70), (3.75, 74, 70), (4.125, 72, 70),
    (4.5, 76, 70), (4.875, 74, 70), (5.25, 76, 70), (5.625, 74, 70)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 77, 100), (1.5, 82, 100), (1.5, 72, 100), (1.5, 76, 100),  # Fmaj7
    # Bar 3: Bbmaj7 (Bb, D, F, A)
    (3.0, 70, 100), (3.0, 75, 100), (3.0, 72, 100), (3.0, 77, 100),  # Bbmaj7
    # Bar 4: D7 (D, F#, A, C)
    (4.5, 74, 100), (4.5, 78, 100), (4.5, 77, 100), (4.5, 72, 100)   # D7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (72), G (73), A (74), F (72)
sax_notes = [
    (1.5, 72, 110), (1.5 + 0.25, 73, 110), (1.5 + 0.5, 74, 110), (1.5 + 0.75, 72, 110),
    (3.0, 72, 110), (3.0 + 0.25, 73, 110), (3.0 + 0.5, 74, 110), (3.0 + 0.75, 72, 110)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (start, 36, 110), (start + 0.375, 42, 100), (start + 0.75, 38, 110), (start + 1.125, 42, 100),
        (start + 1.5, 36, 110), (start + 1.875, 42, 100), (start + 2.25, 38, 110), (start + 2.625, 42, 100)
    ]
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
