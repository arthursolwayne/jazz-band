
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [i * 0.375 for i in range(0, 16)]

for time in kick_times:
    note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in snare_times:
    note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
    drums.notes.append(note)

for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (1.5, 62), (1.75, 64), (2.0, 65), (2.25, 62),
    # Bar 3
    (2.5, 60), (2.75, 62), (3.0, 64), (3.25, 65),
    # Bar 4
    (3.5, 62), (3.75, 64), (4.0, 65), (4.25, 62),
    # Ending chromatic run
    (4.5, 60), (4.75, 62), (5.0, 64), (5.25, 65)
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 69), (2.0, 67), (2.0, 64), (2.0, 62),  # D7
    # Bar 3
    (3.0, 71), (3.0, 69), (3.0, 66), (3.0, 64),  # F#7
    # Bar 4
    (4.0, 74), (4.0, 72), (4.0, 69), (4.0, 67)   # A7
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.75, 67), (2.0, 69), (2.25, 71),  # First phrase
    (2.5, 69), (2.75, 67), (3.0, 65), (3.25, 64),  # Second phrase
    (3.5, 65), (3.75, 67), (4.0, 69), (4.25, 71),  # Third phrase
    (4.5, 67), (4.75, 65), (5.0, 64), (5.25, 62)   # Resolution
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
