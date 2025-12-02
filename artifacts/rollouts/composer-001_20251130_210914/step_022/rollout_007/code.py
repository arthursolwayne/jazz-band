
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
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    (1.5, 62, 100), # D
    (1.75, 63, 100), # Eb
    (2.0, 64, 100), # E
    (2.25, 65, 100), # F
    (2.5, 67, 100), # G
    (2.75, 69, 100), # A
    (3.0, 71, 100), # Bb
    (3.25, 72, 100), # B
    (3.5, 74, 100), # C
    (3.75, 76, 100), # Db
    (4.0, 77, 100), # D
    (4.25, 78, 100), # Eb
    (4.5, 79, 100), # E
    (4.75, 80, 100), # F
    (5.0, 82, 100), # G
    (5.25, 84, 100), # A
    (5.5, 86, 100), # Bb
    (5.75, 87, 100)  # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 67, 100), # G7
    (2.0, 74, 100),
    (2.0, 79, 100),
    (2.0, 84, 100),
    # Bar 3
    (3.5, 67, 100), # G7
    (3.5, 74, 100),
    (3.5, 79, 100),
    (3.5, 84, 100),
    # Bar 4
    (5.0, 67, 100), # G7
    (5.0, 74, 100),
    (5.0, 79, 100),
    (5.0, 84, 100),
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.5, 42, 100), # 1
    (1.75, 42, 100), (2.0, 36, 100), (2.0, 42, 100), # &1, 2
    (2.25, 42, 100), (2.5, 36, 100), (2.5, 42, 100), # &2, 3
    (2.75, 42, 100), (3.0, 38, 100), (3.0, 42, 100), # &3, 4
    (3.25, 42, 100), (3.5, 36, 100), (3.5, 42, 100), # &4, 1
    (3.75, 42, 100), (4.0, 38, 100), (4.0, 42, 100), # &1, 2
    (4.25, 42, 100), (4.5, 36, 100), (4.5, 42, 100), # &2, 3
    (4.75, 42, 100), (5.0, 38, 100), (5.0, 42, 100), # &3, 4
    (5.25, 42, 100), (5.5, 36, 100), (5.5, 42, 100), # &4, 1
    (5.75, 42, 100), (6.0, 38, 100), (6.0, 42, 100)  # &1, 2
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax (Dante) - short motif, make it sing
sax_notes = [
    (1.5, 65, 100), # E
    (1.75, 67, 100), # G
    (2.0, 69, 100), # A
    (2.25, 67, 100), # G
    (2.5, 65, 100), # E
    (2.75, 62, 100), # D
    (3.0, 65, 100), # E
    (3.25, 67, 100), # G
    (3.5, 69, 100), # A
    (3.75, 67, 100), # G
    (4.0, 65, 100), # E
    (4.25, 62, 100), # D
    (4.5, 65, 100), # E
    (4.75, 67, 100), # G
    (5.0, 69, 100), # A
    (5.25, 67, 100), # G
    (5.5, 65, 100), # E
    (5.75, 62, 100)  # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
