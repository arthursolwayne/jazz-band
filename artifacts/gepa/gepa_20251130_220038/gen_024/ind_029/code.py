
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
    # Bar 1 (0.0 - 1.5s)
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time = 1.5s to 6.0s (4.5s total)

# Bass line: Marcus (walking line in Fm)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.875, 62), (2.25, 60), (2.625, 58), (3.0, 64),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62), (3.375, 60), (3.75, 58), (4.125, 57), (4.5, 62),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 60), (4.875, 58), (5.25, 57), (5.625, 55), (6.0, 60)
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Diane (comping on 2 and 4 with 7th chords in Fm)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 47), (1.5, 49), (1.5, 50), (1.5, 52),  # F7
    (2.0, 47), (2.0, 49), (2.0, 50), (2.0, 52),  # F7
    (2.5, 47), (2.5, 49), (2.5, 50), (2.5, 52),  # F7
    (3.0, 47), (3.0, 49), (3.0, 50), (3.0, 52),  # F7
    # Bar 3 (3.0 - 4.5s)
    (3.0, 47), (3.0, 49), (3.0, 50), (3.0, 52),  # F7
    (3.5, 47), (3.5, 49), (3.5, 50), (3.5, 52),  # F7
    (4.0, 47), (4.0, 49), (4.0, 50), (4.0, 52),  # F7
    (4.5, 47), (4.5, 49), (4.5, 50), (4.5, 52),  # F7
    # Bar 4 (4.5 - 6.0s)
    (4.5, 47), (4.5, 49), (4.5, 50), (4.5, 52),  # F7
    (5.0, 47), (5.0, 49), (5.0, 50), (5.0, 52),  # F7
    (5.5, 47), (5.5, 49), (5.5, 50), (5.5, 52),  # F7
    (6.0, 47), (6.0, 49), (6.0, 50), (6.0, 52)   # F7
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Sax: Dante (melody in Fm)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 66), (1.875, 64), (2.25, 66), (2.625, 64), (3.0, 66),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 64), (4.5, 62),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 66), (4.875, 64), (5.25, 66), (5.625, 64), (6.0, 66)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
