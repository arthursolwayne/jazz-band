
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (1.5, 64), (1.75, 65), (2.0, 66), (2.25, 67),  # F7 chord
    (2.5, 65), (2.75, 64), (3.0, 63), (3.25, 62),  # Fm7 chord
    (3.5, 62), (3.75, 63), (4.0, 64), (4.25, 65),  # F7 chord
    (4.5, 65), (4.75, 64), (5.0, 63), (5.25, 62)   # Fm7 chord
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    (2.0, 64), (2.0, 69), (2.0, 71), (2.0, 73),  # F7
    (3.0, 64), (3.0, 69), (3.0, 71), (3.0, 72),  # Fm7
    (4.0, 64), (4.0, 69), (4.0, 71), (4.0, 73),  # F7
    (5.0, 64), (5.0, 69), (5.0, 71), (5.0, 72)   # Fm7
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums: Continue pattern
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Saxophone: Dante (melody)
sax_notes = [
    (1.5, 69), (1.75, 71), (2.0, 72), (2.25, 71),  # Whisper
    (2.5, 72), (2.75, 71), (3.0, 69), (3.25, 67),  # Build
    (3.5, 69), (3.75, 71), (4.0, 72), (4.25, 71),  # Cry
    (4.5, 72), (4.75, 71), (5.0, 69), (5.25, 67)   # Breath
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
