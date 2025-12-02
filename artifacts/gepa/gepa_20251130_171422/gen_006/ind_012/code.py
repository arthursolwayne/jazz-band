
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
drum_notes_bar1 = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes_bar1:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D
    (1.75, 60, 100), # C
    (2.0, 63, 100),  # D#
    (2.25, 62, 100), # D
    (2.5, 67, 100),  # G
    (2.75, 65, 100), # F#
    (3.0, 67, 100),  # G
    (3.25, 69, 100), # A
    (3.5, 71, 100),  # B
    (3.75, 72, 100), # C
    (4.0, 71, 100),  # B
    (4.25, 69, 100), # A
    (4.5, 67, 100),  # G
    (4.75, 65, 100), # F#
    (5.0, 62, 100),  # D
    (5.25, 60, 100), # C
    (5.5, 63, 100),  # D#
    (5.75, 62, 100)  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67, 100),  # G7 (G, B, D, F)
    (1.5, 69, 100),
    (1.5, 62, 100),
    (1.5, 60, 100),
    (1.75, 62, 100),  # D7 (D, F#, A, C)
    (1.75, 64, 100),
    (1.75, 67, 100),
    (1.75, 60, 100),
    (2.0, 67, 100),  # G7
    (2.0, 69, 100),
    (2.0, 62, 100),
    (2.0, 60, 100),
    (2.25, 62, 100),  # D7
    (2.25, 64, 100),
    (2.25, 67, 100),
    (2.25, 60, 100),
    (2.5, 67, 100),  # G7
    (2.5, 69, 100),
    (2.5, 62, 100),
    (2.5, 60, 100),
    (2.75, 62, 100),  # D7
    (2.75, 64, 100),
    (2.75, 67, 100),
    (2.75, 60, 100),
    (3.0, 67, 100),  # G7
    (3.0, 69, 100),
    (3.0, 62, 100),
    (3.0, 60, 100),
    (3.25, 62, 100),  # D7
    (3.25, 64, 100),
    (3.25, 67, 100),
    (3.25, 60, 100),
    (3.5, 67, 100),  # G7
    (3.5, 69, 100),
    (3.5, 62, 100),
    (3.5, 60, 100),
    (3.75, 62, 100),  # D7
    (3.75, 64, 100),
    (3.75, 67, 100),
    (3.75, 60, 100),
    (4.0, 67, 100),  # G7
    (4.0, 69, 100),
    (4.0, 62, 100),
    (4.0, 60, 100),
    (4.25, 62, 100),  # D7
    (4.25, 64, 100),
    (4.25, 67, 100),
    (4.25, 60, 100),
    (4.5, 67, 100),  # G7
    (4.5, 69, 100),
    (4.5, 62, 100),
    (4.5, 60, 100),
    (4.75, 62, 100),  # D7
    (4.75, 64, 100),
    (4.75, 67, 100),
    (4.75, 60, 100),
    (5.0, 67, 100),  # G7
    (5.0, 69, 100),
    (5.0, 62, 100),
    (5.0, 60, 100),
    (5.25, 62, 100),  # D7
    (5.25, 64, 100),
    (5.25, 67, 100),
    (5.25, 60, 100),
    (5.5, 67, 100),  # G7
    (5.5, 69, 100),
    (5.5, 62, 100),
    (5.5, 60, 100),
    (5.75, 62, 100)   # D7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D, F#, A, D - but with a twist
sax_notes = [
    (1.5, 62, 100),  # D
    (1.625, 65, 100),  # F#
    (1.75, 69, 100),  # A
    (2.0, 62, 100),  # D
    (2.5, 62, 100),  # D (reprise)
    (2.625, 65, 100),  # F#
    (2.75, 69, 100),  # A
    (3.0, 62, 100)   # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for bars 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
    (5.5, 36, 100),  # Kick on 1
    (5.75, 42, 100)  # Hihat on &1
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
