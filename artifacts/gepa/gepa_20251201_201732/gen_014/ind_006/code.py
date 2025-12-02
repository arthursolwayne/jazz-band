
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 41),
    (3.0, 41), (3.375, 43), (3.75, 41), (4.125, 39),
    (4.5, 39), (4.875, 41), (5.25, 39), (5.625, 40)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 48), (1.5, 60), (1.5, 64), (1.5, 65),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 62), (3.0, 67), (3.0, 64), (3.0, 60),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (4.5, 60), (4.5, 63), (4.5, 67), (4.5, 62)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.75, 64), (2.0, 62), (2.5, 62),
    (3.25, 64), (3.5, 62), (3.75, 60), (4.25, 62),
    (5.0, 64), (5.25, 62), (5.5, 60), (6.0, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter.mid")
