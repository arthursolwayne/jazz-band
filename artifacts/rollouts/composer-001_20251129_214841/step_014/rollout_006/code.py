
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: C - E - G - Bb - C (motif)
sax_notes = [
    (1.5, 60, 100),  # C4
    (1.75, 64, 100), # E4
    (2.0, 67, 100),  # G4
    (2.25, 70, 100), # Bb4
    (2.5, 60, 100)   # C4
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: walking C minor
bass_notes = [
    (1.5, 48, 80),  # C3
    (1.75, 50, 80), # D#3
    (2.0, 48, 80),  # C3
    (2.25, 51, 80), # F3
    (2.5, 53, 80),  # G#3
    (2.75, 51, 80), # F3
    (3.0, 50, 80),  # D#3
    (3.25, 48, 80)  # C3
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 60, 100),  # C7 (C E G B)
    (1.75, 64, 100),
    (1.75, 67, 100),
    (1.75, 71, 100),
    (2.25, 60, 100),
    (2.25, 64, 100),
    (2.25, 67, 100),
    (2.25, 71, 100)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat and vary motif
sax_notes = [
    (3.0, 60, 100),  # C4
    (3.25, 64, 100), # E4
    (3.5, 67, 100),  # G4
    (3.75, 70, 100), # Bb4
    (4.0, 60, 100)   # C4
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: walking C minor
bass_notes = [
    (3.0, 48, 80),  # C3
    (3.25, 50, 80), # D#3
    (3.5, 48, 80),  # C3
    (3.75, 51, 80), # F3
    (4.0, 53, 80),  # G#3
    (4.25, 51, 80), # F3
    (4.5, 50, 80),  # D#3
    (4.75, 48, 80)  # C3
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 60, 100),
    (3.25, 64, 100),
    (3.25, 67, 100),
    (3.25, 71, 100),
    (3.75, 60, 100),
    (3.75, 64, 100),
    (3.75, 67, 100),
    (3.75, 71, 100)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.25, 42, 100), # Hihat on &1
    (3.5, 38, 100),  # Snare on 2
    (3.75, 42, 100), # Hihat on &2
    (4.0, 36, 100),  # Kick on 3
    (4.25, 42, 100), # Hihat on &3
    (4.5, 38, 100),  # Snare on 4
    (4.75, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif, resolve
sax_notes = [
    (4.5, 60, 100),  # C4
    (4.75, 64, 100), # E4
    (5.0, 67, 100),  # G4
    (5.25, 70, 100), # Bb4
    (5.5, 60, 100)   # C4
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: walking C minor
bass_notes = [
    (4.5, 48, 80),  # C3
    (4.75, 50, 80), # D#3
    (5.0, 48, 80),  # C3
    (5.25, 51, 80), # F3
    (5.5, 53, 80),  # G#3
    (5.75, 51, 80), # F3
    (6.0, 50, 80),  # D#3
    (6.25, 48, 80)  # C3
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 60, 100),
    (4.75, 64, 100),
    (4.75, 67, 100),
    (4.75, 71, 100),
    (5.25, 60, 100),
    (5.25, 64, 100),
    (5.25, 67, 100),
    (5.25, 71, 100)
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.75, 42, 100), # Hihat on &1
    (5.0, 38, 100),  # Snare on 2
    (5.25, 42, 100), # Hihat on &2
    (5.5, 36, 100),  # Kick on 3
    (5.75, 42, 100), # Hihat on &3
    (6.0, 38, 100),  # Snare on 4
    (6.25, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
