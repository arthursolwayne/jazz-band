
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 90),  # Hihat on &1
    (1.125, 42, 90), # Hihat on &2
    (1.5, 38, 100)   # Snare on 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Saxophone - Bar 2: Melody
sax_notes = [
    (1.5, 62, 100),  # D4
    (1.75, 65, 100), # F#4
    (2.0, 62, 90),   # D4
    (2.25, 60, 90),  # C4
    (2.5, 62, 100),  # D4
    (2.75, 65, 100), # F#4
    (3.0, 62, 90)    # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass - Bar 2: Walking line
bass_notes = [
    (1.5, 50, 80),   # D3
    (1.75, 49, 80),  # C#3
    (2.0, 51, 80),   # D#3
    (2.25, 50, 80),  # D3
    (2.5, 52, 80),   # E3
    (2.75, 51, 80),  # D#3
    (3.0, 50, 80)    # D3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano - Bar 2: 7th chords on 2 and 4
piano_notes = [
    (1.75, 62, 80),  # D7 - D
    (1.75, 67, 80),  # F#7 - F#
    (1.75, 72, 80),  # A7 - A
    (1.75, 74, 80),  # B7 - B
    (2.25, 62, 80),  # D7 - D
    (2.25, 67, 80),  # F#7 - F#
    (2.25, 72, 80),  # A7 - A
    (2.25, 74, 80),  # B7 - B
    (2.75, 62, 80),  # D7 - D
    (2.75, 67, 80),  # F#7 - F#
    (2.75, 72, 80),  # A7 - A
    (2.75, 74, 80),  # B7 - B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums - Bar 2
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 90),  # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 90),  # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 90),  # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 90)   # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)

# Saxophone - Bar 3: Melody continuation
sax_notes = [
    (3.0, 62, 100),  # D4
    (3.25, 67, 100), # G4
    (3.5, 62, 90),   # D4
    (3.75, 60, 90),  # C4
    (4.0, 62, 100),  # D4
    (4.25, 67, 100), # G4
    (4.5, 62, 90)    # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass - Bar 3: Walking line
bass_notes = [
    (3.0, 50, 80),   # D3
    (3.25, 51, 80),  # D#3
    (3.5, 52, 80),   # E3
    (3.75, 53, 80),  # F3
    (4.0, 55, 80),   # G3
    (4.25, 53, 80),  # F3
    (4.5, 52, 80)    # E3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano - Bar 3: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62, 80),  # D7 - D
    (3.25, 67, 80),  # F#7 - F#
    (3.25, 72, 80),  # A7 - A
    (3.25, 74, 80),  # B7 - B
    (3.75, 62, 80),  # D7 - D
    (3.75, 67, 80),  # F#7 - F#
    (3.75, 72, 80),  # A7 - A
    (3.75, 74, 80),  # B7 - B
    (4.25, 62, 80),  # D7 - D
    (4.25, 67, 80),  # F#7 - F#
    (4.25, 72, 80),  # A7 - A
    (4.25, 74, 80),  # B7 - B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums - Bar 3
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.25, 42, 90),  # Hihat on &1
    (3.5, 38, 100),  # Snare on 2
    (3.75, 42, 90),  # Hihat on &2
    (4.0, 36, 100),  # Kick on 3
    (4.25, 42, 90),  # Hihat on &3
    (4.5, 38, 100),  # Snare on 4
    (4.75, 42, 90)   # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Saxophone - Bar 4: Melody resolution
sax_notes = [
    (4.5, 62, 100),  # D4
    (4.75, 65, 100), # F#4
    (5.0, 62, 90),   # D4
    (5.25, 60, 90),  # C4
    (5.5, 62, 100),  # D4
    (5.75, 65, 100), # F#4
    (6.0, 62, 90)    # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass - Bar 4: Walking line
bass_notes = [
    (4.5, 50, 80),   # D3
    (4.75, 51, 80),  # D#3
    (5.0, 52, 80),   # E3
    (5.25, 53, 80),  # F3
    (5.5, 55, 80),   # G3
    (5.75, 53, 80),  # F3
    (6.0, 52, 80)    # E3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano - Bar 4: 7th chords on 2 and 4
piano_notes = [
    (4.75, 62, 80),  # D7 - D
    (4.75, 67, 80),  # F#7 - F#
    (4.75, 72, 80),  # A7 - A
    (4.75, 74, 80),  # B7 - B
    (5.25, 62, 80),  # D7 - D
    (5.25, 67, 80),  # F#7 - F#
    (5.25, 72, 80),  # A7 - A
    (5.25, 74, 80),  # B7 - B
    (5.75, 62, 80),  # D7 - D
    (5.75, 67, 80),  # F#7 - F#
    (5.75, 72, 80),  # A7 - A
    (5.75, 74, 80),  # B7 - B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums - Bar 4
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.75, 42, 90),  # Hihat on &1
    (5.0, 38, 100),  # Snare on 2
    (5.25, 42, 90),  # Hihat on &2
    (5.5, 36, 100),  # Kick on 3
    (5.75, 42, 90),  # Hihat on &3
    (6.0, 38, 100),  # Snare on 4
    (6.25, 42, 90)   # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
