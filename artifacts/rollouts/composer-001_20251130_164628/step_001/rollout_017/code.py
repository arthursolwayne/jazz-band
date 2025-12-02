
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

# Drums in bar 1
drum_notes = [
    (0.0, 36),  # kick on 1
    (0.75, 42), # hihat on 2
    (1.125, 38), # snare on 3
    (1.5, 42)   # hihat on 4
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif - D (D4), F# (F#4), G (G4), B (B4)
sax_notes = [
    (1.5, 62),  # D4
    (1.75, 66), # F#4
    (2.0, 67),  # G4
    (2.25, 71)  # B4
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 62),  # D4
    (1.75, 63), # Eb4
    (2.0, 65),  # F#4
    (2.25, 67)  # G4
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 64),  # D7: D, F#, A, C
    (1.75, 67),  # D7
    (1.75, 71),  # D7
    (1.75, 69),  # D7
    (2.25, 64),  # D7
    (2.25, 67),  # D7
    (2.25, 71),  # D7
    (2.25, 69)   # D7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Drums in bar 2
drum_notes = [
    (1.5, 36),  # kick on 1
    (1.75, 42), # hihat on 2
    (2.0, 38),  # snare on 3
    (2.25, 42)  # hihat on 4
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif
sax_notes = [
    (3.0, 62),  # D4
    (3.25, 66), # F#4
    (3.5, 67),  # G4
    (3.75, 71)  # B4
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: walking line with chromatic approaches
bass_notes = [
    (3.0, 67),  # G4
    (3.25, 69), # A4
    (3.5, 71),  # B4
    (3.75, 72)  # C5
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 64),  # D7: D, F#, A, C
    (3.25, 67),  # D7
    (3.25, 71),  # D7
    (3.25, 69),  # D7
    (3.75, 64),  # D7
    (3.75, 67),  # D7
    (3.75, 71),  # D7
    (3.75, 69)   # D7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Drums in bar 3
drum_notes = [
    (3.0, 36),  # kick on 1
    (3.25, 42), # hihat on 2
    (3.5, 38),  # snare on 3
    (3.75, 42)  # hihat on 4
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif and leave it hanging
sax_notes = [
    (4.5, 62),  # D4
    (4.75, 66), # F#4
    (5.0, 67),  # G4
    (5.25, 71)  # B4
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bass: walking line with chromatic approaches
bass_notes = [
    (4.5, 72),  # C5
    (4.75, 71), # B4
    (5.0, 69),  # A4
    (5.25, 67)  # G4
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 64),  # D7: D, F#, A, C
    (4.75, 67),  # D7
    (4.75, 71),  # D7
    (4.75, 69),  # D7
    (5.25, 64),  # D7
    (5.25, 67),  # D7
    (5.25, 71),  # D7
    (5.25, 69)   # D7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Drums in bar 4
drum_notes = [
    (4.5, 36),  # kick on 1
    (4.75, 42), # hihat on 2
    (5.0, 38),  # snare on 3
    (5.25, 42)  # hihat on 4
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
