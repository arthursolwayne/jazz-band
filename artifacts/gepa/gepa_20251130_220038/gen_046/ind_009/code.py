
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet starts here (1.5 - 3.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 52),
    (3.0, 51), (3.375, 50), (3.75, 49), (4.125, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 72),
    (2.625, 62), (2.625, 67), (2.625, 69), (2.625, 72),
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 72),
    (4.125, 62), (4.125, 67), (4.125, 69), (4.125, 72)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax melody - short motif, starts in bar 2
sax_notes = [
    (1.5, 65), (1.875, 69), (2.25, 67), (2.625, 65),
    (3.0, 62), (3.375, 65), (3.75, 69), (4.125, 67)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Continue the quartet (3.0 - 4.5s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    (3.0, 50), (3.375, 49), (3.75, 51), (4.125, 52),
    (4.5, 51), (4.875, 50), (5.25, 49), (5.625, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 72),
    (4.125, 62), (4.125, 67), (4.125, 69), (4.125, 72),
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 72),
    (5.625, 62), (5.625, 67), (5.625, 69), (5.625, 72)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax melody - continuation with space and tension
sax_notes = [
    (3.0, 62), (3.375, 65), (3.75, rest), (4.125, rest),
    (4.5, 65), (4.875, 69), (5.25, 67), (5.625, 65)
]
for time, note in sax_notes:
    if note == 'rest':
        continue
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bar 4: End the piece (4.5 - 6.0s)

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bass line - walking line, chromatic approaches
bass_notes = [
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 52),
    (6.0, 51), (6.375, 50), (6.75, 49), (7.125, 51)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 72),
    (5.625, 62), (5.625, 67), (5.625, 69), (5.625, 72),
    (6.0, 62), (6.0, 67), (6.0, 69), (6.0, 72),
    (7.125, 62), (7.125, 67), (7.125, 69), (7.125, 72)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax melody - resolution with emotional clarity
sax_notes = [
    (4.5, 62), (4.875, 65), (5.25, 69), (5.625, 67),
    (6.0, 65), (6.375, 62), (6.75, 65), (7.125, 69)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
