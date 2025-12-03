
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
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=0.0, end=1.5)
    drums.notes.append(drum_note)
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=3.0)
    drums.notes.append(drum_note)
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=4.5)
    drums.notes.append(drum_note)
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=6.0)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2) - G2 (G2) - A2 (A2) - B2 (B2)
bass_notes = [38, 43, 45, 47]
for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=1.5 + i*1.5, end=1.5 + (i+1)*1.5)
    bass.notes.append(bass_note)

# Piano: D7 (D7) - G7 (G7) - A7 (A7) - B7 (B7)
piano_notes = [74, 78, 80, 82]
for i, note in enumerate(piano_notes):
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=1.5 + i*1.5, end=1.5 + (i+1)*1.5)
    piano.notes.append(piano_note)

# Sax: D5 (D5) - E5 (E5) - F#5 (F#5) - G5 (G5)
sax_notes = [74, 76, 78, 80]
for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=1.5 + i*1.5, end=1.5 + (i+1)*1.5)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (D2) - F#2 (F#2) - G2 (G2) - A2 (A2)
bass_notes = [38, 42, 43, 45]
for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=3.0 + i*1.5, end=3.0 + (i+1)*1.5)
    bass.notes.append(bass_note)

# Piano: D7 (D7) - F#7 (F#7) - G7 (G7) - A7 (A7)
piano_notes = [74, 77, 78, 80]
for i, note in enumerate(piano_notes):
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=3.0 + i*1.5, end=3.0 + (i+1)*1.5)
    piano.notes.append(piano_note)

# Sax: D5 (D5) - F#5 (F#5) - G5 (G5) - A5 (A5)
sax_notes = [74, 77, 78, 80]
for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=3.0 + i*1.5, end=3.0 + (i+1)*1.5)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (D2) - G2 (G2) - A2 (A2) - B2 (B2)
bass_notes = [38, 43, 45, 47]
for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=4.5 + i*1.5, end=4.5 + (i+1)*1.5)
    bass.notes.append(bass_note)

# Piano: D7 (D7) - G7 (G7) - A7 (A7) - B7 (B7)
piano_notes = [74, 78, 80, 82]
for i, note in enumerate(piano_notes):
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=4.5 + i*1.5, end=4.5 + (i+1)*1.5)
    piano.notes.append(piano_note)

# Sax: D5 (D5) - E5 (E5) - F#5 (F#5) - G5 (G5)
sax_notes = [74, 76, 78, 80]
for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=4.5 + i*1.5, end=4.5 + (i+1)*1.5)
    sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
