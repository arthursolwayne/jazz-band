
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5s)
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 50),
    # Bar 3 (3.0s)
    (3.0, 50), (3.375, 49), (3.75, 51), (4.125, 50),
    # Bar 4 (4.5s)
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    (1.5, 70), (1.5, 72), (1.5, 74), (1.5, 77),  # Dm7
    (1.875, 70), (1.875, 72), (1.875, 74), (1.875, 77),
    (2.25, 70), (2.25, 72), (2.25, 74), (2.25, 77),
    (2.625, 70), (2.625, 72), (2.625, 74), (2.625, 77),
    # Bar 3 (3.0s)
    (3.0, 70), (3.0, 72), (3.0, 74), (3.0, 77),
    (3.375, 70), (3.375, 72), (3.375, 74), (3.375, 77),
    (3.75, 70), (3.75, 72), (3.75, 74), (3.75, 77),
    (4.125, 70), (4.125, 72), (4.125, 74), (4.125, 77),
    # Bar 4 (4.5s)
    (4.5, 70), (4.5, 72), (4.5, 74), (4.5, 77),
    (4.875, 70), (4.875, 72), (4.875, 74), (4.875, 77),
    (5.25, 70), (5.25, 72), (5.25, 74), (5.25, 77),
    (5.625, 70), (5.625, 72), (5.625, 74), (5.625, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + x * 0.375 for x in range(4)]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5s)
    (1.5, 62), (1.625, 65), (1.75, 67),  # Dm motif
    # Bar 3 (3.0s)
    (3.0, 62), (3.125, 65), (3.25, 67),
    # Bar 4 (4.5s)
    (4.5, 62), (4.625, 65), (4.75, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
