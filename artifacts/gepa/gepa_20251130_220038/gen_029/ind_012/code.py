
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
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 36),
    (1.875, 38), (2.25, 42), (2.625, 42), (3.0, 42), (3.375, 36),
    (3.75, 38), (4.125, 42), (4.5, 42), (4.875, 42), (5.25, 36),
    (5.625, 38), (6.0, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: chromatic walking line
bass_notes = [
    (1.5, 53), (1.875, 54), (2.25, 52), (2.625, 51), (3.0, 53),
    (3.375, 54), (3.75, 52), (4.125, 51), (4.5, 53),
    (4.875, 54), (5.25, 52), (5.625, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 71),  # Fm7: F, Ab, C, Eb
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Dante on saxophone: short motif with space
sax_notes = [
    (1.5, 62), (1.5, 67), (1.6875, 69), (1.875, 62),  # F, Ab, Bb, F
    (2.25, 62), (2.25, 67), (2.4375, 69), (2.625, 62),  # F, Ab, Bb, F
    (3.0, 62), (3.0, 67), (3.1875, 69), (3.375, 62),  # F, Ab, Bb, F
    (3.75, 62), (3.75, 67), (3.9375, 69), (4.125, 62),  # F, Ab, Bb, F
    (4.5, 62), (4.5, 67), (4.6875, 69), (4.875, 62),  # F, Ab, Bb, F
    (5.25, 62), (5.25, 67), (5.4375, 69), (5.625, 62),  # F, Ab, Bb, F
    (6.0, 62)  # End on F, unresolved
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: chromatic walking line
bass_notes = [
    (3.0, 53), (3.375, 54), (3.75, 52), (4.125, 51), (4.5, 53),
    (4.875, 54), (5.25, 52), (5.625, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),  # Fm7: F, Ab, C, Eb
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71),
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Dante on saxophone: build on motif, leave it hanging
sax_notes = [
    (3.0, 62), (3.0, 67), (3.1875, 69), (3.375, 62),  # F, Ab, Bb, F
    (3.75, 62), (3.75, 67), (3.9375, 69), (4.125, 62),  # F, Ab, Bb, F
    (4.5, 62), (4.5, 67), (4.6875, 69), (4.875, 62),  # F, Ab, Bb, F
    (5.25, 62), (5.25, 67), (5.4375, 69), (5.625, 62)  # F, Ab, Bb, F
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: chromatic walking line
bass_notes = [
    (4.5, 53), (4.875, 54), (5.25, 52), (5.625, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71),  # Fm7: F, Ab, C, Eb
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71),
    (6.0, 62), (6.0, 67), (6.0, 69), (6.0, 71)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Dante on saxophone: end with a whisper
sax_notes = [
    (4.5, 62), (4.5, 67), (4.6875, 69), (4.875, 62),  # F, Ab, Bb, F
    (5.25, 62), (5.25, 67), (5.4375, 69), (5.625, 62),  # F, Ab, Bb, F
    (6.0, 62)  # End on F, unresolved
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
