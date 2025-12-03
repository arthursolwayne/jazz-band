
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C, Bb, Ab, F, Eb
# Fm: F, Ab, D, C, Bb, Ab, F, Eb
bass_notes = [
    (1.5, 38), (1.875, 41), (2.25, 43), (2.625, 40),
    (3.0, 40), (3.375, 38), (3.75, 43), (4.125, 38),
    (4.5, 40), (4.875, 41), (5.25, 43), (5.625, 40)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm9 (F, Ab, C, Eb, G)
# Bar 3: Ab7 (Ab, C, Eb, Gb)
# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    # Bar 2
    (1.5, 53), (1.5, 60), (1.5, 64), (1.5, 65), (1.5, 69),
    # Bar 3
    (3.0, 60), (3.0, 64), (3.0, 65), (3.0, 66),
    # Bar 4
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71)
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: short motif, sing, leave it hanging
# Fm: F, Ab, D, C
sax_notes = [
    (1.5, 53), (1.875, 58), (2.25, 62), (2.625, 60),
    (3.0, 53), (3.375, 58), (3.75, 62), (4.125, 60),
    (4.5, 53), (4.875, 58), (5.25, 62), (5.625, 60)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
