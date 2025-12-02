
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
bar_length = 1.5  # seconds per bar at 120 BPM

# Drums - Bar 1
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100),  # Hihat on 2
    (1.25, 38, 100),  # Snare on 3
    (1.5, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 2: Full ensemble
# Saxophone motif
sax_notes = [
    (0.0, 62, 100),  # E (C7)
    (0.375, 64, 100),  # G (C7)
    (0.75, 60, 100),  # E (C7)
    (1.125, 62, 100)  # E (C7)
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(n)

# Bass - Walking line: C - Bb - B - C
bass_notes = [
    (0.0, 60, 100),  # C
    (0.375, 70, 100),  # Bb (chromatic)
    (0.75, 71, 100),  # B
    (1.125, 60, 100)  # C
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4: C7 on 2, F7 on 4
piano_notes = [
    # C7 on beat 2
    (0.375, 60, 100),  # C
    (0.375, 64, 100),  # E
    (0.375, 67, 100),  # G
    (0.375, 71, 100),  # B
    # F7 on beat 4
    (1.125, 53, 100),  # F
    (1.125, 58, 100),  # A
    (1.125, 60, 100),  # Bb
    (1.125, 64, 100)   # C
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Drums - Bar 2
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 38, 100),  # Snare on 2
    (1.25, 36, 100),  # Kick on 3
    (1.5, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 3: Full ensemble
# Saxophone motif (repeat)
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time + 1.5, end=time + 1.6)
    sax.notes.append(n)

# Bass - Walking line: F - E - F - G
bass_notes = [
    (1.5, 53, 100),  # F
    (1.875, 64, 100),  # E (chromatic)
    (2.25, 53, 100),  # F
    (2.625, 55, 100)  # G
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4: F7 on 2, Bb7 on 4
piano_notes = [
    # F7 on beat 2
    (1.875, 53, 100),  # F
    (1.875, 58, 100),  # A
    (1.875, 60, 100),  # Bb
    (1.875, 64, 100),  # C
    # Bb7 on beat 4
    (2.625, 71, 100),  # Bb
    (2.625, 74, 100),  # D
    (2.625, 76, 100),  # F
    (2.625, 80, 100)   # A
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Drums - Bar 3
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (2.25, 38, 100),  # Snare on 2
    (2.75, 36, 100),  # Kick on 3
    (3.0, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 4: Full ensemble
# Saxophone motif (repeat)
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time + 3.0, end=time + 3.1)
    sax.notes.append(n)

# Bass - Walking line: Bb - A - Bb - C
bass_notes = [
    (3.0, 71, 100),  # Bb
    (3.375, 69, 100),  # A (chromatic)
    (3.75, 71, 100),  # Bb
    (4.125, 60, 100)  # C
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4: Bb7 on 2, Eb7 on 4
piano_notes = [
    # Bb7 on beat 2
    (3.375, 71, 100),  # Bb
    (3.375, 74, 100),  # D
    (3.375, 76, 100),  # F
    (3.375, 80, 100),  # A
    # Eb7 on beat 4
    (4.125, 64, 100),  # Eb
    (4.125, 67, 100),  # G
    (4.125, 69, 100),  # Bb
    (4.125, 72, 100)   # D
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Drums - Bar 4
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.75, 38, 100),  # Snare on 2
    (4.25, 36, 100),  # Kick on 3
    (4.5, 42, 100)    # Hihat on 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("jazz_intro.mid")
