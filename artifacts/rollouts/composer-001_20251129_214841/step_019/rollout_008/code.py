
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.75, 42, 100), # Hihat on &2
    (2.0, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.75, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    (1.5, 60, 100),  # C (1)
    (2.0, 61, 100),  # C# (2)
    (2.5, 62, 100),  # D (3)
    (3.0, 63, 100),  # D# (4)
    (3.5, 64, 100),  # E (1)
    (4.0, 65, 100),  # F (2)
    (4.5, 66, 100),  # F# (3)
    (5.0, 67, 100),  # G (4)
    (5.5, 68, 100),  # G# (1)
    (6.0, 69, 100)   # A (2)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 60, 100),  # C7 (2)
    (2.0, 64, 100),  # E7
    (2.0, 67, 100),  # G7
    (2.0, 71, 100),  # B7
    (4.0, 60, 100),  # C7 (4)
    (4.0, 64, 100),  # E7
    (4.0, 67, 100),  # G7
    (4.0, 71, 100),  # B7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bars 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (2.0, 38, 100),  # Snare on 2
    (2.5, 36, 100),  # Kick on 3
    (3.0, 38, 100),  # Snare on 4
    (3.5, 36, 100),  # Kick on 1
    (4.0, 38, 100),  # Snare on 2
    (4.5, 36, 100),  # Kick on 3
    (5.0, 38, 100),  # Snare on 4
    (5.5, 36, 100),  # Kick on 1
    (6.0, 38, 100),  # Snare on 2
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Dante - One short motif, make it sing
sax_notes = [
    (1.5, 65, 100),  # E (1)
    (2.0, 67, 100),  # G (2)
    (2.5, 69, 100),  # A (3)
    (3.0, 67, 100),  # G (4)
    (3.5, 65, 100),  # E (1)
    (4.0, 62, 100),  # D (2)
    (4.5, 60, 100),  # C (3)
    (5.0, 62, 100),  # D (4)
    (5.5, 65, 100),  # E (1)
    (6.0, 67, 100)   # G (2)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
