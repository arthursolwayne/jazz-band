
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 48), (1.75, 50), (2.0, 49), (2.25, 51),
    (2.5, 52), (2.75, 50), (3.0, 49), (3.25, 51),
    # Bar 3 (3.0 - 4.5s)
    (3.5, 51), (3.75, 53), (4.0, 52), (4.25, 50),
    (4.5, 51), (4.75, 53), (5.0, 52), (5.25, 50),
    # Bar 4 (4.5 - 6.0s)
    (5.5, 50), (5.75, 52), (6.0, 51), (6.25, 53)
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (2.0, 64), (2.0, 67), (2.0, 69), (2.0, 71),
    (2.25, 64), (2.25, 67), (2.25, 69), (2.25, 71),
    # Bar 3: Bb7 on 2 and 4
    (3.5, 62), (3.5, 65), (3.5, 67), (3.5, 69),
    (3.75, 62), (3.75, 65), (3.75, 67), (3.75, 69),
    # Bar 4: E7 on 2 and 4
    (5.0, 59), (5.0, 62), (5.0, 64), (5.0, 67),
    (5.25, 59), (5.25, 62), (5.25, 64), (5.25, 67)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Saxophone (Dante) - simple, emotionally charged motif
sax_notes = [
    # Bar 2: F (start), Bb (end of bar 2)
    (2.0, 75), (2.75, 78),
    # Bar 3: E (start), D (end of bar 3)
    (3.5, 73), (4.25, 71),
    # Bar 4: F (start), Bb (end of bar 4)
    (5.0, 75), (5.75, 78)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
