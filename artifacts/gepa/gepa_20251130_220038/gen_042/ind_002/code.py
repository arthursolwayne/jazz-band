
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42),
    (1.5, 36), (1.875, 38), (2.25, 42), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 42), (4.125, 42),
    (4.5, 36), (4.875, 38), (5.25, 42), (5.625, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Walking line, chromatic approaches, never the same note twice)
bass_notes = [
    (1.5, 45), (1.875, 46), (2.25, 44), (2.625, 45),
    (3.0, 47), (3.375, 45), (3.75, 44), (4.125, 46),
    (4.5, 43), (4.875, 44), (5.25, 46), (5.625, 47)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 65), (2.25, 69), (2.25, 72), (2.25, 76),  # F7
    # Bar 3
    (3.75, 65), (3.75, 69), (3.75, 72), (3.75, 76),  # F7
    # Bar 4
    (5.25, 65), (5.25, 69), (5.25, 72), (5.25, 76)   # F7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), (1.875, 69), (2.25, 71), (2.625, 69),
    (3.0, 66), (3.375, 62), (3.75, 64), (4.125, 62),
    (4.5, 66), (4.875, 69), (5.25, 71), (5.625, 69)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_moment.mid")
